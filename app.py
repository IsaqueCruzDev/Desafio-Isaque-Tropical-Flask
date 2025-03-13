import pandas as pd
import io
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS  # Importação do CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/uploadfile', methods=['POST'])
def upload_file():
    if 'file' not in request.files: 
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and (file.filename.endswith('.csv') or file.filename.endswith('.xlsx')):
        try:
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file, sep=';', dtype=str)  # Garante que tudo seja string
            else:
                df = pd.read_excel(file, dtype=str)

            # Remover linhas completamente vazias
            df = df.dropna(how='all')

            # Substituir NaN por None (para evitar problemas no JSON)
            df = df.where(pd.notna(df), None)

            # Remover espaços extras no início e fim de cada propriedade
            df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            json_data = df.to_dict(orient='records')

            return jsonify(json_data)  # Retorna JSON válido

        except Exception as e:
            return jsonify({'error': str(e)}), 400
    else:
        return jsonify({'error': 'Unsupported file format'}), 400

@app.route('/xlsxGenerate', methods=['POST'])
def xlsxGenerate():
    try:
        # Receber os dados JSON do frontend
        data = request.get_json()

        # Verificar se os dados foram recebidos corretamente
        if not data or not isinstance(data, list):
            return jsonify({"error": "Invalid data format"}), 400

        # Criar DataFrame
        df = pd.DataFrame(data)

        # Criar um buffer de memória para armazenar o arquivo Excel
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Propriedades")

        # Definir o buffer para leitura e enviar o arquivo
        output.seek(0)
        return send_file(output, 
                         mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", 
                         as_attachment=True, 
                         download_name="propriedades_logs.xlsx")
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)

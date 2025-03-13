# API Python - Processamento de Arquivos CSV e XLSX

## 📌 Sobre a API
Esta API, desenvolvida com **Flask**, permite o upload e processamento de arquivos **CSV/XLSX** e a geração de arquivos **XLSX** com base em dados enviados pelo frontend.

## 🚀 Tecnologias Utilizadas
- **Python 3.x** - Linguagem de programação
- **Flask** - Framework para API
- **Flask-CORS** - Permitir chamadas de origens diferentes (CORS)
- **Pandas** - Manipulação de dados estruturados
- **OpenPyXL** e **XlsxWriter** - Processamento de arquivos Excel

## 📂 Estrutura do Projeto
```
/desafio-api-python/
 ├── app.py                 # Código principal da API
 ├── requirements.txt       # Dependências do projeto
```

## 🔧 Configuração do Ambiente
### **1️⃣ Clonar o Repositório**
```sh
git clone https://github.com/seu-usuario/seu-repositorio.git
cd desafio-api-python
```

### **2️⃣ Criar um Ambiente Virtual (Recomendado)**
```sh
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

### **3️⃣ Instalar Dependências**
```sh
pip install -r requirements.txt
```

### **4️⃣ Executar a API**
```sh
python app.py
```
A API estará rodando em **`http://127.0.0.1:5000`**.

## 📡 Endpoints Disponíveis

### **🔹 1. Upload de Arquivo CSV/XLSX**
**`POST /uploadfile`**

📌 **Descrição:** Permite o upload de um arquivo CSV ou XLSX, processa os dados e retorna um JSON.

🔽 **Exemplo de Request (Frontend/React):**
```js
const formData = new FormData();
formData.append("file", file);
const response = await fetch("http://127.0.0.1:5000/uploadfile", {
    method: "POST",
    body: formData
});
const data = await response.json();
console.log(data);
```

🔼 **Exemplo de Response (JSON)**
```json
[
    { "Nome": "João", "Idade": "25", "Cidade": "São Paulo" },
    { "Nome": "Maria", "Idade": "30", "Cidade": "Rio de Janeiro" }
]
```

📌 **Regras:**
- Remove linhas vazias
- Substitui `NaN` por `null`
- Remove espaços extras nos valores

---

### **🔹 2. Gerar Arquivo XLSX**
**`POST /xlsxGenerate`**

📌 **Descrição:** Recebe um JSON com dados e retorna um arquivo **XLSX** para download.

🔽 **Exemplo de Request (Frontend/React):**
```js
const data = [
    { "Nome": "João", "Idade": "25", "Cidade": "São Paulo" },
    { "Nome": "Maria", "Idade": "30", "Cidade": "Rio de Janeiro" }
];

export const xlsxGenerate = async (data: any) => {
    try {
        const response = await flaskApi.post('/xlsxGenerate', data, {
            responseType: 'blob',
            headers: {
                "Content-Type": "application/json"
            }
        })
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "properties_logs.xlsx"); // Nome do arquivo
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } catch (error) {
        throw error
    }
}
```

📌 **Regras:**
- Gera um arquivo Excel com os dados fornecidos
- Formata corretamente os dados na planilha

---
🚀 **API pronta para processar arquivos CSV/XLSX e gerar relatórios Excel!**


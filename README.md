# API Flask 

Este é um projeto simples de uma API REST desenvolvida com **Python** e **Flask**, que retorna uma mensagem JSON em uma rota GET.

---

## 🚀 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Insomnia](https://insomnia.rest/) — para testar endpoints da API

---

## 📁 Estrutura do Projeto

/main.py -> código principal da API Flask

## ▶️ Como rodar

Execute o arquivo Python:

python main.py

A API está disponível em:

http://127.0.0.1:5000/api

## 🔄 Exemplo de resposta da API

GET http://127.0.0.1:5000/api

{
  "mensagem": "Ola mundo!",
  
  "status": "API funcionando"
}

## 🧪 Testando com o Insomnia

Você pode testar a API com o Insomnia:

1.Abra o Insomnia.

2.Crie uma nova requisição do tipo GET.

3.Cole a URL: http://127.0.0.1:5000/api

4.Clique em Send.

5.Você verá a resposta JSON.


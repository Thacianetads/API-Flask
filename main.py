from flask import Flask, jsonify



app = Flask(__name__)

data = {
    "mensagem":"Ola mundo!",
    "status": "API funcionando"
}

@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
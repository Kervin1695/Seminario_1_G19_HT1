from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/check', methods=['GET'])
def check_status():
    return jsonify({"message" : "OK"}), 200

@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "Instancia": "Maquina 1 - Api 1",
        "Curso": "Seminario de Sistemas 1 A",
        "Grupo": "Grupo #19"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
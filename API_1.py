from flask import Flask, jsonify, request

app = Flask(__name__)

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
    app.run(port=8000, debug=True)
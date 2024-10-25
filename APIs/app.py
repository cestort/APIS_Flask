from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/test', methods=['GET'])
def test_api():
    return jsonify({"message": "La API está funcionando correctamente"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Asignamos un puerto diferente al frontend

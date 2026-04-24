from flask import Flask, jsonify

# Creo la aplicación Flask
app = Flask(__name__)

# Endpoint 1: Chequeo de salud 
@app.route('/api/health', methods=['GET'])
def health_check():
    # Devuelve un JSON confirmando que el servicio funciona
    return jsonify({"status": "activo"}), 200

# Endpoint 2: Metadata del servicio 
@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({
        "servicio": "backend-api",
        "version": "1.0.0",
        "descripcion": "API REST para TeamBoard App"
    }), 200

if __name__ == '__main__':
    # El servidor corre en el puerto 5000 
    app.run(host='0.0.0.0', port=5000)
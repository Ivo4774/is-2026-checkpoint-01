import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- FUNCIÓN PARA CONECTAR A LA BASE DE DATOS ---
def get_db_connection():
    # Usa DB_URL tal como la define el docker-compose.yml
    conn = psycopg2.connect(os.environ.get('DB_URL'))
    return conn

# --- ENDPOINTS ---

# Endpoint 1: Chequeo de salud
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "activo"}), 200

# Endpoint 2: Metadata del servicio
@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify({
        "servicio": "backend-api",
        "version": "1.0.0",
        "descripcion": "API REST para TeamBoard App"
    }), 200

# Endpoint 3: Lista de integrantes
@app.route('/api/team', methods=['GET'])
def get_team():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM members;')
        members = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(list(members)), 200
    except Exception as e:
        return jsonify({"error": "No se pudo conectar a la base de datos", "detalle": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
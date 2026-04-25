import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify

# Creo la aplicación Flask
app = Flask(__name__)

# --- FUNCIÓN PARA CONECTAR A LA BASE DE DATOS ---
def get_db_connection():
    # Usamos variables de entorno para no escribir contraseñas en el código
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        database=os.environ.get('DB_NAME', 'postgres'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'postgres'),
        port=os.environ.get('DB_PORT', '5432')
    )
    return conn

# --- ENDPOINTS ---

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

# Endpoint 3: Lista de integrantes 
@app.route('/api/team', methods=['GET'])
def get_team():
    try:
        conn = get_db_connection()
        # RealDictCursores hace que las claves coincidan con lo que pide el frontend
        cur = conn.cursor(cursor_factory=RealDictCursor) 
        
        cur.execute('SELECT * FROM members;')
        members = cur.fetchall()
        
        cur.close()
        conn.close()
        
        return jsonify(members), 200
        
    except Exception as e:
        return jsonify({"error": "No se pudo conectar a la base de datos", "detalle": str(e)}), 500
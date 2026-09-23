"""
Servicio de Consulta de Identificación
Endpoint para consultar datos básicos por número de identificación.
"""
from flask import Flask, jsonify, abort

app = Flask(__name__)

IDENTIFICACIONES = {
    12345: {"id": 12345, "nombre": "Juan Pérez", "existe": True},
    67890: {"id": 67890, "nombre": "María García", "existe": True},
    11111: {"id": 11111, "nombre": "Carlos López", "existe": True},
}


@app.route('/identificacion/<int:id>', methods=['GET'])
def get_identificacion(id):
    """
    Consulta si existe un número de identificación y devuelve sus datos básicos.
    
    Args:
        id: Número de identificación (entero)
    
    Returns:
        200: Datos del identificador si existe
        404: Indicador de no existencia si no se encuentra
    """
    if id in IDENTIFICACIONES:
        return jsonify(IDENTIFICACIONES[id]), 200
    return jsonify({"id": id, "existe": False}), 404


@app.route('/health', methods=['GET'])
def health():
    """
    Endpoint de verificación de salud del servicio.
    """
    return jsonify({
        "status": "healthy",
        "service": "identificacion-service",
        "version": "1.0.0"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

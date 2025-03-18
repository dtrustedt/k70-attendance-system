# backend/src/app/routes/device_routes.py
from flask import Blueprint, request, jsonify
from app.services.device_service import DeviceManager

device_bp = Blueprint('device', __name__, url_prefix='/api/device')

@device_bp.route('/connect', methods=['POST'])
def connect_device():
    data = request.json
    manager = DeviceManager(data['ip'])
    if manager.connect(data.get('password')):
        return jsonify({'status': 'connected'})
    return jsonify({'error': 'Connection failed'}), 400

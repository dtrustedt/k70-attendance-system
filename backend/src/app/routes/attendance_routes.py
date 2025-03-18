# backend/src/app/routes/attendance_routes.py
from flask import Blueprint, send_file
from app.services.device_service import DeviceManager

attendance_bp = Blueprint('attendance', __name__, url_prefix='/api/attendance')

@attendance_bp.route('/export/<ip>')
def export_attendance(ip):
    manager = DeviceManager(ip)
    attendance = manager.sync_attendance.delay(ip).get()
    
    # Generate CSV
    csv_data = "User ID,Name,Date,First,Last,VerifyMode\n"
    for record in attendance:
        csv_data += f"{record.user_id},{record.name},{record.timestamp},..."
    
    return send_file(
        io.BytesIO(csv_data.encode()),
        mimetype='text/csv',
        download_name='attendance.csv'
    )

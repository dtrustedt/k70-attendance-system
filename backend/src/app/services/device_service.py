from zk import ZK
from celery import shared_task

class DeviceManager:
    def __init__(self, ip, port=4370):
        self.ip = ip
        self.port = port
        self.conn = None
        
    def connect(self, password=None):
        zk = ZK(self.ip, port=self.port, timeout=10)
        self.conn = zk.connect()
        return self.conn
    
    @shared_task
    def sync_attendance(self, ip):
        """Background task to sync attendance records"""
        try:
            zk = ZK(ip)
            conn = zk.connect()
            attendance = conn.get_attendance()
            conn.disconnect()
            return attendance
        except Exception as e:
            raise self.retry(exc=e, countdown=30)

from threading import Thread
from modbusTCPServer import ModBusTCPServer


class AlarmTrigger(Thread):

    def __init__(self, mb_ip, mb_port):
        super(AlarmTrigger, self).__init__()
        self.modbus_server = ModBusTCPServer(host=mb_ip, port=mb_port)

    def send_detection_alarm(self):
        self.modbus_server.write_registers([0, 1], [1, 0])

    def send_intrusion_alarm(self):
        self.modbus_server.write_registers([0, 1], [0, 1])

    def run(self):
        self.modbus_server.serve()


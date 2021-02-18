from socketserver import TCPServer
from collections import defaultdict
from umodbus import conf
from umodbus.server.tcp import RequestHandler, get_server


class ModBusTCPServer:

    def __init__(self, host, port):
        self.data_store = defaultdict(int)
        self.host = host
        self.port = port
        conf.SIGNED_VALUES = True
        TCPServer.allow_reuse_address = True

        try:
            self.app = get_server(TCPServer, (host, port), RequestHandler)
        except PermissionError:
            print("Hint: try with a different port (ex: --bind localhost:50200)")

        @self.app.route(slave_ids=[1], function_codes=[1, 2], addresses=list(range(0, 10)))
        def read_data_callback(slave_id, function_code, address):
            """" Return value of address. """
            read_value = self.data_store[address]
            self.data_store[address] = 0
            return read_value

        @self.app.route(slave_ids=[1], function_codes=[5, 15], addresses=list(range(0, 10)))
        def write_data_callback(slave_id, function_code, address, value):
            """" Set value for address. """
            self.data_store[address] = value

    def write_registers(self, addresses, values):
        for address, value in zip(addresses, values):
            self.data_store[address] = value

    def serve(self):
        self.app.serve_forever()

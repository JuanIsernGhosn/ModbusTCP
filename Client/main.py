
#!/usr/bin/env python
# scripts/examples/simple_tcp_client.py
from argparse import ArgumentParser
from socket import create_connection

from umodbus import conf
from umodbus.client import tcp

# Enable values to be signed (default is False).
conf.SIGNED_VALUES = True

host = "localhost"
port = 502

# Returns a message or Application Data Unit (ADU) specific for doing
# Modbus TCP/IP.
message_w = tcp.write_multiple_coils(slave_id=1, starting_address=1, values=[1, 0, 1, 1])
message_r = tcp.read_discrete_inputs(1,0,4)

with create_connection((host, port)) as sock:
    # Response depends on Modbus function code. This particular returns the
    # amount of coils written, in this case it is.
    print(message_r)
    tcp.send_message(message_r, sock)

    #response = tcp.send_message(message_r, sock)
    #print(response)
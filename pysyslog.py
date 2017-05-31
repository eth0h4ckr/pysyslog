#!/usr/bin/env python

import argparse
import SocketServer
import logging

from threading import Thread

PORT = 514
HOST = ""
LOG_FILE = 'poop.log'

logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='', filename=LOG_FILE, filemode='a')

class MySocketServerHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = bytes.decode(self.request[0].strip())
        socket = self.request[1]
        print( "%s : " % self.client_address[0], str(data))
        logging.info(str(data))

def start_udp():
    print("Starting UDP Server at port %s " % PORT)

    try:
        server_s = SocketServer.UDPServer((HOST, PORT), MySocketServerHandler)
        server_s.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        pass
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")


def start_tcp():
    print("Starting TCP Server at port %s " % PORT)
    server_s = SocketServer.TCPServer((HOST, PORT), MySocketServerHandler)
    server_s.serve_forever(poll_interval=0.5)

    try:
        server_s = SocketServer.UDPServer((HOST, PORT), MySocketServerHandler)
        server_s.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit):
        pass
    except KeyboardInterrupt:
        print ("Crtl+C Pressed. Shutting down.")

if __name__ == "__main__":
    print "Starting server...."

    parser = argparse.ArgumentParser(description='Fake Ass Syslog Server')
    parser.add_argument('--tcp', help='Start TCP server', action='store_true', default=False, required=False)
    parser.add_argument('--udp', help='Start UDP server', action='store_true', default=False, required=False)
    parser.add_argument('--port', help='Port for servers', default=514, required=False)
    args = parser.parse_args()
    PORT = int(args.port)

    if args.udp:
       #t = Thread(target=start_udp)
       #t.start()
       start_udp();
    if args.tcp:
       #t2 = Thread(target=start_tcp)
       #t2.start()
       start_tcp();

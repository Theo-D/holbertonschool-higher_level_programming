#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class myServer(BaseHTTPRequestHandler):

    def do_GET(self):
        dataSet = {"name": "John", "age": 30, "city": "New York"}
        infoSet = {"version": "1.0", "description": "A simple API built with http.server"}
        endpointDict = {"/data" : dataSet, "/info" : infoSet, "/status" : "OK"}
        if self.path in endpointDict:
            print(json.dumps(endpointDict[self.path]))
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
        else:
            print("Endpoint Not Found")
            self.send_response(404)

        self.end_headers()


def run(server_class=HTTPServer, handler_class=myServer):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

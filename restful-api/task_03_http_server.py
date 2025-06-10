#!/usr/bin/python3
"""
task_03_http_server.py - A Module containing classes and functions to learn
about http.server python library
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class myServer(BaseHTTPRequestHandler):
    """
    myServer - A subclass of BaseHTTPRequestHandler to adapt its methods.
    """
    def do_GET(self):
        """
        do_GET - A method handling get responses from web server.
        """
        dataSet = {"name": "John", "age": 30, "city": "New York"}
        infoSet = {"version": "1.0", "description":
                   "A simple API built with http.server"}
        endpointDict = {"/data": dataSet, "/info": infoSet, "/status": "OK", "/": ""}
        if self.path in endpointDict:
            if len(endpointDict[self.path]) > 0:
                print(json.dumps(endpointDict[self.path]))
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
        else:
            print("Endpoint Not Found")
            self.send_response(404)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=myServer):
    """
    run - Function to run webserver and learn about http methods.
    """
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

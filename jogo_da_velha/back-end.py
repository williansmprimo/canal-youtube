# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from urllib.parse import urlparse, parse_qs
from jogo_da_velha_lib import *

hostName = "localhost"
serverPort = 8081

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET");
        self.end_headers()
        url=urlparse(self.path)
        query=parse_qs(url.query)
        state = query["state"]
        print(state)
        nextPosition, message = getNextState(state)
        response = {"nextPosition": nextPosition, "message": message}
        response = json.dumps(response)
        self.wfile.write(bytes(response, "utf-8"))
        #self.wfile.close()

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

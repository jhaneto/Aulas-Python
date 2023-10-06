from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(bytes(self.server.myArg, 'utf-8'))
        #...
        self.server.headers = self.headers

class MyHttpServer(HTTPServer):
    def __init__(self, server_address, myArg, handler_class=MyHttpRequestHandler):
        super().__init__(server_address, handler_class)
        self.myArg = myArg
        self.headers = dict()
        
        
    def get_header():
        httpd = MyHttpServer(("127.0.0.1", 8099), "MyFancyText", MyHttpRequestHandler)
        httpd.handle_request()
        return httpd.headers      

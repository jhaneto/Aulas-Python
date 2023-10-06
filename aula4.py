
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHendler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Context-Type", "text/html; charset=utf-8")
        self.send_header("Teste","ABC")
        self.end_headers()
        data = f"""
        <html>
            <head> Óla, Mundo! </head>
               <body>
                   <p>Testando nosso servidor HTTP!</p>
                   <p>Diretorio : {self.path}</p>
               </body>
        </html>
        """.encode()  
        
        self.wfile.write(data)    
        server = HTTPServer(("localhost", 8000), SimpleHendler)
        server.serve_forever()   
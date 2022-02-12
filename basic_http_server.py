import http.server, socketserver
print('open on port 8000')
socketserver.TCPServer(('', 8000), http.server.SimpleHTTPRequestHandler).serve_forever()

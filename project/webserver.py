from http.server import HTTPServer, BaseHTTPRequestHandler


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>Hello!</body></html>'
                self.wfile.write(bytes(output, 'utf8'))

                return
        except IOError:
            self.send_error(404, f'File Not Found {self.path}')


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print('Web server running on port', port)
        server.serve_forever()
    except KeyboardInterrupt:
        server.socket.close()


if __name__ == '__main__':
    main()
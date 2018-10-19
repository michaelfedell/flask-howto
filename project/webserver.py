import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, MenuItem, Restaurant

# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith('/hello'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>Hello!</body></html>'
                self.wfile.write(bytes(output, 'utf8'))
                return

            if self.path.endswith('/restaurants'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += '<h1>A Curated selection of restaurants both classy and trashy</h1>'
                for restaurant in session.query(Restaurant).all():
                    output += f'<strong>{restaurant.name}</strong><br>'
                    output += '<a href=#>Edit</a><br>'
                    output += '<a href=#>Delete</a><br>'
                    output += '<br>'
                output += '<br><a href="restaurants/new">Add a New Restaurant</a>'
                output += '</body></html>'
                self.wfile.write(bytes(output, 'utf8'))
                return

            if self.path.endswith('/restaurants/new'):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ''
                output += '<html><body>'
                output += '<h1>Add a new restaurant</h1>'
                output += '<form action="/restaurants/new" method="POST" enctype="multipart/form-data">'
                output += '<input type="text" placeholder="restaurant name" name="newRestaurantName"></input>'
                output += '<button type="submit">Add</button></form>'
                output += '</body></html>'
                self.wfile.write(bytes(output, 'utf8'))
                return

        except IOError:
            self.send_error(404, f'File Not Found {self.path}')

    def do_POST(self):
        try:
            if self.path.endswith('/restaurants/new'):
                ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                print(ctype, pdict)
                if ctype == 'multipart/form-data':
                    fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                newRestaurant = Restaurant(name=messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(201)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler


class CGIServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        response = """
                   <html>
                <head>
                    <title>Запись к врачу</title>
                </head>
                <body>
                    <h1>Запись к врачу</h1>
                    <form method="post">
                        <label for="name">Имя:</label>
                        <input type="text" id="name" name="name"><br><br>
                        <label for="surname">Фамилия:</label>
                        <input type="text" id="surname" name="surname"><br><br>
                        <label for="patronymic">Отчество:</label>
                        <input type="text" id="patronymic" name="patronymic"><br><br>
                        <label for="specialization">Специализация:</label>
                        <select id="specialization" name="specialization">
                            <option value="терапевт">Терапевт</option>
                            <option value="хирург">Хирург</option>
                            <option value="окулист">Окулист</option>
                            <option value="стоматолог">Стоматолог</option>
                        </select><br><br>
                        <input type="submit" value="Записаться">
                    </form>
                </body>
                </html>
            """
        self.wfile.write(response.encode('cp1251'))

server = HTTPServer
handler = CGIServer
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin", "/wsgi"]

httpd = server(server_address, handler)
httpd.serve_forever()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi


class CGIServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
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
                        <label for="sex">Пол:</label>
                        <select id="sex" name="sex">
                            <option value="М">Мужской</option>
                            <option value="Ж">Женский</option>
                        </select><br><br>
                        <label for="snils">Номер снилса:</label>
                        <input type="text" id="snils" name="snils" pattern="[0-9]{11}" title="Номер СНИЛСа должен состоять из 11 цифр" required><br><br>
                        <label for="polis">Номер полиса:</label>
                        <input type="text" id="polis" name="polis" pattern="[0-9]{11}" title="Номер полиса должен состоять из 11 цифр" required><br><br>
                        <label for="specialization">Специализация врача:</label>
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
        self.wfile.write(response.encode('utf-8'))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST',
                     'CONTENT_TYPE': self.headers['Content-Type'],
                     })
        name = form.getvalue("name")
        surname = form.getvalue("surname")
        patronymic = form.getvalue("patronymic")
        response = f"""
                    <html>
                    <head>
                        <title>Результат записи к врачу</title>
                    </head>
                    <body>
                        <h1>Результат записи к врачу</h1>
                        <p>Вы успешно записаны к врачу.</p>
                        <p>Пациент:</p>
                        <ul>
                            <li>Имя: {name}</li>
                            <li>Фамилия: {surname}</li>
                            <li>Отчество: {patronymic}</li>
                        </ul>
                        <p>Врач:</p>
                        <ul>
                            <li>Имя: {name}</li>
                            <li>Фамилия: {surname}</li>
                            <li>Отчество: {patronymic}</li>
                        </ul>
                        <button onclick="window.location.href = 'http://127.0.0.1:8000';">Ок</button>
                    </body>
                    </html>
                """
        self.wfile.write(response.encode('utf-8'))


server = HTTPServer
handler = CGIServer
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin", "/wsgi"]

httpd = server(server_address, handler)
httpd.serve_forever()
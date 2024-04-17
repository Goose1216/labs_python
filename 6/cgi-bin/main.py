#! /usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ
import cgitb
cgitb.enable()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Get Cookie</title>")
print("</head>")
print("<body>")

if 'HTTP_COOKIE' in environ:
    for cookie in environ['HTTP_COOKIE'].split(';'):
        (key, value) = cookie.split('=')
        print("%s: %s" % (key, value))
        print("<br/>")

print("</body>")
print("</html>")
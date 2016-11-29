# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle
from homepage import homepage

urls = (
    '/wx', 'Handle',
    '/','homepage',
)




if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

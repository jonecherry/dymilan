# -*- coding: utf-8 -*-
# filename: main.py
import web
from handle import Handle

urls = (
    '/wx', 'Handle',
    '/','homepage',
)


class homepage(object):
    def GET(self):
        return " 这里是米兰居家"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()

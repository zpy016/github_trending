#!/usr/bin/env python3
"""极简 HTTP 服务器，为 Coze 平台提供静态文件服务"""
import http.server
import socketserver
import os

PORT = 5000
DIR = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        # 精简日志
        pass

if __name__ == '__main__':
    os.chdir(DIR)
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        print(f"Serving {DIR} on 0.0.0.0:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

#!/usr/bin/env python3
"""
Simple HTTP server with CORS headers for serving IIIF content
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=CORSRequestHandler, port=8000):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting IIIF server on http://127.0.0.1:{port}/')
    print(f'Manifest available at: http://127.0.0.1:{port}/manifest.json')
    print('Press Ctrl+C to stop the server')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\nShutting down server...')
        httpd.shutdown()


if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    run(port=port)

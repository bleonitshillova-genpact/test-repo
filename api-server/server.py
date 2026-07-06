#!/usr/bin/env python3
"""
Simple API Server for Testing
Provides REST endpoints for Postman testing
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs


class TestAPIHandler(BaseHTTPRequestHandler):

    def _set_headers(self, status=200, content_type='application/json'):
        self.send_response(status)
        self.send_header('Content-Type', content_type)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/':
            self._set_headers()
            response = {
                'message': 'API Server is running',
                'timestamp': datetime.now().isoformat(),
                'endpoints': [
                    'GET /health',
                    'GET /users',
                    'GET /users?id=1',
                    'POST /users',
                    'GET /status'
                ]
            }
            self.wfile.write(json.dumps(response, indent=2).encode())

        elif path == '/health':
            self._set_headers()
            response = {
                'status': 'healthy',
                'timestamp': datetime.now().isoformat(),
                'uptime': 'active'
            }
            self.wfile.write(json.dumps(response, indent=2).encode())

        elif path == '/users':
            query_params = parse_qs(parsed_path.query)
            user_id = query_params.get('id', [None])[0]

            users = [
                {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'role': 'Admin'},
                {'id': 2, 'name': 'Bob', 'email': 'bob@example.com', 'role': 'User'},
                {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com', 'role': 'User'}
            ]

            if user_id:
                user = next((u for u in users if u['id'] == int(user_id)), None)
                if user:
                    self._set_headers()
                    self.wfile.write(json.dumps(user, indent=2).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write(json.dumps({'error': 'User not found'}).encode())
            else:
                self._set_headers()
                response = {
                    'count': len(users),
                    'users': users
                }
                self.wfile.write(json.dumps(response, indent=2).encode())

        elif path == '/status':
            self._set_headers()
            response = {
                'server': 'running',
                'database': 'connected',
                'api_version': '1.0',
                'timestamp': datetime.now().isoformat()
            }
            self.wfile.write(json.dumps(response, indent=2).encode())

        else:
            self._set_headers(404)
            response = {'error': 'Endpoint not found'}
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == '/users':
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data.decode())
                self._set_headers(201)
                response = {
                    'message': 'User created successfully',
                    'user': {
                        'id': 4,
                        **data
                    },
                    'timestamp': datetime.now().isoformat()
                }
                self.wfile.write(json.dumps(response, indent=2).encode())
            except json.JSONDecodeError:
                self._set_headers(400)
                response = {'error': 'Invalid JSON'}
                self.wfile.write(json.dumps(response).encode())
        else:
            self._set_headers(404)
            response = {'error': 'Endpoint not found'}
            self.wfile.write(json.dumps(response).encode())

    def log_message(self, format, *args):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {format % args}")


def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, TestAPIHandler)
    print("=" * 60)
    print(f"API Server running on http://localhost:{port}")
    print("=" * 60)
    print("\nAvailable endpoints:")
    print(f"  GET  http://localhost:{port}/")
    print(f"  GET  http://localhost:{port}/health")
    print(f"  GET  http://localhost:{port}/users")
    print(f"  GET  http://localhost:{port}/users?id=1")
    print(f"  POST http://localhost:{port}/users")
    print(f"  GET  http://localhost:{port}/status")
    print("\nPress Ctrl+C to stop the server")
    print("=" * 60 + "\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        httpd.shutdown()


if __name__ == '__main__':
    run_server()

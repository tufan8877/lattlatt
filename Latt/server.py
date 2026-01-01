#!/usr/bin/env python3
"""
Simple HTTP server for serving static HTML files.
Configured for Replit environment with proper cache control headers.
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


class NoCacheHTTPRequestHandler(SimpleHTTPRequestHandler):
    """HTTP request handler that disables caching for all responses."""
    
    def end_headers(self):
        """Add cache control headers to prevent browser caching."""
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Log requests to stdout."""
        print(f"{self.address_string()} - {format % args}")


def run_server(port=5000):
    """Start the HTTP server on the specified port."""
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, NoCacheHTTPRequestHandler)
    print(f"Server running on http://0.0.0.0:{port}")
    print(f"Serving files from: {os.getcwd()}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()

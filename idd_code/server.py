#!/usr/bin/env python
# https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/
# import code; code.interact(local=dict(globals(), **locals()))

from http.server import BaseHTTPRequestHandler, HTTPServer
import _thread


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        if self.path == '/get':
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            message = self.return_data_structure()

        elif self.path == '/':
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = open('flex.html').read()

        elif self.path == '/flex.css':
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            message = open('flex.css').read()

        else:
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = "Invalid path " + self.path

        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def return_data_structure(self):
        import key_entry
        import json
        return json.dumps(key_entry.all_info, indent=4, sort_keys=True)
        # import code; code.interact(local=dict(globals(), **locals()))
        # return "soemthing"

    def log_message(self, fmt, *args):
        pass


def run_server():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 1234)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')


def run_arduino():
    print("Listening to arduino...")
    import key_entry
    key_entry.listen()


# http://www.tutorialspoint.com/python3/python_multithreading.htm
# _thread.start_new_thread( run_server, ("Thread-1", 2, ) )
_thread.start_new_thread( run_arduino, () )

run_server()

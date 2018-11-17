from threading import Thread

from core.RequestHandler import RequestHandler


class ThreadHandler(Thread):

    def __init__(self, socket, document_root):
        Thread.__init__(self)
        self.socket = socket
        self.document_root = document_root

    def run(self):
        while True:
            self.connection_loop()

    def connection_loop(self):
        conn, adr = self.socket.accept()
        request = conn.recv(2048)

        if len(request.strip()) == 0:
            conn.close()
            return

        conn.sendall(RequestHandler(request, self.document_root).get_response())
        conn.close()


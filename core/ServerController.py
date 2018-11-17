import socket

from core.ThreadHandler import ThreadHandler


class ServerController:
    def __init__(self, port, thread_count, document_root):

        self.port = int(port)
        self.thread_count = int(thread_count)
        self.document_root = document_root

        self.threads = []

    def run(self):
        tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcp_server.bind(('0.0.0.0', self.port))
        tcp_server.listen(self.thread_count)

        for i in range(0, self.thread_count):
            print('created thread', i)
            thread = ThreadHandler(tcp_server, self.document_root)
            self.threads.append(thread)
            thread.start()

        for i in range(0, self.thread_count):
            self.threads[i].join()


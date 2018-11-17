import socket

import sys

from core.ThreadHandler import ThreadHandler


class ServerController:
    def __init__(self, port, thread_count, document_root):

        self.port = int(port)
        self.thread_count = int(thread_count)
        self.document_root = document_root

        self.threads = []

    def get_step_function(self, i):
        def step(index):
            return i + self.thread_count*index
        return step

    def run(self):
        # stepper = self.get_step_function(0)
        # stepper2 = self.get_step_function(1)

        tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        tcpServer.bind(('0.0.0.0', self.port))
        tcpServer.listen(self.thread_count)

        for i in range(0, self.thread_count):
            print('spawning thread', i)
            thread = ThreadHandler(tcpServer, self.document_root)
            self.threads.append(thread)
            thread.start()

        for i in range(0, self.thread_count):
            self.threads[i].join()


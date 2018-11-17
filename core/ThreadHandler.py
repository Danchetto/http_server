import queue
# import socket
from threading import Thread

# import select

from core.RequestHandler import RequestHandler


class ThreadHandler(Thread):

    inputs = []
    outputs = []

    message_queues = {}

    def __init__(self, socket, document_root):
        Thread.__init__(self)
        self.socket = socket
        self.document_root = document_root
        self.inputs.append(self.socket)
        # self.step_function = step_function

    def run(self):
        while True:
            self.connection_loop()
            # self.connection_loop_select()
            # try:
            #     self.connection_loop_select()
            # except socket.error:
            #     self.inputs = []
            # except TypeError:
            #     self.inputs = []

    # def connection_loop_select(self):
    #     readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)
    #
    #     for s in readable:
    #         if s is self.socket:
    #             connection, client = s.accept()
    #             connection.setblocking(False)
    #             self.inputs.append(connection)
    #             self.message_queues[connection] = queue.Queue()
    #         else:
    #             data = s.recv(1024)
    #             if data:
    #                 self.message_queues[s].put(RequestHandler(data, self.document_root).get_response())
    #                 if s not in self.outputs:
    #                     self.outputs.append(s)
    #                 self.inputs.remove(s)
    #             else:
    #                 if s in self.outputs:
    #                     self.outputs.remove(s)
    #                 s.close()
    #                 del self.message_queues[s]
    #
    #     for s in writable:
    #         try:
    #             next_msg = self.message_queues[s].get_nowait()
    #         except queue.Empty:
    #             self.outputs.remove(s)
    #         else:
    #             s.send(next_msg)
    #             s.close()
    #             self.outputs.remove(s)
    #
    #     for s in exceptional:
    #         self.inputs.remove(s)
    #         if s in self.outputs:
    #             self.outputs.remove(s)
    #         s.close()
    #         del self.message_queues[s]

    def connection_loop(self):
        conn, adr = self.socket.accept()
        request = conn.recv(1024)

        if len(request.strip()) == 0:
            conn.close()
            return
        conn.sendall(RequestHandler(request, self.document_root).get_response().encode())
        conn.close()



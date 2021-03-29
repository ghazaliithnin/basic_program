import socket


class SocketServer:
    def __init__(self, port=8080,max_clients=1,buffer_size=1024, reader=None, second_reader=None):
        # super().__init__()
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.port = port
        self.max_clients = max_clients
        self.buffer_size = buffer_size

        if reader is None:
            self.buffer = []
        else:
            self.buffer = reader

        if second_reader is None:
            self.cmd_buffer = []
        else:
            self.cmd_buffer = second_reader

    def run(self):
        self.client_sock.bind(("", self.port))
        while True:
            try:
                # data = self.client_sock.recv(self.buffer_size)
                data, address = self.client_sock.recvfrom(self.buffer_size)
                self.mprint(address)
                # self.buffer.append(data.decode("utf8"))
                mData = data.decode("utf-8")
                mData = mData.strip()
                if mData == "kill":
                    self.buffer.append(mData)
                    self.stop()
                    break
                elif mData[0:3] == "cmd":
                    self.cmd_buffer.clear()
                    cmd = mData.split(",")
                    self.cmd_buffer.extend(cmd)
                else:
                    self.buffer.append(mData)
                self.mprint(self.buffer)
            except Exception as e:
                print(e)
                break
            # self.stop()

    def stop(self):
        self.client_sock.close()

    @classmethod
    def mprint(cls,mstring):
        print(mstring)
        pass
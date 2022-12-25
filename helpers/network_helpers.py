import socket
from contextlib import closing

def is_port_open(host: str, port: int, debug=False):
    # popen('lsof -i -n -P | grep "TCP .*:4723"').readlines() #This would be perhaps a mac only solution
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        is_open = sock.connect_ex((host, port)) == 0
        if debug:
            if is_open:
                print("Port is open")
            else:
                print("Port is not open")
        else:
            return is_open

if __name__ == '__main__':
    is_port_open("0.0.0.0", 4723, debug=True)

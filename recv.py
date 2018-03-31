import socket
import requests
import binascii


def recv():
    HOST = '127.0.0.1'
    PORT = 8001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print('Server start at: %s:%s' % (HOST, PORT))
    print('wait for connection...')

    while True:
        try:
            conn, addr = s.accept()
            connect = 'Connected by %s:%s' % (addr[0], addr[1])
            ip_port = '%s:%s' % (addr[0], addr[1])
            print(connect)
            while True:
                try:
                    data = conn.recv(1024)
                    if data:
                        post(binascii.b2a_hex(data), ip_port)
                        print(binascii.b2a_hex(data))
                    conn.send(binascii.b2a_hex(data))
                except Exception as e:
                    print(e)
                    #post('%s:%s disconnect' % (addr[0], addr[1]))
                    break
        except Exception as e:
            print(e)
            #post('%s:%s disconnect' % (addr[0], addr[1]))
        finally:
            conn.close()

def post(message, connect):
    post_data = {
        'data': message,
        'connect': connect
    }
    requests.post('http://127.0.0.1:5000/recv', data=post_data)

if __name__ == '__main__':
    recv()


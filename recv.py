import socket
import requests

def recv():
    HOST = '127.0.0.1'
    PORT = 8001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print('Server start at: %s:%s' % (HOST, PORT))
    print('wait for connection...')

    while True:
        conn, addr = s.accept()
        connect = 'Connected by %s:%s' % (addr[0], addr[1])
        print(connect)
        post(connect)
        while True:
            try:
                data = conn.recv(1024)
                if data:
                    post(data)
                    print(data, type(data))
                conn.send("server received you message.".encode('utf8'))
            except Exception as e:
                post('%s:%s disconnect' % (addr[0], addr[1]))
                break
        #conn.close()

def post(message):
    post_data = {
        'data': message
    }
    requests.post('http://127.0.0.1:5000/send', data=post_data)

if __name__ == '__main__':
    recv()
    
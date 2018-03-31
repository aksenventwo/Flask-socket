
from flask import Flask, render_template, request, jsonify, g
from flask_socketio import SocketIO
from flask_socketio import emit
import socket

app = Flask(__name__)
socketio = SocketIO()
socketio.init_app(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/connect', methods=['POST'])
def connect():
    ip = request.form.get('ip', '')
    port = request.form.get('port', '')
    if not ip or not port:
        return jsonify({'success': False, "err_msg": "Ip or Port can't be empty."})
    try:
        recv = sc_connect(ip, port)
        #socketio.emit('message', {'msg': recv})
    except Exception as e:
        return jsonify({'success': False, "err_msg": str(e)})
    return jsonify({'success': True})


@app.route('/send', methods=['POST'])
def send():
    data = request.form.get('data')
    ip = request.form.get('ip')
    port = request.form.get('port')
    recv = sc_connect(ip, port, data)
    #socketio.emit('message', {'msg': recv})
    return jsonify({'data': data})

@app.route('/recv', methods=['POST'])
def recv():
    data = request.form.get('data')
    socketio.emit('message', {'msg': data})
    return jsonify({'data': data})

def sc_connect(ip, port, data="Hello World"):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.connect((ip, int(port)))
    except socket.error as e:
        raise TcpConnectError(e)
    else:
        server.send(data)
        accept_data = server.recv(1024)
    finally:
        server.close()
    return accept_data


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')

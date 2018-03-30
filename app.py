
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from flask_socketio import emit

app = Flask(__name__)
socketio = SocketIO()
socketio.init_app(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
	data = request.form.get('data')
	socketio.emit('message', {'msg': data})
	return jsonify({'data': data})



if __name__ == '__main__':
	socketio.run(app, host='0.0.0.0')

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
	data = request.form.get('data')
	return jsonify({'data': data})


if __name__ == '__main__':
	app.run()
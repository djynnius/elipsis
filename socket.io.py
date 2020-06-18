from flask import Flask, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from flask_cors import CORS
import json, requests

app = Flask(__name__)

app.config['SECRET_KEY'] = 'elipsis_secret!'
socketio = SocketIO(app, cors_allowed_origins="*", SameSite=None)

'''Receiving from clients'''
@socketio.on('info', namespace='/connected')
def handle_message(info):
	join_room('connected')
	emit('connect', 'your sid is {}'.format(request.sid))

@app.route('/foo')
def foo():
	emit('name', 'message', namespace='/connected', room='connected')
	return ''

if __name__ == '__main__':
    socketio.run(app, port=9000, host='0.0.0.0', debug=True)

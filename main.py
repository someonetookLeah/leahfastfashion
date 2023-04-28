
from app import app
import os

if __name__ == "__main__":
    
    os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
    
    # app.run(debug="True", ssl_context='adhoc')
    app.run(debug="True",use_reloader=True, ssl_context=('cert.pem', 'key.pem'))


    
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static/')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('feedback.html')

@socketio.on('client_message')
def receive_message (client_msg):
    emit('server_message', client_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/static/')
socketio = SocketIO(app)
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from threading import Thread
from main import AssistantMain
import time

"""

[ UNDER CONSTRUCTION ]

"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

assistant_status = 'sleep'

@app.route('/')
def index():
    return render_template('index.html')

def background_thread():
    global assistant_status
    while True:
        socketio.emit('status_update', {'status': assistant_status}, namespace='/')
        time.sleep(1)

@socketio.on('connect')
def handle_connect():
    emit('status_update', {'status': assistant_status}, namespace='/')

def run_assistant():
    assistant = AssistantMain(socketio)
    assistant.main()

if __name__ == '__main__':
    thread = Thread(target=background_thread)
    thread.start()

    assistant_thread = Thread(target=run_assistant)
    assistant_thread.start()

    socketio.run(app, debug=True, use_reloader=False)

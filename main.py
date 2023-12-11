from datetime import datetime

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '''
    <h1>Welcome to my first API!</h1>
    <p><a href="/time"><button>Get Current Time</button></a></p>'''


@app.route('/time')
def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%m-%d-%Y %H:%M-%S")
    return f'''
    <h1>Current Time: {current_time}</h1>
    <p><a href="/"><button>Return</button></a></p>'''


if __name__ == '__main__':
    app.run(debug=True)

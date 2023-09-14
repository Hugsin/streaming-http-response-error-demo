import os
import flask
import openai
import time
from flask import Flask

openai.api_key = os.environ.get('OPENAI_API_KEY')
app = Flask(__name__)


@app.route('/completions', methods=['GET','POST'])
def completion_api():
    def stream():
        for line in range(10):
            yield f'data:{line} \n\n'
            time.sleep(0.2)
    return flask.Response(stream(), mimetype='text/event-stream')

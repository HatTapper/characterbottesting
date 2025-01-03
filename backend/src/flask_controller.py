# this file handles the medium between the front-end and back-end of the program

from flask import Flask, render_template, request
from backend.src.bot_controller import get_response

app = Flask(__name__)


@app.route('/profile', methods=['GET'])
def profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }

    return response_body

@app.route('/post', methods=['POST'])
def post():
    user_input = request.form.get("prompt")
    ai_response = get_response(user_input)
    return ai_response

if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
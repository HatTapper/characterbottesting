# this file handles the medium between the front-end and back-end of the program
from http import HTTPStatus

from flask import Flask, render_template, request
from httpcore import Response

from backend.src.bot_controller import get_response, choose_character

app = Flask(__name__)

@app.route('/post', methods=['POST'])
def post():
    user_input = request.form.get("prompt")
    ai_response = get_response(user_input)
    return ai_response

@app.route("/bondrewd", methods=["GET"])
def select_bondrewd():
    choose_character("Bondrewd")
    return ' ', 200

@app.route("/ainz", methods=["GET"])
def select_ainz():
    choose_character("Ainz")
    return ' ', 200

if __name__ == "__main__":
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
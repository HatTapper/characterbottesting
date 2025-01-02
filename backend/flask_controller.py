from flask import Flask, render_template, request
from bot_controller import get_response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # not sure why this warns
    return render_template("main.html")

@app.route('/post', methods=['POST'])
def post():
    user_input = request.form.get("prompt")
    ai_response = get_response(user_input)
    return ai_response

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
app = Flask(__name__)

@app.route("/") # Revisit decorators if you unclear of this syntax
def index():
    return '<h1>Why so easy</h1>'

@app.route('/user/<username>')
def show(username):
    return f"Hi {username[0:3]}"

if __name__ == '__main__':
    app.run()
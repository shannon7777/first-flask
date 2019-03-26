from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<name>") # Revisit decorators if you unclear of this syntax
def index(name):
    # first_name = first_name.upper()
    # last_name = last_name.upper()
    name = name.upper()
    # first_name = "shannon"
    # last_name = "cherry"
    # num1 = '10'
    # num2 = '5'
    return render_template('index.html', n = name)

@app.route('/user/<username>')
def show(username):
    return f"Hi {username[5]}"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)


# using just before the function. Connect the function with path.
@app.route('/')
def hello():
    return render_template("index.html", number1=12)


@app.route('/second')
def second():
    return render_template("new.html")


if __name__ == "__main__":
    # show the mistakes while working
    app.run('localhost', port=5000, debug=True)

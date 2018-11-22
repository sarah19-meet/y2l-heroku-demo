from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def new_app():
    return render_template("edits.html")

if __name__ == '__main__':
    app.run(debug=True)



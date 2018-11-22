from flask import Flask
app = Flask(__name__)

@app.route('/edits')
def hello_world():
    return render_template("edits.html")

if __name__ == '__main__':
    app.run(debug=True)


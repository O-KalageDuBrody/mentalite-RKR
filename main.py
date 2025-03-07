from flask import Flask, render_template
app = Flask("main")
@app.route("/")
def hello():
    return render_template('hello.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
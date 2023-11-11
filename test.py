from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World! Is a good day right?"

if __name__ == "__main__":
    app.run(port=6318)
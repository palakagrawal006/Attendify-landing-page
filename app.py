from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__' : #run only when explicitly run on terminal
    app.run(debug =True , port=5002)
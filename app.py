from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Manoj. This is from AWS...!'

if __name__ == '__main__':
    app.run()

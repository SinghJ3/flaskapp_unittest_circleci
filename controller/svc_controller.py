from flask import Flask

app = Flask(__name__)

@app.route('/home', methods = ['GET'])
def index():
    return 'Success from Flask app'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
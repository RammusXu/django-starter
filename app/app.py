from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/login', methods=['POST'])
@app.route("/")
def hello():
    app.logger.debug('A value for debugging')

    json = {
        "txt": "Hellsso World!"
    }
    return jsonify(json), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

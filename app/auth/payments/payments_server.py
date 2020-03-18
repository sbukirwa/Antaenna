from flask import Flask, request
import json
app = Flask(__name__)


@app.route('/pay', methods=['GET', 'POST'])
def payments():
    if request.method == 'POST':
        print(request.get_json()['status'])
        return request.args
    elif request.method == 'GET':
        return "The server is running"
python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)

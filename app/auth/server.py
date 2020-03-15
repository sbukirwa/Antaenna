from flask import Flask, request


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def get_content():
    if request.method == 'POST':
        result = request.get_json(force=True)
        return result
    elif request.method == 'GET':
        result = "Hey There Man!"
        return result
    else:
        result = request.error()
        return result
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)
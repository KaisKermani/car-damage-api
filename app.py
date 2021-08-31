from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return {'msg': 'hello world'}


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('file_uploader.html')
    if request.method == 'POST':
        return request.args
        

if __name__ == '__main__':
    app.run()

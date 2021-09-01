from flask import Flask, render_template, request, redirect, Response
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    filenames = [file.filename for file in request.files.getlist('images')]
    print(filenames)
    resp = request.form.get('response')
    if resp == "HTML":
        return render_template('index.html', filenames=filenames)
    elif resp == "JSON":
        return Response(json.dumps(filenames, indent=2),  mimetype='application/json')


if __name__ == '__main__':
    app.run()

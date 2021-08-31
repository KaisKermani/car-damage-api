from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    filenames = [file.filename for file in request.files.getlist('images')]
    print(filenames)
    return render_template('index.html', filenames=filenames)
        

if __name__ == '__main__':
    app.run()

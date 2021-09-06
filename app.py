from flask import Flask, render_template, request, redirect, Response
from PIL import Image
import tensorflow as tf
from estimate_damage import load_images, predict

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def recieve_images():
    filenames = [file.filename for file in request.files.getlist('images')]
    if len(filenames) == 1 and filenames[0] == '':
        filenames = []
        return render_template('index.html', no_file=True)
    
    images = []
    for file in request.files.getlist('images'):
        images.append(Image.open(file.stream))
    
    images = load_images(images, im_h, im_w)
    pred_df = predict(models, images, labels, filenames)
    
    resp = request.form.get('response')
    if resp == "HTML":
        # test_dict = [{'om': 1.0, 'bou': 2.0, 'khuo': 3.0}, {'om': 4.0, 'bou': 5.0, 'khuo': 6.5}]
        # return render_template('index.html', preds=test_dict)
        return render_template('index.html', preds=pred_df.to_dict(orient='records'))
    elif resp == "JSON":
        return Response(pred_df.to_json(orient='records', indent=2), mimetype='application/json')


if __name__ == '__main__':
    print('Initializing app!')
    model_dirs = [
        'tf_models/bumper_damage',
        'tf_models/body_damage',
        'tf_models/door_damage',
        'tf_models/glass_lamp_damage',
        'tf_models/tire_mirror_damage',
        # 'tf_models/classifier',
    ]

    labels = [
        'Bumper_minor',
        'Bumper_severe',
        'Body_minor',
        'Body_severe',
        'Door_minor',
        'Door_severe',
        'Glass',
        'Lamp',
        'Tire',
        'Mirror',
        # 'Class'
    ]

    im_h = im_w = 299

    tf.config.set_visible_devices([], 'GPU')
    
    print('Loading TF Models:')
    models = []
    for path in model_dirs:
        models.append(tf.keras.models.load_model(path))
        print('Loaded model from', path)
    
    app.run(debug=False, host='192.168.100.6', port=5000, )

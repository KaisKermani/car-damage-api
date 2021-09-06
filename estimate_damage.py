import tensorflow as tf
import numpy as np
import PIL
import pandas as pd


def load_images(files, im_h, im_w):
    imgs = []
    for file in files:
        if type(file) == str:
            img = tf.io.decode_jpeg(tf.io.read_file(file), channels=3)
        elif type(file) == PIL.JpegImagePlugin.JpegImageFile:
            img = tf.keras.preprocessing.image.img_to_array(file)
        elif type(file) == PIL.PngImagePlugin.PngImageFile:
            img = tf.keras.preprocessing.image.img_to_array(file)
            if img.shape[2] == 4:
                img = img[:, :, :3]
            
        img = tf.image.resize(img, [im_h, im_w])
        imgs.append(np.array([img]))
    
    return np.concatenate(imgs)


def predict(tf_models: list, x, labels: list, img_names: list):
    assert len(img_names) == x.shape[0], \
        'image names (' + str(len(img_names)) + ') and input rows (' + str(x.shape[0]) + ') do not match!'
    pred = []
    for model in tf_models:
        pred.append(model.predict(x))
    pred = np.concatenate(pred, axis=1)
    assert pred.shape[1] == len(labels), \
        'feature labels (' + str(len(labels)) + ') and prediction features (' + str(pred.shape[1]) + ') do not match!'
    
    result = []
    for i, row, in enumerate(pred):
        res = {'image': img_names[i]}
        for j, cell in enumerate(row):
            res[labels[j]] = cell
        result.append(res)
    
    return pd.DataFrame.from_dict(result)


if __name__ == '__main__':
    
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
    img_paths = [
        'data/coco_1.jpg',
        'data/coco_6.jpg',
        'data/coco_7.jpg',
        'data/coco_8.jpg',
        'data/coco_9.jpg',
        'data/coco_10.jpg',
        'data/coco_16.jpg',
    ]
    im_h = im_w = 299
    
    tf.config.set_visible_devices([], 'GPU')
    
    models = []
    for path in model_dirs:
        with tf.device('/cpu:0'):
            models.append(tf.keras.models.load_model(path))
        print('Loaded model from', path)
    
    x = load_images(img_paths, im_h, im_w)
    predictions = predict(models, x, labels, img_paths)
    print(predictions)

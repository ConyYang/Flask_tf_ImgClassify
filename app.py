from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap

import os
import inference

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file.filename != '':
            image_path = os.path.join('static', upload_file.filename)
            upload_file.save(image_path)

            predict_result = inference.get_prediction(image_path)
            predict_score = predict_result[0]
            class_name = predict_result[1]
            result ={
                'predict_score': predict_score,
                'class_name': class_name,
                'image_path': image_path,
            }
            return render_template('show.html', result=result)

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
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

            result =  inference.get_prediction(image_path)
            predict_score = result[0]
            class_name = result[1]
            print('The predict score is: ', predict_score)
            print('We predict it is a: ', class_name)

    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
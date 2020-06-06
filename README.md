# Flask_tf_ImgClassify

### Intro
This is a simple web app to classify cat and dog

### Mechanism
- We serve a TensorFlow model with TensorFlow serving and Docker.
- We create a minimal flask application to create an interface to the served model.

### Start Tensorflow Server using Docker
```console
foo@bar:~$ pwd
foo
```
```console
foo@bar:~$ sudo docker ps
foo
```
```console
foo@bar:~$ sudo docker run -p 8501:8501 --name==pets -v "../../../PetApp/pets/:/models/pets/1"
-e MODEL_NAME=pets tensorflow/serving
foo
```
### Demo
```console
foo@bar:~$ python run app.py
foo
```

Main Page:
You can upload your own image here. The image will also be written to static file.
![Main Page](assets/mainPage.png)

Result Page:
You can see the prediction result, telling you whether it's a dog or cat.
You can also see the predicted score.
Click back to main to go back.
![ClassifyPage](assets/classifyPage.png)


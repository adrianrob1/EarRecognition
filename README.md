# Ear Detection and Verification with pre-trained CNN models

This repository contains the project files for the Biometric Systems exam in the Master's Degree in Computer Science at Sapienza University, made by [@adrianrob1](https://github.com/adrianrob1) and [@AntonioDOrazio](https://github.com/AntonioDOrazio).

## Ear detection

For ear detection we used [YoloV5](https://github.com/ultralytics/yolov5). We took the pretrained nano model and finetuned it for ear detection using the [UBEAR](http://ubear.di.ubi.pt/ubear.html) dataset after labelling the left and right ears in the yolo format.

## Ear verification

For verification we used [MobileNetV3](https://www.tensorflow.org/api_docs/python/tf/keras/applications/MobileNetV3Large). We started with the large model trained on ImageNet, then finetuned the model on [AWE](http://awe.fri.uni-lj.si/datasets.html) and then on [EarVN](https://data.mendeley.com/datasets/yws3v3mwx3/3). After finetuning, we removed the classifier level at the top and used the model for feature extraction.

## Android App

We also implemented the two models in an Android app. 
Initially, the user can enroll by taking 3 pictures of the ear, then we perform ear detection and segmention so that the user can have some feedback on the pictures taken. When they click on the save button, we extract the features and save the templates.
In the verification step they only need to frame the ear. We also implemented a software motion detector, so that we only pass frames to the models when the camera is stable. This allows the app to run smoothly when the user is moving the phone to show their ear using the front facing camera. After performing the detection, we segment the ear and pass it to the feature extraction model, then the app uses the output to compute a similarity score with the saved templates and takes the best score to make a decision based on the threshold. In the verification step the app doesn't require any other input from the user. When matching is performed we give feedback through a vibration and by showing the result on the screen.

More details can be found in the report and the Jupyter notebooks.

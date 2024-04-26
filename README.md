# Weather Image Recognition

This project aims to classify weather conditions from images using machine learning techniques. The model achieves an accuracy of 95% on the test dataset.

## Overview

Weather Image Recognition utilizes machine learning algorithms to classify weather conditions based on input images. With a diverse dataset covering various weather phenomena, the model accurately predicts the weather depicted in the images.

## Dataset

The dataset consists of images representing different weather conditions. Each image is labeled with one of the following classes:

- 0: dew
- 1: fog/smog
- 2: frost
- 3: glaze
- 4: hail
- 5: lightning
- 6: rain
- 7: rainbow
- 8: rime
- 9: sandstorm
- 10: snow

## Model Performance

The model deployed achieved a test accuracy of 95%, demonstrating its effectiveness in classifying weather conditions from images. The classification performance was evaluated using standard metrics such as accuracy, precision, recall, and F1-score.

## Deployment

The model is deployed using a Flask web application, providing a user-friendly interface for weather classification. Users can upload images, and the application will predict the corresponding weather condition.

### Instructions for Deployment:

1. Install Flask and other necessary dependencies.
2. Clone this repository.
3. Run the Flask application locally or deploy it on a web server.

## Future Improvements

Future enhancements for this project may include:

- Fine-tuning the model architecture to improve accuracy further.
- Adding support for real-time weather detection using live camera feeds.
- Incorporating user feedback to refine the model's predictions.


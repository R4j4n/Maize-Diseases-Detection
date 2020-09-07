[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)<br>
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)<br>
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

# CropDiseaseDiag
This is a complete webapp that uses Flask microframework for plant disease detection.
This repository aims to detect diseases that occur on the maize plants using Convolutional Neural Network and Transfer Learning. Currently, the model is able to predict major 3 diseases that occur on the leaves of the plant which are Corn grey leaf spot, Northern corn leaf blight, and Common Rust. The model is also able to predict healthily plant also.<br>

## Traning
Here we use a pre-trained VGG16 network for our disease classification problem. Then this pre-trained VGG16 was trained on our custom dataset. Our dataset mainly consists the images from [PlantVillage Dataset](https://www.kaggle.com/emmarex/plantdisease). Additional images were scraped from google and manual preprocessing was applied to it before adding it to the original dataset.

# Demo 
Here are some demo images of the project.
<img src= "PROJECT_IMG\IMG_6134.JPG"> 


<img src= "PROJECT_IMG\IMG_6135.JPG">
<img src= "PROJECT_IMG\IMG_6136.JPG">

## Compatibility 
This code was developed on : 
```
tensorflow==2.0.0
numpy==1.18.2
Flask==1.1.2
Pillow==7.1.1
```
 ![visitors](https://visitor-badge.glitch.me/badge?page_id=page.https://github.com/R4j4n/Maize-Diseases-Detection)
# car-damage-api  
## Introduction:
This project aims to help estimate the damage done to a car after an accident.
This API leverages state of the art deep learning models in order to assess the damage done to a car and its intensity from images of the damaged vehicule.  
   
## Demo:
![Alt text](Demo.gif?raw=true "Display")

## Dataset:
In this project I combined images from different datasets to come to a larger and more diverse dataset:
Pletarion dataset: https://peltarion.com/knowledge-center/documentation/terms/dataset-licenses/car-damage
Open Data Commons Attribution License dataset;
Coco Dataset

## Data Labeling:
The different datatsets were labelled differently, so I had to integrate a data labeling step, so I developed a small desktop GUI to speed up the labeling process:
![Alt text](labeling_app.png?raw=true "Display")

## Model architectures:
During the training process I used a pre-trained xception architecture and adapted it to our particular use-case.
Added to it a data augumentation layer and droupout layers for regularization (as well as L2 regularization). 

## Scores and metrics:
The metrics used in the validation step are accuracy and f1-score:

| Class         | Accuracy | F1-Score |
|---------------|----------|----------|
| Bumper_minor  | 90       | 88       |
| Bumper_severe | 89       | 85       |
| Door_minor    | 99       | 98       |
| Door_severe   | 99       | 97       |
| Body_minor    | 79       | 81       |
| Body_severe   | 85       | 75       |
| Glass_shatter | 94       | 81       |
| Lamp          | 85       | 75       |
| Tire          | 94       | 35       |
| Mirror        | 96       | 36       |


## Full project report:
Detailed walkthrough the different steps and processes of the project:
https://colab.research.google.com/drive/1kGv-hCy6PUIVtjOVNMZNmDtQLvk0Gssd?usp=sharing

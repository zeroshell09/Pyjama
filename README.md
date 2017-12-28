# Pyjama
The point of this project is to experiment both linear and polynomial interpolation. we want to reconstruct missing data from a subset data. 

The whole project will be deployed as an azure machine learning solution using following component:

 - Azure IOt Hub to push data from Virtual sensors into the pipeline
 - Azure Time Series to visualize reconstructed data in real time
 - Azure Model Management to deploy new ML model


![](https://github.com/zeroshell09/Pyjama/blob/master/eda/missing-data_viz.png)

All expected Data signal Vs Altered Signal


![](https://github.com/zeroshell09/Pyjama/blob/master/eda/degree2_underfitting.png)

Example of underfitting interpolator


![](https://github.com/zeroshell09/Pyjama/blob/master/eda/degree7_overfitting.png)

Example of overfitting interpolator


![](https://github.com/zeroshell09/Pyjama/blob/master/eda/degree4.png)
Polynomial features of degree 4
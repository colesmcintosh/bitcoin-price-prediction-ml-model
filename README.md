# Bitcoin Price Prediction Machine Learning Model

## About the model

>Using the Yahoo Finance API to download historical data for the Bitcoin-USD pair. I then use the scikit-learn library to split the data into a training set and a test set. 

>We train a random forest regression model on the training data. The model is then used to make predictions on the test data. The predictions are then compared to the actual values to calculate the accuracy of the model. 

>We use the trained model to make predictions for the Bitcoin-USD pair. The predictions are then displayed.

>The first model (ml_6_features.py) uses 6 different features ('Month', 'Year', 'Open', 'High', 'Low', 'Volume') whereas the second model (ml_2_features.py) uses only 2 features ('Month', 'Year') to make predications on the 'Closing' value.

<br>
<br>

## Accuracy of the model and images.

>Based upon testing for model #1 (ml_6_features.py), this model has an accuracy of about 99%.
<img alt="ml-model-1" src="sample_images\ml_6_f.PNG" height="auto" width="auto">

<br>

>Based upon testing for model #2 (ml_2_features.py), this model has an accuracy of about 97%.
<img alt="ml-model-2" src="sample_images\ml_2_f.PNG" height="auto" width="auto">
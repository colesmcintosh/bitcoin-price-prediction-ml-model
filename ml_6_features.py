import yfinance as yf
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#get data
df = yf.download('BTC-USD', start='2017-01-01', end='2028-01-01')

#transform data
df['Date'] = pd.to_datetime(df.index)
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

#split into training and test
train, test = train_test_split(df, test_size=0.2)

#create and train model
model = LinearRegression()
x_train = train[['Month', 'Year', 'Open', 'High', 'Low', 'Volume']]
y_train = train['Close']
model.fit(x_train, y_train)

#make predictions
x_test = test[['Month', 'Year', 'Open', 'High', 'Low', 'Volume']]
predictions = model.predict(x_test)

#transform predictions
predictions = pd.DataFrame(predictions, index=x_test.index, columns=['Predicted Close'])

#join predictions to actual values
results = pd.concat([test, predictions], axis=1)

#print results
print(results.round(2))

accuracy = r2_score(test['Close'], predictions)
accuracy = accuracy * 100
print("Accuracy: {:.2f}%".format(accuracy))


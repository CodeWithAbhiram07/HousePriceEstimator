import pandas as pd
from sklearn.linear_model import LinearRegression

def load_and_train_model(data_path='data/USA_Housing.csv'):
    try:
        df = pd.read_csv(data_path)
        X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
        y = df['Price']
        
        model = LinearRegression()
        model.fit(X, y)
        return model, df
    except FileNotFoundError:
        return None, None

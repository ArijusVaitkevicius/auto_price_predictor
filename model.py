from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
import pandas as pd

df = pd.read_sql_table('cars', 'sqlite:///cars.db')
le = LabelEncoder()
dfle = df
dfle.make = le.fit_transform(dfle.make)
dfle.model = le.fit_transform(dfle.model)
dfle.model_type = le.fit_transform(dfle.model_type)
dfle.fuel = le.fit_transform(dfle.fuel)
dfle.gearbox = le.fit_transform(dfle.gearbox)
dfle.city = le.fit_transform(dfle.city)


def model():
    price = dfle
    cols = price.columns.tolist()
    x = price[cols[2:-1]]
    y = price['price']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
    new_model = LinearRegression().fit(x_train, y_train)

    pred = new_model.predict(x_test)
    spejimai = pd.Series(data=pred, name='Spėjimas')
    res = pd.concat([y_test.reset_index(), spejimai], axis=1)[['price', 'Spėjimas']]
    print(new_model.score(x_test, y_test))

    return res


model()



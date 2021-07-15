# ------------------------------------------------------------------------------------------------------------
#                                                  pickle
# ------------------------------------------------------------------------------------------------------------
#
#     with open('auto_price_predictor.pickle', 'wb') as f:
#         pickle.dump(new_model, f)
#

# ------------------------------------------------------------------------------------------------------------
#                                                  def predictor
# ------------------------------------------------------------------------------------------------------------

# def prediction(car):
#
#     pickled_model = open('auto_price_predictor.pickle', 'rb')
#     loaded_model = pickle.load(pickled_model)
#     predict = loaded_model.predict([car])
#     return predict[0]
#
#
# print(prediction([1.6, 2003, 110, 20000, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0,
#                   1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

# ------------------------------------------------------------------------------------------------------------
#                                                  1st model with LabelEncoder
# ------------------------------------------------------------------------------------------------------------

# le = LabelEncoder()
# dfle = df
# dfle.make = le.fit_transform(dfle.make)
# dfle.model = le.fit_transform(dfle.model)
# dfle.model_type = le.fit_transform(dfle.model_type)
# dfle.fuel = le.fit_transform(dfle.fuel)
# dfle.gearbox = le.fit_transform(dfle.gearbox)
# dfle.city = le.fit_transform(dfle.city)
#
#
# def model():
#     price = dfle
#     cols = price.columns.tolist()
#     x = price[cols[2:-1]]
#     y = price['price']
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)
#     new_model = LinearRegression().fit(x_train, y_train)
#
#     pred = new_model.predict(x_test)
#     spejimai = pd.Series(data=pred, name='Spėjimas')
#     res = pd.concat([y_test.reset_index(), spejimai], axis=1)[['price', 'Spėjimas']]
#     print(new_model.score(x_test, y_test))
#
#     return res
#
#
# model()

# acc 0.5869390453058725


# ------------------------------------------------------------------------------------------------------------
#                                                  2nd model with dummies
# ------------------------------------------------------------------------------------------------------------

# dummies_list = ['make', 'model', 'model_type', 'fuel', 'gearbox']
# for name in dummies_list:
#     dummies = pd.get_dummies(df[name])
#     df = pd.concat([df, dummies], axis=1)
#     df.drop([name], axis=1, inplace=True)
#
# col = df.columns.tolist()
# col = col[:6] + col[7:] + col[6:7]
# df = df[col]
#
#
# def model():
#     price = df
#     cols = price.columns.tolist()
#     x = price[cols[2:-1]]
#     y = price['price']
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)
#     new_model = LinearRegression().fit(x_train, y_train)
#
#     pred = new_model.predict(x_test)
#     spejimai = pd.Series(data=pred, name='Spėjimas')
#     res = pd.concat([y_test.reset_index(), spejimai], axis=1)[['price', 'Spėjimas']]
#     print(new_model.score(x_test, y_test))
#
#     return res
#
#
# model()

# acc 0.6753276479045196

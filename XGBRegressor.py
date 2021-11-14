import numpy as np
import pandas as pd

pd.set_option('display.width', 1000)
from pandas import DataFrame
from collections import Counter

#################################################
train_0 = DataFrame(pd.read_csv("..\\datasets\\ch10_train.csv"))
test_0 = DataFrame(pd.read_csv("..\\datasets\\ch10_test.csv"))
################################################
predictors = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
############################
rd = {}
for col in predictors:
    res = Counter(train_0[col])
    if str(res.most_common(1)[0][0]) == 'nan':
        rd[col] = res.most_common(2)[1][0]
    else:
        rd[col] = res.most_common(1)[0][0]

train = train_0.fillna(rd)
test = test_0.fillna(rd)

############################
ohe_train = pd.get_dummies(train[predictors])
##################################
train_ohe_col_list = list(ohe_train.columns.values)
################################
col_list_test = predictors.copy()
ohe_test = pd.get_dummies(test[col_list_test])
empty_df = DataFrame(columns=train_ohe_col_list)
test_final = pd.merge(empty_df, ohe_test, how='outer')

print(test_final)
##############################################
train_X = ohe_train
train_y = train_0.charges

from xgboost import XGBRegressor

my_model = XGBRegressor(
    max_depth=50,
    learning_rate=0.1,
    n_estimators=300,
    silent=1,
    objective='reg:linear',
    booster='gbtree',
    n_jobs=1,
    nthread=None,
    gamma=0,
    min_child_weight=0,
    max_delta_step=0,
    subsample=0.8999999999999999,
    colsample_bytree=0.6,
    colsample_bylevel=1,
    reg_alpha=0,
    reg_lambda=1,
    scale_pos_weight=1,
    base_score=0.5,
    random_state=0,
    seed=27,
    missing=np.NAN
)
my_model.fit(train_X, train_y, verbose=False)
test_y = my_model.predict(test_final)
print('**********Result*************')

df = DataFrame(test_y)
df.columns = ['predict_charges']
real_price = DataFrame(test_0.charges)
real_price.columns = ['real_charges']
MAE = DataFrame((df['predict_charges'] - real_price['real_charges']) / real_price['real_charges'] * 100)
MAE.columns = ['deviation percents %']
print(((test[predictors].join(df)).join(real_price)).join(MAE))

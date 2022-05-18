import pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
import json
from flask import jsonify
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

# q4

app = Flask(__name__)

def sorted_df_to_json(sorted_df):
    final_dict = {}
    for i in range(sorted_df.shape[0]):
        final_dict[i] = {}
        final_dict[i]['brand_name'] = sorted_df['brand_name'][i]
        final_dict[i]['item_name'] = sorted_df['item_name'][i]

    return final_dict

# part F
@app.route('/best', methods=['POST'])
def predict_churn_bulk():
    #print(request.get_json(), type(request.get_json()),request.data)
    dict = request.get_json()
    return dict['input']#request.get_json()

@app.route('/predict', methods=['POST'])
def return_ranked_meals():
    """
    Get the client's choice and the meals dataframe, scales the df and
    """
    dict_of_restaurants = request.get_json()['restaurants']
    # choose only the nearby resturant from database
    df = df_origin[df_origin.brand_name.apply(lambda x: x in dict_of_restaurants.values())]
    df.reset_index(drop=True, inplace=True)
    dict_of_nutrients = request.get_json()['input']
    # SCALING of df
    dg = df[dict_of_nutrients.keys()]
    st = StandardScaler()
    # dg = df.drop('brand_name', axis=1)
    st.fit(dg)
    dg = pd.DataFrame(st.transform(dg), columns=dg.columns)

    client_vals = np.array(list(dict_of_nutrients.values())).reshape(1, -1)
    client_vals = st.transform(client_vals)

    ind = df.index[euclidean_distances(client_vals, dg).argsort()[0]]
    sorted_meals = df.loc[ind]
    return sorted_df_to_json(sorted_meals) #.reset_index().iloc[:, :2]

if __name__ == '__main__':
    # with open('churn_model.pkl', 'rb') as file:
    #     loaded_model = pickle.load(file)
    df = pd.read_csv("CLEANED_DATAFRAME.csv")
    app.run(host='0.0.0.0', port=8080)


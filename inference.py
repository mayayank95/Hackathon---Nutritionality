import pickle
import pandas as pd
import numpy as np
from flask import Flask
from flask import request
import json
from flask import jsonify


# q4

app = Flask(__name__)


# part F
@app.route('/predict_churn_bulk', methods=['POST'])
def predict_churn_bulk():
    data = json.loads(request.get_json())
#     data = json.loads(json.dumps(request))
    # X_test = pd.DataFrame.from_dict(data)
    #
    # y_pred_calc = loaded_model.predict(X_test)
    # response_body = []
    # for i in range(len(y_pred_calc)):
    #     dict = {
    #         "input": X_test.iloc[i].to_dict(),
    #         "prediction": str(y_pred_calc[i])
    #     }
    #     response_body.append(dict)
    # return jsonify(response_body)
    return jsonify(data)


if __name__ == '__main__':
#     with open('churn_model.pkl', 'rb') as file:
#         loaded_model = pickle.load(file)
    app.run(host='0.0.0.0', port=8080)


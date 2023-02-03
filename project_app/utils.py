import numpy as np
import pandas as pd
import pickle
import json
import config

class Price_prediction():
    def __init__(self,CRIM,ZN,INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX,PTRATIO, B, LSTAT):
        self.CRIM = CRIM
        self.ZN = ZN
        self.INDUS = INDUS
        self.CHAS = CHAS
        self.NOX = NOX
        self.RM = RM
        self.AGE = AGE
        self.DIS = DIS
        self.RAD = RAD
        self.TAX = TAX
        self.PTRATIO = PTRATIO
        self.B = B
        self.LSTAT = LSTAT

    def load_model(self):
        with open(config.Model_file_path, "rb") as f:
            self.Model_predict=pickle.load(f)

        with open(config.Json_file_path, "r") as f:
            self.project_json=json.load(f)

        with open(config.scaling_file_path,"rb") as f:
            self.scaled_data=pickle.load(f)

    def predict_price(self):
        self.load_model()
        test_array=np.zeros(len(self.project_json["columns"]))
        test_array[0]=self.CRIM
        test_array[1]=self.ZN
        test_array[2]=self.INDUS
        test_array[3]=self.CHAS
        test_array[4]=self.NOX
        test_array[5]=self.RM
        test_array[6]=self.AGE
        test_array[7]=self.DIS
        test_array[8]=self.RAD
        test_array[9]=self.TAX
        test_array[10]=self.PTRATIO
        test_array[11]=self.B
        test_array[12]=self.LSTAT

        test_array1=self.scaled_data.transform([test_array])

        prediction=self.Model_predict.predict(test_array1)

        return prediction
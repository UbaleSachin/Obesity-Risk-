import os
from pathlib import Path
from ObesityRisk.utils.common import *


class PredictionPipeline:
    def __init__(self):
        #self.model = load_pickle(Path('artifacts\model_trainer\model.pkl'))
        #self.preprocessor = load_pickle(Path('artifacts\data_transformation\preprocessor.pkl'))
        pass

    def predict(self, data):
        model_path = os.path.join(Path('artifacts\model_trainer', 'model.pkl'))
        preprocessor_path = os.path.join(Path('artifacts\model_trainer', 'preprocessor.pkl'))

        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
                                  
        scaled_data = preprocessor.transform(data)
        prediction = model.predict(scaled_data)

        return prediction


class CoustomData:
    def __init__(self,
                 Gender: str,
                 Age: str,
                 Height: str,
                 Weight: str,
                 family_history_with_overweight: str,
                 FAVC: str,
                 FCVC: str, 
                 NCP: str, 
                 CAEC: str,
                 SMOKE: str,
                 CH2O: str,
                 SCC: str,
                 FAF: str, 
                 TUE: str,
                 CALC: str,
                 MTRANS: str):
        self.Gender = Gender
        self.Age = Age
        self.Height = Height
        self.Weight = Weight
        self.family_history_with_overweight = family_history_with_overweight
        self.FAVC = FAVC
        self.FCVC = FCVC
        self.NCP = NCP
        self.CAEC = CAEC
        self.SMOKE = SMOKE
        self.CH2O = CH2O
        self.SCC = SCC
        self.FAF = FAF
        self.TUE = TUE
        self.CALC = CALC
        self.MTRANS = MTRANS

    def get_data_as_dataframe(self):
        try:
            custom_data_input = {'Gender': [self.Gender],
                                'Age': [self.Age],
                                'Height': [self.Height],
                                'Weight': [self.Weight],
                                'family_history_with_overweight': [self.family_history_with_overweight],
                                'FAVC': [self.FAVC],
                                'FCVC': [self.FCVC],
                                'NCP': [self.NCP],
                                'CAEC': [self.CAEC],
                                'SMOKE': [self.SMOKE],
                                'CH2O': [self.CH2O], 
                                'SCC': [self.SCC],
                                'FAF': [self.FAF], 
                                'TUE': [self.TUE], 
                                'CALC': [self.CALC], 
                                'MTRANS': [self.MTRANS]
                                }
            return pd.DataFrame(custom_data_input)
        except Exception as e:
            raise e

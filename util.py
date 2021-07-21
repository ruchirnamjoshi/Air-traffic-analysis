import pickle
import json
import numpy as np

_data_columns = None
_model = None


def predict_passenger_count(op_air, IATA_code, pub_air, pa_IATA, geo_summ, geo_region, act_code, price_cat, terminal, bord_area,
               aa_code, month, pas_count):
    input = np.zeros(len(_data_columns))
    input[318] = pas_count

    bal = _data_columns.index(op_air.lower())
    input[bal] = 1

    apt = _data_columns.index(IATA_code.lower())
    input[apt] = 1

    loc = _data_columns.index(pub_air.lower())
    input[loc] = 1

    loc2 = _data_columns.index(pa_IATA.lower())
    input[loc2] = 1

    loc3 = _data_columns.index(geo_summ.lower())
    input[loc3] = 1

    loc4 = _data_columns.index(geo_region.lower())
    input[loc4] = 1

    loc5 = _data_columns.index(act_code.lower())
    input[loc5] = 1

    loc6 = _data_columns.index(price_cat.lower())
    input[loc6] = 1

    loc7 = _data_columns.index(terminal.lower())
    input[loc7] = 1

    loc8 = _data_columns.index(bord_area.lower())
    input[loc8] = 1

    loc9 = _data_columns.index(aa_code.lower())
    input[loc9] = 1

    loc10 = _data_columns.index(month.lower())
    input[loc10] = 1

    return int(_model.predict([input]))


def load_artifacts():
    global _data_columns
    global _model

    print('Loading Artifacts...')

    with open('C:/Users/ruchi/7.Air traffic project/columns.json', 'r') as f:
        _data_columns = json.load(f)['data_columns']

    with open('./air_traffic.pickle', 'rb') as f:
        _model = pickle.load(f)

    print('Artifacts...Loaded')


def column_names():
    return _data_columns


load_artifacts()
#print(int(predict_passenger_count('ATA Airlines','TZ','ATA Airlines','TZ','Domestic','US','Deplaned','Low Fare','Terminal 1','B','Deplaned','July',27271)[0][0]))
#print(column_names())
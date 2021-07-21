from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_column_names')
def get_column_names():
    response = {'Columns': util.column_names()}
    return response


@app.route('/predict_passenger_count', methods=['POST'])
def predict_passenger_count():
    pas_count = float(request.form['pas_count'])
    op_air = (request.form['op_air'])
    IATA_code = (request.form['IATA_code'])
    pub_air = (request.form['pub_air'])
    pa_IATA = request.form['pa_IATA']
    geo_summ = request.form['geo_summ']
    geo_region = request.form['geo_region']
    act_code = request.form['act_code']
    price_cat = request.form['price_cat']
    terminal = request.form['terminal']
    bord_area = request.form['bord_area']
    aa_code = request.form['aa_code']
    month = request.form['month']

    response = jsonify({'estimated_p': util.predict_passenger_count(op_air, IATA_code, pub_air, pa_IATA, geo_summ, geo_region, act_code, price_cat, terminal, bord_area,
               aa_code, month, pas_count)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run()

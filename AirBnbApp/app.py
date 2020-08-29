from flask import Flask, request, jsonify, render_template
import pickle
import sklearn
import pandas as pd
import csv
import numpy as np
from AirBnbApp.predict import vectorize_data, pre

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    def get_df():
        data_file = open('/app/AirBnbApp/airbnb.csv')
        csv_file = csv.reader(data_file)
        info = []
        for row in csv_file:
            info.append(row)
        data = pd.DataFrame(info)
        data.columns = ['No','city', 'state', 'room_type', 'security_deposit',        'guests_included', 'extra_people','minimum_nights', 'maximum_nights', 'review_scores_rating']
        data = data.drop(data.index[0])
        return data


    @app.route('/')
    def home():
        return jsonify((
        'Project: AirBnb Pricing API',
        'Developers: Nour Etienne Huens de Brouwer & Yuanjin Ren',
    ))

    @app.route('/data', methods=['GET','POST'])
    def data():
        info = get_df()
        return render_template('data.html', data=info.to_html(index=False))

    @app.route('/data/bycity/<city>', methods=['GET','POST'])
    def city(city):
        info_city = get_df()
        df_city = info_city[info_city['city'] == city]
        return render_template('bycity.html', city=df_city.to_html(index=False))

    
    @app.route('/data/bytype', methods=['GET','POST'])
    def price():
        city = str(request.args['city'])
        room_type = str(request.args['room_type'])
        info = get_df()
        df_city = info[info['city'] == city]
        df_type = df_city[df_city['room_type'] == room_type]
        return render_template('byroomtype.html', roomtype=df_type.to_html(index=False))


    @app.route('/predict',methods=['POST','GET'])
    def predict():
        city = str(request.args['city'])
        room_type = str(request.args['room_type'])
        security_deposit = float(request.args['security_deposit'])
        guests_included = int(request.args['guests_included'])
        mininum_nights = int(request.args['mininum_nights'])

        prediction = pre(city=city, room_type=room_type, security_deposit=security_deposit, guests_included=guests_included, min_nights=mininum_nights)

        return jsonify(prediction)
        
    return app

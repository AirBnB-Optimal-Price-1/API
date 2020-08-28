from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os
import datetime
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.layers import Dropout
from tensorflow.keras import regularizers
import pandas as pd
from tensorflow.keras.models import load_model

model = load_model('AirBnbApp/light_model.h5')

def vectorize_data(data):
    dtm = tfidf.transform(data)
    dtm_df = pd.DataFrame(dtm.todense(), columns=tfidf.get_feature_names())
    return dtm_df

def pre(city='United States', room_type='any', security_deposit=0.0, guests_included=1, min_nights=1):
    # Make dataframe from the inputs
    df = pd.DataFrame(
        data=[[city, room_type, security_deposit, guests_included, min_nights]], 
        columns=['city', 'room_type', 'security_deposit', 'guests_included', 'min_nights']
    )
    df["text_combined"] = df[['city', 'room_type']].apply(' '.join, axis=1)
    matrix = vectorize_data(df["text_combined"])
    df = pd.concat([df, matrix], axis=1)    
    df = df.drop(columns=['city', 'room_type', 'text_combined'])
    # Get the model's prediction
    pred = model.predict(df.values)[0][0]
    # return f'city: {city}, room_type: {room_type}, security_deposit: {security_deposit}, guests_included: {guests_included}, min_nights: {min_nights}, price: ${pred:.2f}'

    return jsonify({"city": city, 
                    "room_type": room_type, 
                    "security_deposit": security_deposit, 
                    "guests_included": guests_included, 
                    "min_nights": min_nights,
                    "price": results})
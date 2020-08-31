# AirBnb
Unit3 Build Week

Data Source:
airbnb.csv file

Entry point: 
__init__.py file

In app.py file
get_df() is used to convert the csv file into a dataframe.
@app.route('/') is the homepage of this app.

@app.route('/data', methods=['GET','POST']) shows the dataframe of all data. 

@app.route('/data/bycity/<city>', methods=['GET','POST']) 
We are able to put city name in the route, then all airbnb info of this city will be showed in a dataframe. 

@app.route('/data/bytype', methods=['GET','POST'])
We are able to check airbnb info by using the city name and room type. The value of city name and room type should be input by queries in the URL. For example,
https://localhost:5000/data/bytype?city=Portland&room_type=Shared%20room

@app.route('/predict',methods=['POST','GET'])
This route is used to predict airbnb price by defining values of each parameter. The model under the hood is a CNN model using tensorflow and vectorization. The trained ffidf was obtained by pickle file tfidf.pkl. And the trained CNN model was obtained by light_model.h5.  

To push to Heroku, the directory of the data source need to be changed. The directory can be checked by using 'heroku run bash' command.
By this command, we can check the path of our app, then we can get the path of csv file using 'pwd' command. 

# Heroku Links
1. Homepage
https://airbnbapi-dspt6.herokuapp.com/
2. All data page (It shows the whole dataset)
https://airbnbapi-dspt6.herokuapp.com/data
3. Filter data by city name(city name in the URL can be uppercase or lowercase, it will be converted to uppercase automatically)
https://airbnbapi-dspt6.herokuapp.com/data/bycity/Portland
4. Filter data by using city name and room type in URL queries
https://airbnbapi-dspt6.herokuapp.com/data/bytype?city=Portland&room_type=Shared%20room
5. To get Airbnb price prediction, we need to pass values of parameters in the URL as below
https://airbnbapi-dspt6.herokuapp.com/predict?city=NEW%20YORK&room_type=HOTEL%20ROOM&security_deposit=100.0&guests_included=2&mininum_nights=2

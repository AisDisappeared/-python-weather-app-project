import requests
import time 
import mysql.connector
from datetime import datetime

# making a connection between python and mysql , and Also making a cursor 
cnx = mysql.connector.connect(user='root',password='ali@grpc1',host='127.0.0.1',database='weather_app')
cursor = cnx.cursor()




# define a function that will get the timestamp parameter to convert into a datetime object
def convertor(Datetime):
    date_obj = datetime.fromtimestamp(Datetime)
    return date_obj.strftime("%Y-%m-%d %H:%M:%S")
    

# defining a function that scrap our specific fields key of json data and render them to get_weather_data function 
def proccess_data(data):
    return {'temp' : data['main']['temp'],'name' :data['name'],'Datetime' : convertor(int(data['dt'])),
            'humidity' : data['main']['humidity'],'status': data['weather'][0]['main']}


def get_weather_data(Lat=35.7219,Long=51.3347,API_KEY='5142d212b6ddc15d8d50c11cb24b459d'):

# The URL that we are going to request and sending parameters to OpenWeather API
    URL = "https://api.openweathermap.org/data/2.5/weather?lat={Lat}&lon={Long}&appid={API_KEY}".format(Lat=Lat, Long=Long, API_KEY=API_KEY)
    req = requests.get(URL)

# Convert the data into json format 
    data = req.json()
    return proccess_data(data) 


data = (get_weather_data())
list_data = [value for key,value in data.items()]


def insert_data(cursor,cnx,data=list_data):
    query = "INSERT INTO info VALUES(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')" % (str(list_data[0]), str(list_data[1]), str(list_data[2]), str(list_data[3]) , str(list_data[4]))
    cursor.execute(query)
    cnx.commit()


while True :
    data_weather = get_weather_data()
    list_data_weather = [value for key,value in data_weather.items()]
    insert_data(cursor,cnx,list_data_weather)
    print(data_weather)
    time.sleep(10)
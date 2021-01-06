import sqlite3
import weather_scraper
from datetime import datetime
import time

#Queries
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    nationality TEXT
);
"""

create_temperature_table = """
CREATE TABLE IF NOT EXISTS WeatherLogs(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    CurrentTemperature STRING NOT NULL,
    date STRING NOT NULL,
    time STRING NOT NULL
    );
    """


#create methods
def get_time():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time

def get_date():
    now = datetime.now()
    date = now.strftime("%Y-%d-%m")
    return str(date)

def get_temp():
    temp = weather_scraper.weather_tampa()
    return temp

def send_temp_date_time_data():
    connection = sqlite3.connect('/Volumes/JaredCrucialSSD-Extended/databases/pythonsqlite.db')
    cursor = connection.cursor()

    time = get_time()
    date = get_date()
    temp = get_temp()

    #tests
    """
    print(time)
    print(date)
    print(temp)
    """

    sql_insert_with_param = 'INSERT INTO testLogs (CurrentTemperature, date, time) VALUES (?, ?, ?);'
    data_tuple = (temp, date, time)
    cursor.execute(sql_insert_with_param, data_tuple)
    connection.commit()
    connection.close()


def main():
    x = 0
    time_started = get_time()
    print(f"Data collection started at {time_started}")
    
    while x < 40:
        send_temp_date_time_data()
        x+=1
        time.sleep(1)
    
    time_ended = get_time()
    print(f"Data collection stopped at {time_ended}")




#test methods
main()
#get_time()

import datetime
import pandas as pd
import random

points_to_create = 86400 # Number of data points to create
# points_to_create = 1000 # Number of data points to create
number_of_sensors = 10 # Number of sensors for which to create data for each data point
number_of_files = 3 # Number of files to create

current_datetime = datetime.datetime.now()

for n in range(number_of_files):
    filename = current_datetime.strftime('%Y_%m_%d') + '.parquet'
    df = pd.DataFrame()
    for i in range(points_to_create):
        
        for y in range(number_of_sensors):
            sensor_dict = {
                'datetime': current_datetime,
                'sensor_id': y,
                'sensor_reading': round(random.uniform(60, 100), 2),
                'sensor_unit': 'c'
            }
            df = pd.concat([df, pd.DataFrame([sensor_dict])], ignore_index=True)


        current_datetime = current_datetime + datetime.timedelta(seconds=1) # Add one second for next run
        print(f'File: {n}, Point: {i}')
    current_datetime = current_datetime + datetime.timedelta(days=1)
    df.to_parquet(filename)
    
import MySQLdb
import numpy as np
import os


path = './data'

data = {
    'gps': {
        'filename': 'GpsLocation_01_Dec_2015_08-20-32.900_GMT+00-00.txt',
        'format': 'i8,f,f,f,f,f,f' },
    'gyroscope': {
        'filename': 'L3G4200D_Gyroscope_sensor_01_Dec_2015_08-20-32.900_GMT+00-00.txt',
        'format': 'i8,f,f,f,f' },
    'linear_accelerometer': {
        'filename': 'Linear_Acceleration_Sensor_01_Dec_2015_08-20-32.900_GMT+00-00.txt',
        'format': 'i8,f,f,f,f' },
    'acceleration': {
        'filename': 'LIS3DH_3-axis_Accelerometer_01_Dec_2015_08-20-32.900_GMT+00-00.txt',
        'format': 'i8,f,f,f,f' }
}


for k, v in data.items():
    print(k)
    table = np.genfromtxt(os.path.join(path, v['filename']), dtype=v['format'], delimiter=',')
    print(table)


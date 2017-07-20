import MySQLdb
import numpy as np
import os
import getpass


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
    print(k, " ... ")
    v['table'] = np.genfromtxt(os.path.join(path, v['filename']), dtype=v['format'], delimiter=',')
    # print(v['table'])

pw = getpass.getpass()
db = MySQLdb.connect(host='localhost', user='root', passwd=pw, db='roadquality')
c = db.cursor()

#### doing this messes things up...
# schema = open('roads-schema.sql').read()
# c.execute(schema)
# c.close()
# db.commit()

c = db.cursor()
c.execute("SELECT * FROM `Devices` WHERE `idDevices` = 0")
result = c.fetchone()
print("Device 0: {}".format(result))

if result is None:
    print("adding device")
    c.execute("INSERT INTO `Devices` (idDevices, name) VALUES (%s, %s)", (0, "magic device #1",))

c.executemany("INSERT INTO `GPS` (deviceId, time, accuracy, lattitude, longitude, altitude, bearing, speed)"
              "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
              [(0,) + tuple(v) for v in data['gps']['table']])

c.executemany("INSERT INTO `Accelerometer` (deviceId, time, accuracy, x, y, z)"
              "VALUES (%s, %s, %s, %s, %s, %s)",
              [(0,) + tuple(v) for v in data['acceleration']['table']])

c.executemany("INSERT INTO `LinearAcceleration` (deviceId, time, accuracy, x, y, z)"
              "VALUES (%s, %s, %s, %s, %s, %s)",
              [(0,) + tuple(v) for v in data['linear_accelerometer']['table']])

c.executemany("INSERT INTO `Gyroscope` (deviceId, time, accuracy, x, y, z)"
              "VALUES (%s, %s, %s, %s, %s, %s)",
              [(0,) + tuple(v) for v in data['gyroscope']['table']])

db.commit()
#c.executemany("INSERT INTO `GPS`

import adxl345 #import the library
from time import sleep

ADDRESS=0x53

acc=adxl345.ADXL345(i2c_port=1,address=ADDRESS) #instantiate
acc.load_calib_value() #load calib. values in accel_calib
acc.set_data_rate(data_rate=adxl345.DataRate.R_100) #see datasheet
acc.set_range(g_range=adxl345.Range.G_16,full_res=True) # ..
acc.measure_start()

#acc.calibrate() #calibrate only one time

while(True):
       x,y,z=acc.get_3_axis_adjusted()
       print(x,y,z)
       sleep(0.5)
        

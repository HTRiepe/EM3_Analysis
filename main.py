import time

import matplotlib.pyplot as plt
import requests
# import numpy as np
# import matplotlib as mpl
import pandas as pd

ip = "192.168.0.50"  # Set your IP address from Shelly EM3
solar = False  # Is that make True when you youse are Solar Panel
local = True # Do you have the data in the same place with the name "Phase_1.CSV","Phase_2.CSV","Phase_3.CSV",
Data_request = ["http://" + ip + "/emeter/0/em_data.csv", "http://" + ip + "/emeter/1/em_data.csv",
                "http://" + ip + "/emeter/2/em_data.csv"]
Data_request_voltage = ["http://" + ip + "/emeter/0/vm_data.csv", "http://" + ip + "/emeter/1/vm_data.csv",
                        "http://" + ip + "/emeter/2/vm_data.csv"]
## Get The Data
print("Run up get data")
if (local == False):
	Phase_1 = pd.read_csv(Data_request[0])
else:
	Phase_1 = pd.read_csv('Phase_1.csv')

time.sleep(5)
print("(1)1/3 E-Phasen geladen")
if (local == False):
	Phase_2 = pd.read_csv(Data_request[1])
else:
	Phase_2 = pd.read_csv('Phase_2.csv')
time.sleep(5)
print("(1)2/3 E-Phasen geladen")
if (local == False):
	Phase_3 = pd.read_csv(Data_request[2])
else:
	Phase_3 = pd.read_csv('Phase_3.csv')
time.sleep(5)
print("(1)3/3 E-Phasen geladen")
print(requests.get("http://192.168.0.50/reboot/"))
print("(2) Done /n Data is ")

##Orga the Data
Phase_SUM = pd.merge_ordered(Phase_1, Phase_2, on='Date/time UTC', how='outer')
Phase_SUM = pd.merge_ordered(Phase_SUM, Phase_3, on='Date/time UTC', how='outer')
if not solar:
	try:
		del Phase_SUM['Returned energy Wh (A)']
		del Phase_SUM['Returned energy Wh (B)']
		del Phase_SUM['Returned energy Wh (C)']
	except:
		print("Failed to cleanup ")
else:
	print ("You have are Solar Panel install in your home circut")
	
x = (Phase_SUM['Date/time UTC'])
if not solar:
	yr_1 = Phase_SUM['Returned energy Wh (A)']
	yr_2 = Phase_SUM['Returned energy Wh (B)']
	yr_3 = Phase_SUM['Returned energy Wh (A)']
	#plt.plot(x, yr_1, color="red")
	#plt.plot(x, yr_2, color="blue")
	#plt.plot(x, yr_3, color="green")
yc_1 = Phase_SUM['Active energy Wh (A)']
yc_2 = Phase_SUM['Active energy Wh (B)']
yc_3 = Phase_SUM['Active energy Wh (C)']

plt.plot(x, yc_1, color="red")
plt.plot(x, yc_2, color="blue")
plt.plot(x, yc_3, color="green")
plt.show()
Phase_SUM_EDIT = Phase_SUM
Phase_SUM_EDIT['Date/time UTC'].str.split(" ", expand=True)
print(Phase_SUM_EDIT)

print(Phase_SUM)

print("5/5 Done")

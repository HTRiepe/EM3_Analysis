import requests
import numpy as np
import matplotlib as mpl
import pandas as pd

ip = "192.168.0.50"  # Set your IP address from Shelly EM3

Data_request = ["http://" + ip + "/emeter/0/em_data.csv", "http://" + ip + "/emeter/1/em_data.csv",
                "http://" + ip + "/emeter/2/em_data.csv"]
print(Data_request)
Phase_1 = pd.read_csv(Data_request[0])
print("1/5 Done")
Phase_2 = pd.read_csv(Data_request[1])
print("2/5 Done")
Phase_3 = pd.read_csv(Data_request[2])
print("3/5 Done")
print(Phase_1)
print(Phase_2)
print(Phase_3)

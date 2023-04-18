# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import glob
import matplotlib.pyplot as plt
import numpy as np

from obspy import UTCDateTime
from obspy.clients.seedlink import Client
#from obspy.clients.fdsn import Client
from obspy.clients.seedlink.easyseedlink import create_client
#from obspy.clients.earthworm import Client
from obspy.core import read
from obspy import read_inventory




ipserver = "163.178.101.86" #seedlink - earthworm
#ipserver = "163.178.170.170" #apollo

port = 18000
timeout = 60
startime = UTCDateTime('2023-04-11T19:20:00.000')
endtime =startime + 10*60


myClient = Client(ipserver,port,timeout,debug=False)
info = myClient.get_info()

st = read()
print(info)




t = UTCDateTime()
st1 = read("C:/seedLink/20230901345.TJS2.HNZ")
#st = myClient.get_waveforms("MF", "AATN", "?", "HN?", t-20, t)
#inv = read_inventory("C:/seedLink/20230901345.TJS2.HNZ")

st_acc = st1.copy()
#st_acc.remove_response(inventory = inv, output="ACC")

"""""
st = myClient.get_waveforms("MF","AATN","?","HH*",startime,endtime)
"""





#st1.plot()
#st_acc.plot()













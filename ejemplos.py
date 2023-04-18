

t = UTCDateTime() - 1500

st = myClient.get_waveforms("MF", "AFRA", "?", "HN?", t, t + 20)

print(st)
st.plot()


def handle_data(trace):
    print("Recibiendo la traza: ")
    print(trace)
    trace.plot()
    print()


myClient = create_client(ipserver,on_data=handle_data)
myClient.select_stream('MF','AMTY','HNN')
myClient.run()

"""""
station = read("C:/seedLink/20230901345.TJS2.HNZ")
#station += read("C:/seedLink/20230901345.TJS2.HNE")
#station += read("C:/seedLink/20230901345.TJS2.HNN")
print(station)


station.plot()
"""


"""
Codigo para multiplicar valores del stream por una constante -- todavía no funciona

factor = 4.906e-4
data = st1[0].data
times = st1[0].times()


data_acc = st_acc[0].data
times_acc = st_acc[0].times()

with np.nditer(st_acc[0].data, op_flags=['readwrite']) as it:

   for x in it:

       x[...] = factor * x



st1.plot()
st_acc.plot()

"""
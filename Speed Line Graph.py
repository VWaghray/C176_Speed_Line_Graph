import speedtest
import matplotlib.pyplot as plt
import time
list_ds = []
list_us = []

for i in range(5):
    st = speedtest.Speedtest()
    ds = round(st.download()/1000000,2)
    list_ds.append(ds)
    us = round(st.upload()/1000000,2)
    list_us.append(us)
    time.sleep(60)
    print(list_ds)
    print(list_us)
    
x = [1,2,3,4,5]
plt.plot(x, list_ds, label = "Download Speed")
plt.title('Speed')
plt.plot(x, list_us,label = "Upload Speed")
plt.legend()
plt.show()

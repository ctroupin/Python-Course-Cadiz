# IPython log file

S = 36.4
if S > 40.:
    print("Salinity is too high")
elif S < 0.0:
    print("Salinity is too low")
else:
    print("Good salinity")
    
S = -2.
if S > 40.:
    print("Salinity is too high")
elif S < 0.0:
    print("Salinity is too low")
else:
    print("Good salinity") 
speed = [0, 1, 2.4, 0.02]
for s in speed:
    print(speed * 1000. / 3600)
speed = [0, 1, 2.4, 0.02]
for s in speed:
    print(s * 1000. / 3600)
i = 1
while i ** 0.5 < 4.:
    i += 1
i
i = 1
while i ** 0.5 < 4.:
    i += 1
i
devices = ["Glider", "CTD", "Drifting buoys", "Satellite"]
for d in devices:
    print(d)
variable_units = {"temperature": "degrees C", 
                  "salinity": "PSU ", 
                  "pressure": "hPa",
                  "velocity": "m/s"}
variable_units = {"temperature": "degrees C", 
                  "salinity": "PSU ", 
                  "pressure": "hPa",
                  "velocity": "m/s"}
for v in variable_units:
    print(v)
variable_units = {"temperature": "degrees C", 
                  "salinity": "PSU ", 
                  "pressure": "hPa",
                  "velocity": "m/s"}
for v in variable_units:
    print(v)
for v in variable_units:
    print(variable_units[v])
variable_units = {"temperature": "degrees C", 
                  "salinity": "PSU ", 
                  "pressure": "hPa",
                  "velocity": "m/s"}
for v in variable_units:
    print(v)
for v in variable_units:
    print(variable_units[v])
for k, v in variable_units.items():
    print(k, v)
for ii, dev in devices:
    print(ii, dev)
for ii, dev in enumerate(devices):
    print(ii, dev)
for i in range(0, 10):
    print(i)
for i in range(0, 10):
    print(i**i)
for i in range(0, 10):
    print(i**3)
for i in range(0, 10):
    print(i**3)
for i in range(0, 5):
    print(i**3)
for i in range(0, 6):
    print(i**3)
-1 ** (0.5)
-1.**(0.5)
(-1).**(0.5)
(-1.)**(0.5)
(-1)**(0.5)
get_ipython().magic('logoff')
get_ipython().magic('logstart')
get_ipython().magic('logstate')
get_ipython().magic('logstop')

from datetime import datetime, timedelta

time = datetime(2020,10,1,21,22,22)
t = time + timedelta(hours=20,minutes=30)
if t>time:
    print(time)
    print('t가 더큼{}'.format(t))
else:
    print('time{}'.format(time))
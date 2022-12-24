#New parts for the main file, fiddling, tinkering and tests are made here
#Then implemented into the main file. 

from Time_Extractor import VN_Summary_Extractor
YU = 'D:\Programming\Own_Projects\Time_Extractor\Example_Subjects\終の空 - Yukito.docx'

Yuki = VN_Summary_Extractor(YU)
# print(Yuki.old_time())


data = [x for x in Yuki.old_time() if ";" in x]
data = data[0].split()
data = [x.split(",") if "," in x else x for x in data]

#Takes elements out of nested lists and puts them into the main list, removing the nested lists. 
def list_clear(data):
    placeholder = [x for x in data if type(x) == list]
    data = [x for x in data if type(x) != list]
    for x in placeholder:
        data.extend(x)
    return data

data = list_clear(data)

#Takes out only the four chars before and four chars after "-", specific for that format.
def num_stripper(st):
    return (st[:st.find("-")]+st[st.find("-"):st.find("-")+5])

data = [num_stripper(x) for x in data]
data = [x for x in data if len(x) == 9]
data = ['{}:{}-{}:{}'.format(SP[0:2], SP[2:4], SP[5:7], SP[7:9]) for SP in data]





from datetime import datetime, time as datetime_time, timedelta
def time_diff(start, end):
    if isinstance(start, datetime_time): # convert to datetime
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end: # e.g., 10:33:26-11:15:49
        return end - start
    else: # end < start e.g., 23:55:00-00:25:00
        end += timedelta(1) # +day
        assert end > start
        return end - start

print(time_diff('21:00:00', '00:10:00'))
Check = [10,60,30,25,120,15,15,60,35,35,60,60,60,70,60,60,60,60,60,60,65,30,60,60,20,60,60,40,15,60,30,15,60,60,5]
print(sum(Check))
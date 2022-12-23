from Time_Extractor import VN_Summary_Extractor

Yuki = VN_Summary_Extractor('終の空 - Yukito.docx')
# print(Yuki.old_time())


data = [x for x in Yuki.old_time() if ";" in x]
data = data[0].split()
data = [x.split(",") if "," in x else x for x in data]


print(data)

print("")
for x in data:
    if type(x) == list:
        li = x
        data.remove(x)
        data += li

print(data)

print("")
st = '1950-2130(100/M35)'
print(st[:st.find("-")]+st[st.find("-"):st.find("-")+5])


'''
from datetime import datetime
S = "19:50"
E = "21:30"

t1 = datetime.strptime(S, "%H:%M")
t2 = datetime.strptime(E, "%H:%M")

t = t2-t1
t = t.total_seconds()
print(t//60)
'''

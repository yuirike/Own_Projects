from Time_Extractor import VN_Summary_Extractor
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import docx


NO = 'D:\\Programming\\Own_Projects\\Time_Extractor\\Example_Subjects\\Natsu no Owari.docx'

data = []
doc = docx.Document(NO)
for line in doc.paragraphs:
    data.append(line.text)


data = [x.split(" ") for x in data]

new_data = []
for x in data:
    new_data.extend(x)


data = [x for x in new_data if x.isalpha()]
data = [x.lower() for x in data]


keys = list(set(data))

dic = {}
for key, datum in zip(keys, data):
    dic[key]=data.count(key)

data = [x for x in dic.items()]

print(data)

data.sort()
print(data)
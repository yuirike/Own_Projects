#Stuff is applied here, imported from the main file. 

from Time_Extractor import VN_Summary_Extractor
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

NO = 'D:\\Programming\\Own_Projects\\Time_Extractor\\Example_Subjects\\Natsu no Owari.docx'
KK = 'D:\Programming\Own_Projects\Time_Extractor\Example_Subjects\KokoKata.docx'
WR = 'D:\Programming\Own_Projects\Time_Extractor\Example_Subjects\With Ribbon.docx'
YU = 'D:\Programming\Own_Projects\Time_Extractor\Example_Subjects\終の空 - Yukito.docx'


With_Riboon  = VN_Summary_Extractor(WR)
print(With_Riboon.time())


import sys
import os

txt_input = 'launchdata.txt'
bulno = ""

print("DROP TABLE launches;")
print("CREATE TABLE launches (")
print("launchID TEXT,")
print("launchJDate DATE,")
print("launchDate TIMESTAMP,")
print("lv_type TEXT,")
print("lv_serial TEXT,")
print("lv_Payload TEXT,")
print("ls_state TEXT,")
print("lv_name TEXT,")
print("lv_launchPad TEXT,")
print("lv_outcome TEXT,")
print("lv_buletin TEXT")
print(");")
    
with open(txt_input) as fp:
    line_lv = fp.readline()
    cnt=1
    while line_lv:
        if len(line_lv)<154: bulno = ""
        else: bulno = line_lv[154:len(line_lv)].strip()
        if len(bulno) == 2:
            bulno = "0"+bulno
            bulno = "[[/bul/"+bulno+"]["+str(int(bulno))+"]]"
        if len(bulno) == 3:
            bulno = "[[/bul/"+bulno+"]["+str(int(bulno))+"]]"
        print("INSERT INTO launches VALUES ('" + line_lv[0:12].strip() +"','" + line_lv[12:23].strip() + "','" + line_lv[12:31].strip() +"','" + line_lv[31:55].strip().replace("'","''").replace("Chang Zheng ","CZ-") + "','"+ line_lv[55:76].strip() + "','" + line_lv[76:123].strip().replace("'","''") + "','" + line_lv[123:129].strip() + "','" + line_lv[129:142].strip() + "','" + line_lv[142:153].strip() + "','" + line_lv[153:154].strip() + "','" + bulno + "');")
        line_lv = fp.readline()
        cnt+=1

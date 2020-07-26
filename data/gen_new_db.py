import sys
import os
import time

# just for debugging purposes
tic = time.perf_counter()

txt_input = 'launchdata.txt'
bulno = ""

print("DROP TABLE launches;")
print("CREATE TABLE launches (")
print("launchID TEXT,")
print("launchDate TIMESTAMP,")
print("lv_type TEXT,")
print("lv_serial TEXT,")
print("lv_Payload TEXT,")
print("sat_currStatus TEXT,")
print("sat_dateStatus TEXT,")
print("sat_orbitClass TEXT,")
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
        if len(line_lv)<172: bulno = ""
        else: bulno = line_lv[173:175].strip()
        if len(bulno) == 2: 
            bulno = "0"+bulno
            bulno = "[[/bul/"+bulno+"]["+str(int(bulno))+"]]"

        print("INSERT INTO launches VALUES ('"+ line_lv[0:11].strip() +"','"+ line_lv[11:29].strip() +"','"+ line_lv[29:52].strip().replace("'","''") +"','"+ line_lv[52:72].strip() +"','"+ line_lv[72:117].strip().replace("'","''") + "','"+ line_lv[117:122].strip() +"','"+ line_lv[122:134].strip() +"','"+ line_lv[134:144].strip() +"','"+ line_lv[144:149].strip() +"','"+ line_lv[149:161].strip() +"','"+ line_lv[161:171].strip() +"','"+ line_lv[171:173].strip() +"','"+bulno + "');")
        line_lv = fp.readline()
        cnt+=1

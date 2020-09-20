import sys
import os
import csv

tsv_file = open("launch.tsv")

read_tsv = csv.reader(tsv_file, delimiter="\t")

for row in read_tsv:
  Launch_Tag = row[0].strip()
  Launch_JD = row[1].strip()
  Launch_Date = row[2].strip()
  LV_Type = row[3].strip()
  Variant = row[4].strip()
  Flight_ID = row[5].strip()
  Flight = row[6].strip()
  Mission = row[7].strip()
  FlightCode = row[8].strip()
  Platform = row[9].strip()
  Launch_Site = row[10].strip()
  Launch_Pad = row[11].strip()
  Ascent_Site = row[12].strip()
  Ascent_Pad = row[13].strip()
  Apogee = row[14].strip()
  Apoflag = row[15].strip()
  Range = row[16].strip()
  RangeFlag = row[17].strip()
  Dest = row[18].strip()
  Agency = row[19].strip()
  Launch_Code = row[20].strip()
  Group = row[21].strip()
  Category = row[22].strip()
  ls_state = ""

  if "-S" not in Launch_Tag and "-A" not in Launch_Tag and "-M" not in Launch_Tag and "-U" not in Launch_Tag and "-W" not in Launch_Tag and "-Y" not in Launch_Tag and "-E" not in Launch_Tag and "-S" not in Launch_Tag and "2014-000" not in Launch_Tag and "#Launch_Tag" not in Launch_Tag:
  # ^filtering out non-orbital launches or pad explosions
    
    if "F" in Launch_Tag: Launch_Code = "F"
    else: Launch_Code = "S"

    if "?" in Launch_Date: Launch_Date = Launch_Date.replace("?","")
    if "Jan" in Launch_Date: Launch_Date = Launch_Date.replace(" Jan ", "-01-")                             
    if "Feb" in Launch_Date: Launch_Date = Launch_Date.replace(" Feb ", "-02-")
    if "Mar" in Launch_Date: Launch_Date = Launch_Date.replace(" Mar ", "-03-")
    if "Apr" in Launch_Date: Launch_Date = Launch_Date.replace(" Apr ", "-04-")
    if "May" in Launch_Date: Launch_Date = Launch_Date.replace(" May ", "-05-")
    if "Jun" in Launch_Date: Launch_Date = Launch_Date.replace(" Jun ", "-06-")
    if "Jul" in Launch_Date: Launch_Date = Launch_Date.replace(" Jul ", "-07-")
    if "Aug" in Launch_Date: Launch_Date = Launch_Date.replace(" Aug ", "-08-")
    if "Sep" in Launch_Date: Launch_Date = Launch_Date.replace(" Sep ", "-09-")
    if "Oct" in Launch_Date: Launch_Date = Launch_Date.replace(" Oct ", "-10-")
    if "Nov" in Launch_Date: Launch_Date = Launch_Date.replace(" Nov ", "-11-")
    if "Dec" in Launch_Date: Launch_Date = Launch_Date.replace(" Dec ", "-12-")
    if "- " in Launch_Date: Launch_Date = Launch_Date.replace("- ","-0")
    if ":" in Launch_Date: Launch_Date = Launch_Date[:-3]
    data1 = Launch_Date[:13]
    data2 = Launch_Date[13:]
    Launch_Date = data1 + ":" + data2
    if Launch_Date[len(Launch_Date)-1] == ":": Launch_Date = Launch_Date[:-1]

    if (Flight != Mission) and  (Flight != "-") and (Mission != "-"): 
      Flight = Flight + " / " + Mission
    
    if (Flight == "-"): Flight = Mission

    if Launch_Site == "NIIP-5": 
      Launch_Site = "Baikonur"
      if float(Launch_JD) < 2448254: ls_state = "SU"
      if float(Launch_JD) > 2448254: ls_state = "RU"
    if Launch_Site == "GIK-5": 
      Launch_Site = "Baikonur"
      if float(Launch_JD) < 2448254: ls_state = "SU"
      if float(Launch_JD) > 2448254: ls_state = "RU"
    if Launch_Site == "NIIP-53": 
      Launch_Site = "Plesetsk"
      if float(Launch_JD) < 2448254: ls_state = "SU"
      if float(Launch_JD) > 2448254: ls_state = "RU"        
    if Launch_Site == "GIK-1" or Launch_Site == "GNIIP": 
      Launch_Site = "Plesetsk"
      if float(Launch_JD) < 2448254: ls_state = "SU"
      if float(Launch_JD) > 2448254: ls_state = "RU"         
    if Launch_Site == "GNIIPV": 
      Launch_Site = "Plesetsk"
      if float(Launch_JD) < 2448254: ls_state = "SU"
      if float(Launch_JD) > 2448254: ls_state = "RU"            
    if Launch_Site == "V": Launch_Site = "VAFB"
    if Launch_Site == "VS": Launch_Site = "SVAFB"
    if Launch_Site == "MAHIA": Launch_Site = "Mahia"
    if Launch_Site == "WI" or Launch_Site == "WIMB": Launch_Site = "Wallops"
    if Launch_Site == "GTsP-4" or Launch_Site == "GTsMP-4": 
      Launch_Site = "Kapustin"
      if float(Launch_JD) < 2448254: ls_state = "SU"
      if float(Launch_JD) > 2448254: ls_state = "RU" 
    if Launch_Site == "KASC": Launch_Site = "Kagoshima"
    if Launch_Site == "USC": Launch_Site = "Kagoshima"
    if Launch_Site == "WOO": Launch_Site = "Woomera"
    if Launch_Site == "CSG": Launch_Site = "Kourou"
    if Launch_Site == "JQ": Launch_Site = "Jiuquan"
    if Launch_Site == "XSC": Launch_Site = "Xichang"
    if Launch_Site == "TNSC": Launch_Site = "Tanegashima"
    if Launch_Site == "PALB": Launch_Site = "Palmachim"
    if Launch_Site == "WEN": Launch_Site = "Wenchang"
    if Launch_Site == "TYSC": Launch_Site = "Taiyuan"
    if Launch_Site == "MARS": Launch_Site = "Wallops"
    if Launch_Site == "VOST": Launch_Site = "Vostochny"
    if Launch_Site == "PALB": Launch_Site = "Palmachim"
    if Launch_Site == "SHAR": Launch_Site = "Satish"
    if Launch_Site == "KLC": Launch_Site = "Kodiak"
    if Launch_Site == "SEM": Launch_Site = "Semnan"
    
    US_Locations = ["CC", "KSC","VAFB", "SVAFB", "Mahia", "Wallops", "NOTS", "PA", "SMLC", "EAFB", "GANC", "SPFL","KMR", "Kodiak", "KAU", "MHV"]
    AU_Locations = ["Woomera"]
    EU_Locations = ["Kourou", "HMG"]
    CN_Locations = ["Jiuquan","Xichang","Wenchang","Taiyuan","HHAI"]
    JP_Locations = ["Tanegashima","Kagoshima"]
    IL_Locations = ["Palmachim"]
    IN_Locations = ["Satish"]
    RU_Locations = ["GIK-2","BLA","KLA","YAS","Vostochny"]
    BR_Locations = ["ALCA"]
    KP_Locations = ["TONGH","SOHAE"]
    IR_Locations = ["Semnan","SHAHR"]
    KR_Locations = ["NARO"]

    if Launch_Site in US_Locations: ls_state = "US"
    if Launch_Site in AU_Locations: ls_state = "AU"
    if Launch_Site in EU_Locations: ls_state = "EU"
    if Launch_Site in CN_Locations: ls_state = "CN"
    if Launch_Site in JP_Locations: ls_state = "JP"
    if Launch_Site in IL_Locations: ls_state = "IL"
    if Launch_Site in IN_Locations: ls_state = "IN"
    if Launch_Site in RU_Locations: ls_state = "RU"
    if Launch_Site in BR_Locations: ls_state = "BR"
    if Launch_Site in KP_Locations: ls_state = "KP"
    if Launch_Site in IR_Locations: ls_state = "IR"
    if Launch_Site in KR_Locations: ls_state = "KR"

    print(Launch_Tag.ljust(11), Launch_Date.ljust(18), LV_Type.ljust(23), Flight_ID.ljust(20), Flight.ljust(46), ls_state+" ".ljust(3), Launch_Site.ljust(12), Launch_Pad.ljust(10), Launch_Code)

tsv_file.close()

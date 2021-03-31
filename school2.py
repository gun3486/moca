import requests

year = str(input("year : "))
month = str(input("month : "))
date = str(input("date : "))
SD_SCHUL_CODE = "7261028"
KEY = "376c66873c3845a485f42bc79baa29ce"
YMD = year+month+date
ATPT_OFCDC_SC_CODE = "D10"
url = "https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&KEY="+KEY+"&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE="+ATPT_OFCDC_SC_CODE+"&SD_SCHUL_CODE="+SD_SCHUL_CODE+"&MLSV_YMD="+YMD
res = requests.get(url).json()
data = res["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"].replace("<br/>","\n")
print(date)

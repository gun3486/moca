import requests, re, json, sys

try:
    officeCode=sys.argv[1] ## 교육청 코드
    schulCode=sys.argv[2] ## 학교 고유코드
    schulCrseCode=sys.argv[3] ## 학교 분류코드 (고등학교, 중학교, 초등학교)
    schulKndScCode="0" + str(sys.argv[3]) ## 학교 분류코드
    schYm=sys.argv[4]
except:
    print("""!!ERROR.... 
            코드 인자 값이 맞지 않거나 값이 이상합니다.
            제대로 된 코드 값을 입력해주십쇼""")
    sys.exit(1)


URL="https://" + officeCode + "/sts_sci_md00_001.do"
params = {'schulCode': str(schulCode), 'schulCrseScCode': str(schulCrseCode), 
'schulKndScCode' : str(schulKndScCode), 
'schYm' : str(schYm)}
response = requests.get(URL, params=params).text
data = response[response.find("<tbody>"):response.find("</tbody>")]
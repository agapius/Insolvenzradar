import re
regNo_pattern = "\d+((\w|.).(IN|IK).(\d+\/\d+))"

string = "2018-07-11Abbi, Isabell, Hamm, 254 IK 95/18"

regNo_raw_match = re.search(regNo_pattern, string)	
regNo = regNo_raw_match

print(regNo_raw_match)
print(regNo)

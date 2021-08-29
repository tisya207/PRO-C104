import csv
from collections import Counter
with open('height-weight.csv', newline='') as f:
    reader= csv.reader(f)
    data= list(reader)

data.pop(0)
newdata = []

for i in range(len(data)): 
    num= data[i][1]
    newdata.append(float(num))

filedata= Counter(newdata)
datarange = {
                        "50-60": 0,
                        "60-70": 0,
                        "70-80": 0
                    }
for height, occurence in filedata.items():
    if 50 < float(height) < 60:
        datarange["50-60"] += occurence
    elif 60 < float(height) < 70:
        datarange["60-70"] += occurence
    elif 70 < float(height) < 80:
        datarange["70-80"] += occurence

mode_range, mode_occurence = 0, 0
for range, occurence in datarange.items():
    if occurence > mode_occurence:
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"Mode is -> {mode:2f}")
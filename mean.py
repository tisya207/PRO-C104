import csv
with open('height-weight.csv', newline='') as f:
    reader= csv.reader(f)
    data= list(reader)

data.pop(0)
newdata = []

for i in range(len(data)): 
    num= data[i][1]
    newdata.append(float(num))

total=0
n= len(newdata)

for s in newdata:
    total+=s

mean=total/n 
print('mean(average) is -> ' + str(mean))
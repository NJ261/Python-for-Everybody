import re
x = open('C:\\Users\\Ignite - 4\\Desktop\\Pyton Coursera\\regex_sum_6304.txt','r') #give your file's path accordingly

finalValue = 0

for line in x.readlines():
    for value in re.findall('[0-9]+', line):
        finalValue += int(value)
x.close()
print(finalValue)
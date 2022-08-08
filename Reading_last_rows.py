## Python 3.9.13
## Reading last rows from Random.txt
## Count of rows you can enter by command line
import random
count=0
## Check is enter value digit
while count==0:
    count=input('Please, enter count of strings \n')
    if not count.isdigit():
        count=0
        print('Only digits is enterable')
r=open('Random.txt')
## Reading Random.txt
data = r.readlines()
l=len(data)
## Increasing number of rows if count of rows in Random.txt is low
if int(count)>l:
    count=str(l)
## Printing rows
for i in range(l-int(count),l):
    print(data[i].replace('\n', '').rstrip())
r.close()

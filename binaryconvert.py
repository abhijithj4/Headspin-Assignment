result=0
binnumber=list(input("Binary Number: "))
for i in range(len(binnumber)):
	temp=binnumber.pop()
	if temp=='1':
		result=result+pow(2,i)
print(result)
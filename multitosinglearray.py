def fun(num):
	new_list = []
	for i in num:
        	for j in i:
            	new_list.append(j)
	return new_list

print(fun(a))
l = 'karnataka'
d = {}
for each in l:
	if each in d:
		d[each] += 1
	else:
		d[each] = 1

k = [1, [1, 2, 3, 1], [1, 2, 4, float('nan'), 1, 3, 5], [2, 4, 6, None, 7, [5, 7, 9], [8, 9, 10]]]

flatList = list() 
def flattenList(originalList, flatList):
	for item in originalList:
		flattenList(item, flatList) if isinstance(item, (list, tuple)) else flatList.append(item)


flattenList(k, flatList)
print(flatList)
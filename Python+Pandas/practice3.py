predicted = [(1,4), (22,3), (3, 5), (10,20)]

original ={22:6, 1:4, 3:5}

print(original)
print(predicted[0])

s=[]
for i in predicted:
	s.append(i[0])
diff =0
n=0
for i in original:
	k=s.index(i)
	print(i, original[i], predicted[k][1])
	diff += abs(original[i] - predicted[k][1])
	n+=1
print(diff, n)


# print(s)
# print("\n\n", predicted.index((3,5)))




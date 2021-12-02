with open("day1_data", "r") as f:
	data_list = []
	for line in f.readlines():
		data_list.append(line.rstrip("\n"))
	del data_list[-1]
	#print(data_list)
	
	counter = 0
	counter_low = 0
	for i in range(0, len(data_list)-1):
		try:
			prev = int(data_list[i]) + int(data_list[i+1]) + int(data_list[i+2])
			next = int(data_list[i+1]) + int(data_list[i+2]) + int(data_list[i+3])
			print(prev, next)
			if next > prev:
				counter += 1
				print("increase")
			if next <= prev:
				counter_low += 1
				print("decrease")
		except:
			break
print("total number of data: ", len(data_list))
print("increasing: ", counter)
print("lower: ", counter_low)
	
	


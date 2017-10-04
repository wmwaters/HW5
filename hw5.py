import re
file = open('regex_sum_32323').read()
num_list = []
for line in file:
	small_list = []
	small_list = re.findall([0-9]+)
	for item in small_list:
		num_list.append(int(item))
print(sum(num_list))
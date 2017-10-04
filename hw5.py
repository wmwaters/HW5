import re
file = open('regex_sum_32323.txt').read()
small_list = []
num_list = []
small_list = re.findall('([0-9]+)',file)
for item in small_list:
	num_list.append(int(item))
print(sum(num_list))
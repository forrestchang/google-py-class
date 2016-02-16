import re
import sys

def read(filename):
	f = open(filename, 'r')
	text = f.read()
	f.close()
	return text

def find_all(text):
	pattern = r'<td>(\d+)</td>\s<td>(\w+)</td>\s<td>(\w+)</td>'
	match = re.findall(pattern, text)
	return match

def sort(match):
	male_list = []
	female_list = []
	result = []
	for i in range(1, 1001):
		male_list.append((i, match[i-1][1]))
		female_list.append((i, match[i-1][2]))
	result.append(male_list)
	result.append(female_list)
	return result

def write(filename, male_list, female_list):
	f = open(filename+'.summary', 'w')
	f.write(filename + '\n')
	for item in male_list:
		f.write(item[1] + ' ' + str(item[0]) + '\n')
	for item in female_list:
		f.write(item[1] + ' ' + str(item[0]) + '\n')
	f.close()

def main():
	for argv in sys.argv[1:]:
		text = read(argv)
		match = find_all(text)
		result = sort(match)
		write(argv, result[0], result[1])

if __name__ == '__main__':
	main()

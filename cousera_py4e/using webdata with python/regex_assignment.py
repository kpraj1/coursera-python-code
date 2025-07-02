import re

#handle = open('regex_sum_42.txt')
handle = open('regex_sum_2178605.txt')
sum = 0

for line in handle:
    line = line.rstrip()
    numbers = re.findall("\d+",line)
    if len(numbers) >=1:
        #for debugging how numbers are found
        #print(f"numbers:{numbers}")
        for num in numbers:
            sum = sum+int(num)
        #for debugging how their sum is calculated
        #print(f"sum is {sum}")
print(f"total sum is {sum}")
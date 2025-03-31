import re 
files = ['./diary\\2023-10-21.txt', './diary\\2023-10-22.txt', './diary\\2023-10-23.txt', './diary\\2023-10-24.txt', './diary\\2023-10-25.txt', './diary\\2023-10-26.txt', './diary\\2023-10-27.txt','./diary\\2023-10-21.txt', './diary\\2023-10-22.txt', './diary\\2023-10-23.txt', './diary\\2023-10-24.txt', './diary\\2023-10-25.txt', './diary\\2023-10-26.txt', './diary\\2023-10-27.txt']
for date in files:
    match = re.findall(r"\d{4}-\d{2}-\d{2}", date)
    
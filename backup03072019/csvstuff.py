import csv

# open the file in universal line ending mode 
with open('licenses.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

names = data['Drivers License']
count = 1

for number in names:
    if number.count("-") != 2 and len(number) != 17: names.remove(number)

for number in names:
    print('/html/body/app-root/div/app-enter-details/div/div[2]/table/tbody/tr[' + str(count) + ']/td[2]','      ',number)
    count+=1

print(names)
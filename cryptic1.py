import csv

file = csv.DictReader(open('/Users/omarchaudhry/documents/cryptic1.csv'))
result = {}

for row in file:
    result[row['word']] = row['abb']
    
while True:
  answer = input('Write a word and I will find its cryptic abbreviation ')
  abb = result.get(answer, 'sorry not in database')
  print(abb)
  
  
 




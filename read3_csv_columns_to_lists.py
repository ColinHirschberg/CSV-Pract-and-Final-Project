#Make use of the defaultdict
import csv
from collections import defaultdict(list)

with open('vowel_and_syllable_counts.txt') as f:
reader = csv.DictReader(f)
for row in reader:
  for(k,v) in row.items():
    columns[k].append(v)

print(columns['word'])
print(columns['vowels'])
print(columns['syllables'])
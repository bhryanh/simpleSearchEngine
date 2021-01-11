from classes.VectorCompare import VectorCompare
from classes.ReadTextFile import TextFile

v = VectorCompare()
f = TextFile()

documents = f.readFile('example.txt')
documents = f.splitByPhrases(documents)
documents = f.removeBlankLines(documents)
index = v.indexLines(documents)

searchterm = input('Enter Search Term: ')
matches = []

for i in range(len(index)):
  relation = v.relation(v.concordance(searchterm.lower()),index[i])
  if relation != 0:
    matches.append((relation,documents[i][:100]))

matches.sort(reverse=True)

for i in matches:
  print(i[0],i[1])
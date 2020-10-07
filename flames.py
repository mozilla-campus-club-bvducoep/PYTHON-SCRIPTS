from collections import Counter
a = input('Enter your name: ').lower().replace(' ','')
b = input('Enter your crush name: ').lower().replace(' ','')
c = []
d = []
for i in a:
  c.append(i)
for i in b:
  d.append(i)

c1 = Counter(c)
c2 = Counter(d)
d1 = list((c1 - c2).elements())
d2 = list((c2 - c1).elements())

n1 = len(d1)
n2 = len(d2)
relations = ['F','L','A','M','E','S']
flames = {
  'F':'Friend',
  'L':'Lover',
  'A':'Affection',
  'M':'Marriage',
  'E':'Enemy',
  'S':'Sister',
}
n = n1 + n2
match = True
while match:
  r = len(relations)
  if r < n:
    r3 = n % r
    if r3 == 0:
      r1 = r
    else:
      r1 = r3
  else:
    r1 = n
  relations.pop(r1-1)
  temp = [i for i in relations]
  relations.clear()
  if (r1-1) == 0 or (r1-1) == len(temp):
    relations = temp
  else:
    for i in range((r1-1),len(temp)):
      relations.append(temp[i])
    for i in range(0,(r1-1)):
      relations.append(temp[i])
  print(relations)
  if len(relations) == 1:
    match = False
 
print(f'Relation with your crush is: {flames[relations[0]]}')

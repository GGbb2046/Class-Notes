import shelve
pets = ['Fluffy', 'Pookems', 'Killa']
e2f = {1:"un", 2:"deux", 3:"trois"}

with shelve.open('mydata.dat') as shelfie:
  shelfie['pets'] = pets
  shelfie['english to french'] = e2f


with shelve.open('mydata.dat') as shelfie:
  print("keys --->",list(shelfie.keys()))
  print("values ->", list(shelfie.values()))

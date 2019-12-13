myList=['burger','soda','onion_rings','fries','pie']
print myList
print myList.index('fries')
print myList.count('fries')

print

myList=['burger','soda','onion_rings','fries','pie']
newList=myList.append('milkshakes')
print myList
print newList

print

item=myList.pop()
print myList
print item

print

myList.extend('milkshakes')
print myList

print

myList=['burger','soda','onion_rings','fries','pie']
myList.insert(2,'hotdogs')
print myList

print

myList.remove('fries')
print myList

# IS AN ERROR->myList.remove('bagel')

print

myList=['burger','soda','onion_rings','fries','pie']
myList.sort()
print myList

print

myList=['burger','soda','onion_rings','fries','pie']
new_List=sorted(myList)
print myList
print new_List


myList=['burger','soda','onion_rings','fries','pie']
new_List=myList.reverse()
print myList
print new_List

myList=[]
word='LottaBurger'
myList.extend('LottaBurger')
new_word=':'.join(myList)
base_word=''.join(myList)

print word
print myList
print new_word
print base_word



raw_input('Done')
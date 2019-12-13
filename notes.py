print "Dictionaries"
print
d1={'Rangers':'No 1','Yankees':'FAIL','Giants':'Go Home','Astros':'Next Time','Phillies':'Stay Home'}
print d1
print
print sorted(d1)
print
print d1.keys()
print d1.values()
print d1.items()
print
for key in d1:
    print ("%s are made of %s"%(key,d1[key]))
print
d1['Yankees']="Don't even try"#can sub but not add or extend
print d1
print
print "EOF"
print 
print "Sets"
print
setA=set([1,3,5,7,9])
setB=set([1,2,4,8,16])
print setA
print
print setA.intersection(setB)
print
print setA.union(setB)
print
print setA.difference(setB)
print
print setA.issuperset(setB)
print
print setA.issubset(setB)
print
print setB.union(setA).issuperset(setB)
print 
print "EOF"

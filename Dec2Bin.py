dString = raw_input("Enter the decimal number to convert:")
d = int(dString)
# a recursive dec to bin function
d2b = lambda d: (not isinstance(d,int) or (d==0)) and '0' \
or (d2b(d//2)+str(d%2))
print(d2b(d))
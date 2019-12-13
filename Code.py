#Encode

encode={'b':'a','B':'A','c':'e','C':'E','d':'i','D':'I','f':'o','F':'O','g':'u','G':'U','h':'b','H':'B','j':'c','J':'C','k':'d','K':'D','l':'f','L':'F','m':'g','M':'G','n':'h','N':'H','p':'j','P':'J','q':'k','Q':'K','r':'l','R':'L','s':'m','S':'M','t':'n','T':'N','v':'p','V':'P','w':'q','W':'Q','x':'r','X':'R','y':'s','Y':'S','Z':'t','z':'T','a':'v','A':'V','e':'w','E':'W','i':'x','I':'X','o':'y','O':'Y','u':'Z','U':'z',' ':' ','!':'!'}

def encoder (myString):
    global encode
    result=''
    for letter in myString:
        result=result+encode[letter]
    return result

def doEncode ():
    message=raw_input("Please enter your message/secret:")
    secret=encoder(message)
    print secret 
    return

encoder
doEncode


#for Decode; dictionary is backwards. Code same.
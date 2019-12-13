import math
def ConvDecToBaseVar(num):
     base= 2
     if base > 10 or base < 2:
          raise ValueError, 'The base number must be between 2 and 10.'
     if num == 0: return 0
     ans = ''
     while num != 0:
          num, rem = divmod(num, base)
          ans =  str(rem)+ans
     return int(ans)
print ConvDecToBaseVar(3000)
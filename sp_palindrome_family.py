def palin(string):
    reverse = ''.join(reversed(st))
    if(string == reversed):
      return True

t = int(input())
for test in range(t):

    s = input()
    
    os = ''
    for i in range(0,len(s),2):
        os += s[i]
        
    es = ''
    for i in range(1,len(s),2):
        es += s[i]
        
    isodd = palin(os)
    iseven = palin(es)
    
    if palin(s):
        print('PARENT')
    
    elif isodd and iseven:
        print('TWIN')
    elif iseven:
        print('EVEN')
    elif isodd:
        print('ODD')
    else:
        print('ALIEN')

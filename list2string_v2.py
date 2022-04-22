#refactor goal: remove special case if-else codes.
#


#function that returns a list value into a string separated by comma & 'and' list[-1]


#str( str(val[0])+", "+str(val[1])+", "+str(val[2])+", "+....+"and "+str(val[-1]) )

def commaCode(val): #function code, given val to be a list
    if val == []:           #if empty list (special case 1)
        return None
    else:                   #list w/ more than 2 value
        r = str(val[0])      #set string to first list value 
        for i in range(1,len(val)):
            if i == len(val)-1:
                r += " and "+val[i]
            else:
                r += " "+str(val[i])+","
        return r

#sample val list & print out, to be commented out
val = [1,2,3,'cat','$']
print(val)
print(commaCode(val))
print("val = []")
print(commaCode([]))
print("val = [1,'cat']")
print(commaCode([1,'cat']))
print("val = ['cat']")
print(commaCode(['cat']))

#what if there's val = [],
#what if only 1 value, val = ['one']

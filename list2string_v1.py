#function that returns a list value into a string separated by comma & 'and' list[-1]


#str( str(val[0])+", "+str(val[1])+", "+str(val[2])+", "+....+"and "+str(val[-1]) )

def commaCode(val): #function code, given val to be a list
    if val == []:           #if empty list (special case 1)
        return None
    elif len(val) == 1:       #if only 1 value in list, loop wouldn't work (special case 2)
        return str(val[0])
    elif len(val)==2:           #if only 2 values in list
        return str(val[0])+" and "+str(val[1])
    else:                   #list w/ more than 2 value
        r = ""
        for i in range(len(val)-1):
            r += str(val[i])+", "
        r += "and "+val[-1]
        return r

#sample val list & print out, to be commented out
val = [1,2,3,'cat','$']
print(val)
print(commaCode(val))
print("val = []")
print(commaCode([]))
print("val = [1,'cat']")
print(commaCode([1,'cat']))

#what if there's val = [],
#what if only 1 value, val = ['one']

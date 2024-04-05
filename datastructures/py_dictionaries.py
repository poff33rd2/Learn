#Dictionary: optimized to retreive values based on keys and not an index like a list.
#faster and more flexible than lists
# Key : Value pair -> can go straight to value using a key
#Keys can be a string or int
#values can be string or int
#dictionaries don't take duplicate keys and will show only the latest key of the duplicate

sampledict = {1: 'Coffee', 'Favorite': 'Chai', 3: 'Acai Bowl'}

# print(sampledict[1]) #prints 'Coffee'
# print(sampledict) #prints the entire dictionary
# print(sampledict['Favorite']) #prints 'chai'
# sampledict[2] = 'Mint Tea' #changes key 2 into 'Mint Tea'
# sampledict[2] = 'Ice Cream' #adds key of 2 and a value of 'Ice Cream'
# del sampledict[1] #deletes key 1 and its value

# print(sampledict)

# for x in sampledict:
#     print(x) # only prints the keys


for key, value in sampledict.items(): #prints the key and its value as type string for the key.
    print(str(key) + ' : ' + value) #the key has to be wrapped in str or int because concatonation values need to be the same.
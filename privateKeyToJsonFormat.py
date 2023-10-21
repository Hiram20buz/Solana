import base58
a = [i for i in base58.b58decode('you private key')]
print(a)

'''
Run the script and save the array into a file key.json
print(a) will return an array save it into a json file.
Also import base58.
'''

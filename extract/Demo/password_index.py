password_index = {
     'Account 1' : {'Username': 'mrbooleanswag',
        'Password': 'askjdkljfgsdfg'},
     'Account 2' : {'Username': 'Lexington',
        'Password': 'kfsdjgfdg'},
     'Account 3': {'Username': 'Gerard',
        'Password': 'lkihfaksd'}
        
}
print(password_index)
print ("The current list of accounts has %s accounts in it." % (len(password_index)))

unpack = {**password_index}
print(unpack)
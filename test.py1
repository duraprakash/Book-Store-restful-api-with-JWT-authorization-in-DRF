# loop through nested dict in python

address = {'street':'vyas-2', 'city':'damauli'}
user = {'username':'uname', 'password':'ppassword', 'address': address}

address = user.pop('address',None)
for key,value in user.items():
    print(f'{key}: {value}')
    # # get the address key and value inside user
    # if isinstance(value, dict):
    #     for inner_key, inner_value in value.items():
    #         print(f'{inner_key}: {inner_value}')
    
# # get the address key and value escaping the user
# for key,value in user.items():
#     if isinstance(value, dict):
#         for inner_key, inner_value in value.items():
#             print(f'{inner_key}: {inner_value}')

# get the address key and value
if address:
    for key,value in address.items():
        print(f'{key}: {value}')
        
user['address'] = address

print("User:")
for key, value in user.items():
    if isinstance(value, dict):
        print(f"  {key}:")
        for inner_key, inner_value in value.items():
            print(f"    {inner_key}: {inner_value}")
    else:
        print(f"  {key}: {value}")
        


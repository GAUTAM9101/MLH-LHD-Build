cricketers = [
    {'Name': 'Sachin Tendulkar', 'age': 47},
    {'Name': 'M.S. Dhoni', 'age': 39},
    {'Name': 'Virat', 'age': 32},
    {'Name': 'Yuvraj', 'age': 39},
]

def get_name(cricketers):
    return cricketers.get('Name')


def get_age(cricketers):
    return cricketers.get('age')



# sort by name (Ascending order)
cricketers.sort(key=get_name)
print(cricketers, end='\n\n')

# sort by Age (Ascending order)
cricketers.sort(key=get_age)
print(cricketers, end='\n\n')

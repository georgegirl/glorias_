from datetime import datetime
import string
import random


def generate_order_id():
    ''' this function generates random ids with the data and certain strings'''
    rand_str= [random.choice(string.ascii_letters)for _ in range(4)]
    code= "".join(rand_str)
    today = datetime.now()
    return today.strftime(f'%d%m%y- {code}')


print(generate_order_id())

# print(string.ascii_letters)

# today=datetime.now()

# w = today.isoformat()
# d ={"f": datetime.fromisoformat(w)}
# print(d)
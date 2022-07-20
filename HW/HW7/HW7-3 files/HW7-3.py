import pickle
from operator import itemgetter
import dill


class User:
    def __init__(self, id, firs_name, last_name, phone):
        self.id = id
        self.first_name = firs_name
        self.last_name = last_name
        self.phone = phone

    def __repr__(self) -> str:
        return f"{self.id}:{self.first_name}{self.last_name} <{self.phone}>"

    # Defining new method full name which concatenates first name to last name
    def fullname(self) -> str:
        return f"{self.first_name} {self.last_name}"


# Unpickling
with open("users.pickled", 'rb') as f:
    unpickled = pickle.load(f)
print(unpickled)
# sorting by id. which is converting the objects to str and
# storing it as dictionary to sort
lst = list(map(str, unpickled))
res_dict = {}
for i in lst:
    k, v = i.split(':')
    res_dict[int(k)] = v
result = sorted(res_dict.items(), key=itemgetter(0))
out = {k: v for k, v in result}

# opening file to save the sorted dictionary
with open("output-q-3-1.txt", 'w') as f:
    for k in out:
        f.write(f'{k}:{out[k]}' + '\n')

# filtering users by phone numbers that has 0919 in it.
ans = [i.split() for i in lst]
res2 = [' '.join(j) + '\n' for j in ans if j[1].startswith('<0919')]

# saving the filtered users
with open("output-q-3-2.txt", 'w') as f:
    f.writelines(res2)

# using dill to dill the users and save them in the file
new_list = [i.fullname() for i in unpickled]
with open("output-q-3-3.dill", 'wb') as f:
    dill.dump(new_list, f)

# with open("output-q-3-3.dill", 'rb') as f:
#     print(dill.load(f))

import pickle
class User:
    pass


def save_pickle(obj, filename):
    with open(filename, 'ab') as file:
        pickle.dump(obj, file=file)

def load_all(filename='users.pickle'):
    with open(filename, "rb") as f:
        while True:
            try:
                yield pickle.load(f)
            except EOFError:
                break
u1 = User()
u2 = User()

# save_pickle(obj=u1, filename='users.pickle')
# save_pickle(obj=u2, filename='users.pickle')

print(list(load_all()))
# for i in load_all():
#     print(i)
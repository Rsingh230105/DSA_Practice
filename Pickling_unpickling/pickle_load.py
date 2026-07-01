import pickle

with open('person.pkl','rb') as f:
    p = pickle.load(f)

p.display_info()
import pickle
from person import Person

p = Person("Ram",18)


with open('person.pkl','wb') as f:
    pickle.dump(p,f)
    
print("Person object saved successfully!")
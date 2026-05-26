import pickle

with open('label_classes.pkl', 'rb') as f:
    data = pickle.load(f)

print(type(data))
print(data)

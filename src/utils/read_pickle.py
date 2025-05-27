import pickle

# Replace with your pickle file path
pickle_file = '/predictions/depth_new.pkl'

with open(pickle_file, 'rb') as f:
    data = pickle.load(f)

print(data)


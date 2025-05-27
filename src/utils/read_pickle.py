import pickle
import os
# Replace with your pickle file path
pickle_file = 'predictions/depth_new.pkl'
path = os.path.join(os.path.dirname(os.getcwd()), pickle_file)
print(f"reading pickle file in path: {path}")
with open(path, 'rb') as f:
    data = pickle.load(f)

print(data)


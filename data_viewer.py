import pickle

with open("data_store.pkl", "rb") as file:

    website_data = pickle.load(file)

context = website_data.get("context", "")

print("\nWebsite Data Preview:\n")

print(context[:2000])
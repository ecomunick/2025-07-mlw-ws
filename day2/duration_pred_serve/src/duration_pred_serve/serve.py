import pickle

model_path = "./models/2022-01.pkl"
with open(model_path, "rb") as f_in:
    model = pickle.load(f_in)
    
trip = {
    "PULocationID": "43",
    "DOLocationID": "238",
    "trip_distance": 1.16,
    
}

prediction = model.predict(trip)
print(prediction[0])

# run to test if it works: uv run python src/duration_pred_serve/serve.py 
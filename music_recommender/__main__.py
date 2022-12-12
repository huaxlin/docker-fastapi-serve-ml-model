import sys
import json
from music_recommender.predict import predict

row=json.loads(list(sys.stdin)[0])
print(f'{predict(row) = }')

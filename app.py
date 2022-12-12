from fastapi import FastAPI

from music_recommender.predict import predict

app = FastAPI()


@app.get("/health", response_model=str)
def read_root():
    return 'ok'


@app.post("/predict", response_model=dict)
def predict_handler(body: dict):
    ret = predict(body)
    return ret


if __name__ == "__main__":
    # debugging mode
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")

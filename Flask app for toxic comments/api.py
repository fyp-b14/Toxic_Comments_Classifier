from fastapi import FastAPI
from pydantic import BaseModel
from detoxify import Detoxify

app = FastAPI()


class Request(BaseModel):
    text: str


class Response(BaseModel):
    Result: str
    Developer_metric: dict


@app.get("/")
def root():
    return {"message": "API running"}


@app.post("/model/predict")
def predict(body: Request):
    text = body.text

    res = Detoxify('original').predict([text])
    Output = "Not Hateful"
    for key in res:
        for i in res[key]:
            if i > 0.5:
                Output= "Hateful"

    return Response(
        Result=Output,
        Developer_metric=res
    )

from fastapi import FastAPI


from typing import Union


app = FastAPI()


@app.get("/")
def home():
    return {"123": "456"}

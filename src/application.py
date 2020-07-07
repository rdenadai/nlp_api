from fastapi import FastAPI
from utils import parser


app = FastAPI()


@app.get("/")
def index():
    return {"Working": True}


@app.post("/parser/")
def parser_phrase(phrase: str):
    return parser(phrase)

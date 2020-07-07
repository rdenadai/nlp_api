from fastapi import FastAPI
from utils import parser


app = FastAPI()


@app.get("/")
async def index():
    return {"Working": True}


@app.post("/parser/")
async def parser_phrase(phrase: str):
    return parser(phrase)

from fastapi import FastAPI, Body, status
from fastapi.responses import JSONResponse
from tools.funcs.add import addNew
from datetime import datetime
from tools.parseCsv import listData
from tools.funcs.getMark import getMarkById
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Hello"},
    )


@app.get("/doc/{item_id}")
def read_item(item_id: int):
    return getMarkById(item_id)


@app.post("/add")
def addOne(url: str = Body(...)):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    return addNew(url, date_str)


@app.post("/addsome")
def addSome(urls: list[str] = Body(...)):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    return {"results": [addNew(el, date_str) for el in urls]}


@app.get("/getAll")
def getAll():
    return listData()

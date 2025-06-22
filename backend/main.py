from fastapi import FastAPI, status, Request
from fastapi.responses import JSONResponse
from tools.funcs.add import addNew


app = FastAPI()


@app.get("/")
def read_root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "Hello"},
    )


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}


@app.post("/add")
def add(link):

    return addNew(link)["description"]

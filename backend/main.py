from fastapi import FastAPI, Body, status
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
def addOne(url: str = Body(...)):
    return addNew(url)


@app.post("/addsome")
def addSome(urls: list[str] = Body(...)):
    return {"results": [addNew(el) for el in urls]}

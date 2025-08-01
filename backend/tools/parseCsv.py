import pandas as pd
from pathlib import Path

documents_path = Path.home() / "Documents"


def createCSV(columns: list):
    global documents_path
    df = pd.DataFrame({col: [] for col in columns})
    Path(f"{documents_path}/noter").mkdir(parents=True, exist_ok=True)
    output_path = documents_path / "noter/dataframe.csv"
    df.to_csv(output_path, index=False)


def pushOne(data: list, columns: list):
    path = documents_path / "noter/dataframe.csv"
    if not path.exists():

        createCSV(columns)
    df = pd.read_csv(path)
    new_row = pd.DataFrame([data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(path, index=False)
    return "OK"


# def parseExitingCSV():
#     pd.read_csv(),
def listData():
    path = documents_path / "noter/dataframe.csv"
    if path.exists():
        df = pd.read_csv(path)
        return df[["title", "company", "timeago", "id"]].to_dict(orient="records")
    else:
        return "No records"


# readCsv(Path(f"{documents_path}/noter/dataframe.csv"))
# pushOne(["aboba", "https://aboba.com", "05.05.2025"])
# print(listData(documents_path / "noter/dataframe.csv"))

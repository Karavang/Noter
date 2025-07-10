import pandas as pd
from pathlib import Path

documents_path = Path.home() / "Documents"


def createCSV(columns: list):
    global documents_path
    df = pd.DataFrame({col: [] for col in columns})
    Path(f"{documents_path}/noter").mkdir(parents=True, exist_ok=True)
    output_path = documents_path / "noter/dataframe.csv"
    df.to_csv(output_path, index=False)


def pushOne(data: list):
    path = documents_path / "noter/dataframe.csv"
    df = pd.read_csv(path)
    print(df)
    new_row = pd.DataFrame([data], columns=df.columns)
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(path, index=False)


# def parseExitingCSV():
#     pd.read_csv(),
def readCsv(path: Path):
    df = pd.read_csv(path)
    return df


# readCsv(Path(f"{documents_path}/noter/dataframe.csv"))
# pushOne(["aboba", "https://aboba.com", "05.05.2025"])
createCSV(["title", "company", "loc", "timeago", "description", "lvl"])

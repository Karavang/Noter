import requests
from bs4 import BeautifulSoup


def addOneDj(id: str, timeago: str):
    print(id)
    url = f"https://djinni.co/jobs/{id}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = {}
    try:
        data["title"] = (
            soup.find("h1", {"class": "d-flex align-items-center flex-wrap"})
            .find("span")
            .get_text(strip=True)
        )
        data["company"] = soup.find("a", {"class": "text-reset"}).get_text(strip=True)

        data["timeago"] = timeago
        data["id"] = id
        return data

    except Exception as e:
        return {"error": str(e)}


# if __name__ == "__main__":
#     data = input("data: ").split(" ")
#     print(data)
#     print(addOneDj(data[0], data[1]))

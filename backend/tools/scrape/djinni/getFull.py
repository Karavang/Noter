import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def getFullDj(id: str):
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

        data["loc"] = soup.find("span", {"class": "location-text"}).get_text(strip=True)
        data["description"] = md(
            soup.find("div", {"class": "job-post__description"}).get_text(
                separator="\n"
            )
        )

        data["lvl"] = soup.find("span", {"class": "description__job-criteria-text"})
        return data

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    data = input("data: ").split(" ")

    print(getFullDj(data[0]))

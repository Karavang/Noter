import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def addOneLn(id: str, timeago: str):
    url = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{id}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = {}
    try:
        data["title"] = soup.find("h2", {"class": "top-card-layout__title"}).get_text(
            strip=True
        )
        data["company"] = soup.find(
            "a", {"data-tracking-control-name": "public_jobs_topcard-org-name"}
        ).get_text(strip=True)

        data["timeago"] = timeago
        data["id"] = id
        return data

    except:
        return "Something went wrong with scraping"


# print(lnParse(argv[1]))

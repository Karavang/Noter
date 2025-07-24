import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def getFullLn(id: str):
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
        data["loc"] = soup.find("span", {"class": "topcard__flavor--bullet"}).get_text(
            strip=True
        )
        data["description"] = md(
            str(soup.find("div", {"class": "show-more-less-html__markup"}))
        )
        data["lvl"] = soup.find(
            "span", {"class": "description__job-criteria-text"}
        ).get_text(strip=True)
        return data

    except:
        return "Something went wrong with scraping"


# print(lnParse(argv[1]))

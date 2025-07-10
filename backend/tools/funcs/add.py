from tools.scrape.lnkdn import lnParse
from tools.parseCsv import pushOne


def addNew(link):
    if "linkedin.com" in link:
        if "/jobs/view/" in link:
            parts = link.split("/jobs/view/")
            id_part = parts[1].split("/")[0]
            data_dict = lnParse(id_part)
            data = list(data_dict.values()) if isinstance(data_dict, dict) else []

            return pushOne(data) if id_part.isdigit() else "Link is not valid"
    return "Link is not valid"

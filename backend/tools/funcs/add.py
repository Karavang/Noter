from tools.scrape.lnkdn import lnParse


def addNew(link):
    if "linkedin.com" in link:
        if "/jobs/view/" in link:
            parts = link.split("/jobs/view/")
            id_part = parts[1].split("/")[0]
            return lnParse(id_part) if id_part.isdigit() else "Link is not valid"
    return "Link is not valid"

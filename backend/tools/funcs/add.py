from backend.tools.scrape.lnkdn.addOne import addOneLn
from backend.tools.parseCsv import pushOne


def addNew(link, timeago):
    if "linkedin.com" in link:
        if "/jobs/view/" in link:
            parts = link.split("/jobs/view/")
            id_part = parts[1].split("/")[0]
            try:
                data_dict = addOneLn(id_part, timeago)
                print(data_dict)
                data = list(data_dict.values()) if isinstance(data_dict, dict) else []
                return (
                    pushOne(data, data_dict.keys())
                    if id_part.isdigit()
                    else "Link is not valid"
                )
            except:
                return "Link is not valid or not valid"

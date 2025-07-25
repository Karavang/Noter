from backend.tools.scrape.lnkdn.getFull import getFullLn


def getMarkById(id):
    data = getFullLn(id)
    if not isinstance(data, dict):
        return "Something went wrong with scraping"
    return f"""
# {data["title"]}

### {data["company"]} |  {data["loc"]} |  {data["lvl"]}

{data["description"]}
"""

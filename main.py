from scraper import Scraper

# TODO: 
# 1. pass the file as argument
# 2. add validation for file extension
file = "sample.xlsx"

sc = Scraper(file)

print(sc.active_sheet().title)
print(sc.get_violations())
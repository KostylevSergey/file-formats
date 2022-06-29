import sys

# чтение XML
# https://docs.python.org/3/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
# # если будет проблема с кодировкой, сначала нужно создать парсер и явно задать кодировку файла
# tree = ET.parse("files/newsafr.xml")
parser = ET.XMLParser(encoding="utf-8")
# # подставляем парсер при разборе xml
tree = ET.parse("files/newsafr.xml", parser)

xml_root = tree.getroot()
print(xml_root)
print(xml_root.tag)
print(xml_root.text)
print(xml_root.attrib)

titles_list = xml_root.findall("channel/item/title")
print(len(titles_list))
item = xml_root.find("channel/item")
print(item.tag)	
print(item.attrib)
# for title in titles_list:
# 	print(title.text)

sys.exit()

import json
from pprint import pprint

with open("files/newsafr.json") as f:
	json_data = json.load(f)
# print(json_data)
# for news in json_data["rss"]["channel"]["items"]:
# 	print(news["title"])
# print(f'Всего у нас {len(json_data["rss"]["channel"]["items"])} новостей')

pprint(json_data["rss"]["channel"]["items"][0])

# with open("files/newsafr2.json", "w") as f:
# 	json.dump(json_data, f, ensure_ascii=False, indent=4)
# unicode decode error

sys.exit()


import csv

news_count = 0
with open("files/newsafr.csv") as f:
	reader = csv.reader(f)
	# reader = csv.DictReader(f)
	# for row in reader:
	# 	print(row[-1], type(row))
	# 	news_count += 1
	news_list = list(reader)
	# for row in reader:
	# 	print(row["title"], type(row))
	# 	news_count += 1
		# print(row, type(row))
	
# news_count -= 1
# print(f"Всего {news_count} статей")

header = news_list.pop(0)
print(news_list[:3])
print(f"Всего {len(news_list)} статей")
print(header)

csv.register_dialect("customcsv", delimiter=",", quoting=csv.QUOTE_NONE, escapechar="\\")

with open("files/newsafr2.csv", "w") as f:
	writer = csv.writer(f, "customcsv")
	writer.writerow(header)
	# writer.writerow(["hello"])
	writer.writerows(news_list[:3])

with open("files/newsafr2.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerows(news_list[3:])
		





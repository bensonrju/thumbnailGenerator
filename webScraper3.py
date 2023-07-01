from html.parser import HTMLParser
import pandas
import math

myFrame = pandas.read_csv('electrical_budget2.csv')

URLs = []

for element in myFrame['URL (if avalilable)']:
    if str(element) != 'nan':
        URLs.append(element)

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if (tag == 'meta'):
            for targetAttr in attrs:
                if (targetAttr[1] == 'og:image'):
                    for targetTuple in attrs:
                        if (targetTuple[0] == 'content'):
                            print("src: ", targetTuple[1])
            
        return super().handle_starttag(tag, attrs)
    
    def handle_endtag(self, tag: str) -> None:
        return super().handle_endtag(tag)
    
    def handle_data(self, data: str) -> None:
        return super().handle_data(data)
    
myParser = MyHTMLParser()

with open('sampleHead.txt', encoding="utf8") as fin:
    contents = fin.read()

myParser.feed(contents)
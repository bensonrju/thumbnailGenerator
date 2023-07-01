from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        #print("Encountered a start tag:", tag)
        """
        if(tag == "img"):
            print(attrs)
            for targetAttr in attrs:
                if (targetAttr[0] == 'src'):
                    print("Image Source: ", targetAttr[1])
        """
        if (tag == 'meta'):
            #print('Meta tag: ', attrs)
            
            for targetAttr in attrs:
                if (targetAttr[1] == 'og:image'):
                    for targetTuple in attrs:
                        if (targetTuple[0] == 'content'):
                            print("src: ", targetTuple[1])
            
        return super().handle_starttag(tag, attrs)
    
    def handle_endtag(self, tag: str) -> None:
        #print("Encountered an end tag:", tag)
        return super().handle_endtag(tag)
    
    def handle_data(self, data: str) -> None:
        #print("Encountered some data: ", data)
        return super().handle_data(data)
    
myParser = MyHTMLParser()

with open('sampleHead.txt', encoding="utf8") as fin:
    contents = fin.read()

myParser.feed(contents)
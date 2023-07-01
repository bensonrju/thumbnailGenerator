from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print("Encountered a start tag:", tag)
        if(tag == "img"):
            for targetAttr in attrs:
                if (targetAttr[0] == 'src'):
                    print("Image Source: ", targetAttr[1])
        return super().handle_starttag(tag, attrs)
    
    def handle_endtag(self, tag: str) -> None:
        print("Encountered an end tag:", tag)
        return super().handle_endtag(tag)
    
    def handle_data(self, data: str) -> None:
        print("Encountered some data: ", data)
        return super().handle_data(data)
    
myParser = MyHTMLParser()
myParser.feed('<html><head><title>Test</title></head>'
            """<body>
            <img src="/web/20050202181140im_/http://www.google.com/images/logo.gif" alt="Google" width="276" height="110">
            <h1>Parse me!</h1></body></html>""")
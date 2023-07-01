"""
with open('samplePage.txt', encoding="utf8") as fin:
    line = fin.readline()
    print(line)
    while line:
        line = fin.readline()
        print(line)
"""

with open('samplePage.txt', encoding="utf8") as fin:
    contents = fin.read()


with open('sampleOutput.txt', 'w', encoding="utf8") as fout:
    fout.write(contents)

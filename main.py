import pdfParse, jsonDump, sys#, charts

while True:
    a = int(input('Select option:\n'
                  '0 - Download PDFs\n'
                  '1 - Parse PDFs\n'
                  '2 - Charts\n'
                  '3 - Exit\n'))
    if a == 0:
        pdfParse.option()
    if a == 1:
        jsonDump.choice()
    if a == 3:
        sys.exit()

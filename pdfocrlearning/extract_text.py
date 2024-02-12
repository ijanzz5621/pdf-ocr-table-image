import re
from pdfminer.high_level import extract_pages, extract_text

def start():
    
    for page_layout in extract_pages("data/sample.pdf"):
        for element in page_layout:
            print(element)
            
            
    text = extract_text("data/sample.pdf")
    print(text)
    
    #pattern = re.compile(r"[a-zA-Z]+,{1}\s{1}")
    # using look ahead (?=) to find names (ahead must have 1 comma and 1 space)
    pattern = re.compile(r"[a-zA-Z]+(?=,{1}\s{1})")
    
    matches = pattern.findall(text)
    print(matches)
    
    for name in matches:
        print(name)
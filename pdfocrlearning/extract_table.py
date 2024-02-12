import tabula

#import warnings
#warnings.simplefilter(action='ignore', category=FutureWarning)

def start():
    print("Extract table from PDF")
    
    tables = tabula.read_pdf("data/sample.pdf", pages="all")
    
    for table in tables:
        print(table.head())
        print(table.columns)
        
        # filter
        print(table[table.Age > 30])
    
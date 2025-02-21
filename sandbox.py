from numpy import random

    
    
def make_gene():
    gene = []
    #assume 64 entriesof code
    n = random.randint(0,3)
    if n == 0:
        print("0")
    else:
        print("1")
        
make_gene() to 
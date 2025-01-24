def make_gene():
    gene = []
    #assume 64 entriesof code
    entries = 64
    while len(gene) < entries:

        if n == 0:
            gene.append("A")
        elif n == 1:
            gene.append("C")
        elif n == 2:
            gene.append("G")
        elif n == 3:
            gene.append("T")
        
    print(gene)

make_gene()
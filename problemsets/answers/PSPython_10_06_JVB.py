class Sequence(object):
    def __init__(self, name=None, organism=None, sequence=None):
        self.name = name
        self.organism = organism
        self.sequence = sequence


    def length(self):
        if self.sequence is None:
            return 0
        else:
            return len(self.sequence)


    def composition(self, counts=False):
        comp = {}
        for nt in self.sequence:
            if nt in comp:
                comp[nt] += 1
            else:
                comp[nt]  = 1

        if counts:
            return comp
        else:   
            return { nt: float(comp[nt]) / self.length() for nt in comp }

        
    def gc_content(self):
        comp = self.composition(counts=True)
        return float(comp['G']+comp['C']) / self.length()

    
if __name__ == '__main__':
    gene = Sequence("yfg","Mola mola","ATGATGCTGACGTACGTAGCTGACGGACTTCTGCGGCTATAG")

    # attributes are variables bound to an object, no parenthases necessary
    print("Gene Name:", gene.name)  
    print("Organism:", gene.organism)
    print("Sequence:", gene.sequence)
    # methods are functions bound to a object, so we must use parenthases
    print("Length:", gene.length())
    print("Composition:", str(gene.composition()))
    print("GC content", gene.gc_content())

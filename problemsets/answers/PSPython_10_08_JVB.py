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
        for nt in self.sequence.upper():
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


    def format_fasta(self, width=60):
        if self.length() < 1:
            raise Exception("Sequence has length of zero")
        else:
            organism = ''
            if self.organism is not None:
                organism = str(self.organism)

            folded = ''
            for start in range(0, self.length(), width):
                if start+width > self.length():
                    folded += self.sequence[start:start+width]
                else:
                    folded += self.sequence[start:start+width] + '\n'
            
            return ">{}{}\n{}".format(self.name, organism, folded)


    def same_as(self, other):
        if self.name != other.name:
            return False
        if self.organism != other.organism:
            return False
        if self.sequence != other.sequence:
            return False
        return True
    
        
if __name__ == '__main__':
    gene1 = Sequence("yfg","Mola mola","ATGATGCTGACGTACGTAGCTGACGGACTTCTGCGGCTATAGCGAGCGTACTCGACACACATCGATCGATGCAGCTATGCTAGCAGCTAG")
    gene2 = Sequence("gfp","Mola mola","ATGGTACGTACAGCTAGCAGCTAGCTATTTATATATCGGCGCGATTCGATCGATCGATCTCTCGCGCGATTAGCGTACGTACTGACGTACGTACT")
    # attributes are variables bound to an object, no parenthases necessary
    print("Gene Name:", gene1.name)  
    print("Organism:", gene1.organism)
    print("Sequence:", gene1.sequence)
    # methods are functions bound to a object, so we must use parenthases
    print("Length:", gene1.length())
    print("Composition:", str(gene1.composition()))
    print("GC content", gene1.gc_content())
    print("Fasta record:")
    print(gene1.format_fasta())

    for gene in (gene1, gene2):
        if gene1.same_as(gene):
            print("The genes are the same ({} == {})".format(gene1.name, gene.name))
        else:
            print("The genes are different ({} != {})".format(gene1.name, gene.name))
    

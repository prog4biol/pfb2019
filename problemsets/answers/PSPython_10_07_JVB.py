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

        
if __name__ == '__main__':
    gene = Sequence("yfg","Mola mola","ATGATGCTGACGTACGTAGCTGACGGACTTCTGCGGCTATAGCGAGCGTACTCGACACACATCGATCGATGCAGCTATGCTAGCAGCTAG")

    # attributes are variables bound to an object, no parenthases necessary
    print("Gene Name:", gene.name)  
    print("Organism:", gene.organism)
    print("Sequence:", gene.sequence)
    # methods are functions bound to a object, so we must use parenthases
    print("Length:", gene.length())
    print("Composition:", str(gene.composition()))
    print("GC content", gene.gc_content())
    print("Fasta record:")
    print(gene.format_fasta())
    

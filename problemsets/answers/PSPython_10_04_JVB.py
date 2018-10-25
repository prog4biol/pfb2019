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
        
        
if __name__ == '__main__':
    gene = Sequence("yfg","Mola mola","ATGATGCTGACGTACGTAGCTGACGGACTTCTGCGGCTATAG")

    # attributes are variables bound to an object, no parenthases necessary
    print("Gene Name:", gene.name)  
    print("Organism:", gene.organism)
    print("Sequence:", gene.sequence)
    # methods are functions bound to a object, so we must use parenthases
    print("Length:", gene.length())

    

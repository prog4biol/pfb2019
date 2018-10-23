class Sequence(object):
    def __init__(self, name=None, organism=None, sequence=None):
        self.name = name
        self.organism = organism
        self.sequence = sequence

if __name__ == '__main__':
    gene = Sequence("yfg","Mola mola","ATGATGCTGACGTACGTAGCTGACGGACTTCTGCGGCTATAG")
    
    gene.name = "yfg"
    gene.organism = "Mola mola"
    gene.sequence = "ATGATGCTGACGTACGTAGCTGACGGACTTCTGCGGCTATAG"

    

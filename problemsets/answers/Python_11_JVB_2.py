#!/usr/bin/env python3
# 2. Write some some lines of code, outside your class (in your main
#    program) that sets the name, DNA sequence, and organism for a gene.


# Our Sequence class will inheret generic object methods from the object
# class
class Sequence(object):  
    def __init__(self, name=None, sequence='', organism=None):
        """
        Class constructor method for Sequence object. In order to create
        an instance (instantiate) an object from the Sequence class, call:
        Sequence(sequence_id, sequence_string [,organism="Org name"]).
        """
        self.name = name
        self.sequence = sequence
        self.organism = organism

        
# If someone (accidentally?) tries to import this script, the following code
# would get executed, which is not what we want. Writing the following line
# protects against this because `__name__` will be assigned the module name
# and not "__main__" as it is if this script is executed as a script:
if __name__ == '__main__':
    # There are two ways we can set the name, organism, and sequence in
    # the Sequence object, we can set them with the Sequence() constructor, 
    record1 = Sequence(
        "U31202.1",
        "GAGCTCCGGCGGGTCAGCCGGACTGTCGGCTTCCCGGGGCATCTGGGTCCGGCGGGGCACAGCCCTGGGC",
        "Homo sapiens"
    )
    # or we can set the Sequence object data via its attributes:
    record2 = Sequence()
    record2.name = "NM_008711.2"
    record2.sequence = "AGACAAACCGGTGCCAACGTGCGCGGACGCCGCCGCCGCCACCGCCGCCACCGCCGCTGGAGTCCGCCGG"
    record2.organism = "Mus musculus"

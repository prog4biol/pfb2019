#!/usr/bin/env python3
# 7. FASTA Formatter method
#    a. Add in a method that returns the sequence record in FASTA format.
#    b. Write some some lines of code, outside your class (in your main
#       program) that gets and prints the sequence in FASTA format using
#       your new method.


# private unbound class function
def _wrap(linear_sequence, width=None):
    """
    Input: (Required) A linear sequence string without any existing newline 
           characters.
           (Optional) An integer `width` argument to specify the maximum
           line length to wrap the sequence flush to.
       
    Returns: A string of the input sequence, but with newline characters
           at fixed intervals specified by the `width` keyword argument.
    """
    if width is None:
        width = sys.maxsize
        
    wrapped_sequence = ''
    linear_sequence_length = len(linear_sequence)  # pre-calc it
    for offset in range(0, linear_sequence_length, width):
        if offset+width < linear_sequence_length:
            wrapped_sequence += linear_sequence[offset:(offset+width)] + "\n"
        else:
            wrapped_sequence += linear_sequence[offset:linear_sequence_length]

    return wrapped_sequence

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

    def length(self):
        """Calc. the length of the sequence string"""
        return len(self.sequence)

    def nt_composition(self, fraction=False):
        """Calc. the nucleotide composition of the sequence. The optional
        argument `fraction`, when set to `True` will return the fractional
        nucleotide composition
        """
        nt_comp = {'A':0, 'T':0, 'G':0, 'C':0, 'N':0}
        for nt in self.sequence.upper():
            try:
                nt_comp[nt] += 1
            except KeyError:
                raise ValueError("Invalid DNA nucleotide character '{}'".format(nt))

        if fraction:
            sequence_length = self.length()
            for nt in nt_comp:
                nt_comp[nt] = float(nt_comp[nt]) / sequence_length
                
        return nt_comp
    
    def gc_content(self):
        gc_chars = set('GCgc')
        gc_count = 0
        for nt in self.sequence:
            if nt in gc_chars:
                gc_count += 1

        return float(gc_count) / self.length()

    def __str__(self):
        """
        This __str__ method allows object specific formatting, allowing us
        to use `str(sequence_obj)` to return a formatted FASTA record.
        """
        return ">{}{}\n{}\n".format(
            self.name,
            '' if self.organism is None else ' [{}]'.format(self.organism),
            _wrap(self.sequence, width=50)
        )
    
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

    # do a test print:
    print('ID: {}\nORG: {}\nLEN: {}\nGC%: {}\nSEQ: {}\n{}'.format(
        record1.name,
        record1.organism,
        record1.length(),
        record1.gc_content() * 100.0,
        record1.sequence,
        str(record1)
    ))
    print()
    print('ID: {}\nORG: {}\nLEN: {}\nGC%: {}\nSEQ: {}\n{}'.format(
        record2.name,
        record2.organism,
        record2.length(),
        record2.gc_content() * 100.0,
        record2.sequence,
        str(record2)
    ))



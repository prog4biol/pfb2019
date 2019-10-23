#!/usr/bin/env python3
# 1. Create a DNA sequence class that will contain a sequence, its name,
#    and it's organism of origin. Do this by creating an __init__ function.


# Our Sequence class will inheret generic object methods from the object
# class
class Sequence(object):  
    def __init__(self, name, sequence, organism=None):
        """
        Class constructor method for Sequence object. In order to create
        an instance (instantiate) an object from the Sequence class, call:
        Sequence(sequence_id, sequence_string [,organism="Org name"]).
        """
        self.name = name
        self.sequence = sequence
        self.organism = organism


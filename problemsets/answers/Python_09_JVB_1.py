#!/usr/bin/env python3
# Python 9 - Exceptions -Problem Set
# ===================

# 1. Add in exception handling to a script from Problem Set 8 or any script
#    you have written that uses I/O to open and read a FASTA file. 
   
#    Throw and handle (try/except) the exception
#    - if no input is provided  
#    - if the file cannot be opened
#    - if the file does not end in '.fasta' or '.fa' or '.nt'
#    - if a non ATGCN charcter is found in the sequence


import sys


def assert_dna(sequence, char_set=set('ATCGN')):
    """
    This function iterates through every residue in an input sequence
    and checks that every residue exists in the given `char_set` (can be
    a set, list, or dict) of capital characters. If an unsupported 
    character is observed, raise an AssertionError.
    """

    # Upper-case the sequence so that char case matches char_set, as
    # case has no meaning in biology
    for char in sequence.upper():
        # assert raises AssertionError exception if its expression is False
        assert char in char_set, \
            "Non-ATCGN character '{}' detected in sequence".format(char)

        
def wrap(linear_sequence, width=None):
    """
    Input: (Required) A linear sequence string without any existing newline 
           characters.
           (Optional) An integer `width` argument to specify the maximum
           line length to wrap the sequence flush to.
       
    Returns: A string of the input sequence, but with newline characters
           at fixed intervals specified by the `width` keyword argument.
    """
    if width is None:
        # Set the default width of each line to be the max integer size of
        # your machine (typically either 2**(64-1) on 64-bit machines or
        # 2**(32-1) on 32-bit machines) by convention.
        width = sys.maxsize
        
    wrapped_sequence = ''
    linear_sequence_length = len(linear_sequence)  # pre-calc it
    for offset in range(0, linear_sequence_length, width):
        # Our function iterated over each sequence, jumping every `width`
        # nucleotides along the string. This is effectively like a sliding-
        # window approach, where windows do not overlap. The left coordinate
        # of the window is `offset`, the right coordinate is `offset+width`
        if offset+width < linear_sequence_length:
            # then the sliding window sits completely within the sequence:
            # Iter 1:
            # +---------+
            #    Iter 2: +---------+
            #               Iter 3: +---------+
            # ===================================   Sequence
            wrapped_sequence += linear_sequence[offset:(offset+width)] + "\n"
        else:
            # then the sliding window projects off the end of the sequence
            # and we need to bound the window to the end of the string.
            # Also, we don't want to add the newline to the last line
            #                          Iter 4: +---------+
            # ===================================   Sequence
            wrapped_sequence += linear_sequence[offset:linear_sequence_length]

    return wrapped_sequence

# If someone (accidentally?) tries to import this script, the following code
# would get executed, which is not what we want. Writing the following line
# protects against this because `__name__` will be assigned the module name
# and not "__main__" as it is if this script is executed as a script:
if __name__ == "__main__":
    try:
        # If the user does not provide any input arguments to this script,
        # an IndexError is raised by trying to access `sys.argv[1]`, as it
        # only contains the script name in element 0. If the file does not
        # exist, a FileNotFoundError will be raised by `open()`. If the
        # file is not suffixed by `.nt`, `.fa`, or `.fasta`, we raise a
        # TypeError exception.
        fasta_infile = open(sys.argv[1], 'r')
        if not (sys.argv[1].endswith('.nt') or \
                sys.argv[1].endswith('.fa') or \
                sys.argv[1].endswith('.fasta')):
            raise TypeError("File suffix not '.nt', '.fa', or '.fasta'")

    except IndexError as error:
        sys.stderr.write('Error: Input FASTA file not given\n')

    except (FileNotFoundError, TypeError) as error:
        # Errors should go to stderr stream or you risk corrupting your
        # output or not knowing the script teriminated prematurely with an
        # error. When exiting gracefully after catching an error, returning
        # a non-0 exit status is best-practice; it communicates to the 
        # UNIX environment that your script ended in an error.
        sys.stderr.write('Error: {}\n'.format(error))
        sys.exit(1)

        
    try:
        # Here, if the user provides no second argument on the command line
        # then attempting to access `sys.argv[2]` below will trigger an
        # IndexError, causing the script to default to an 80 character line
        # width. Otherwise, try to coerce the user-inputted value to an
        # integer. Non-integer values will raise ValueErrors from `int()`.
        # If the integer is zero or negative, raise a ValueError instead.
        line_width = int(sys.argv[2])
        if line_width < 1:
            raise ValueError(
                "Input line with must be a positive integer, got '{}'".\
                format(sys.argv[2]))

    except IndexError:
        line_width = 80

    except ValueError as error:
        sys.stderr.write("Error: {}\n".format(error))
        sys.exit(1)

    sequence = ''
    defline = [None,'']  # store ID and description in a list
    fasta_outfile = sys.stdout
    for line in fasta_infile:
        # FASTA files are allowed to have blank lines between sequence
        # records, and older versions of FASTA spec allowed for comment
        # lines starting with ';'. Skip these lines.
        if line.isspace() or \
           line.startswith(';'):
            continue

        # remove leading and trailing whitespace from the line
        line = line.strip()
        
        if line.startswith('>'):  # FASTA defline
            if len(sequence) > 0:
                # If we are parsing our first FASTA record, `sequence` will
                # still be an empty string (as initialized) and evaluate to
                # False, if we are parsing any other record, then we exec
                # the following code on the previously-seen record, then
                # re-initialize our variables for the current record.
                try:
                    assert_dna(sequence)
                except AssertionError as error:
                    sys.stderr.write("Error: {} '{}'\n".format(
                        error, defline[0]))
                    sys.exit(1)
                    
                fasta_outfile.write(">{0}\n{1}\n".format(
                    ' '.join(defline), wrap(sequence, width=line_width)))
                sequence = ''

            # A split character of `None` means any whitespace.
            # `split()` can be told to split the first N instances of the
            # specified split character. Split on only the first whitespace
            # below (as descriptions may contain whitespaces)
            defline = line.lstrip('>').split(None, 1)

        else:
            sequence += line

    if len(sequence) > 0:
        try:
            assert_dna(sequence)
        except AssertionError as error:
            sys.stderr.write("Error: {} '{}'\n".format(error, defline[0]))
            sys.exit(1)
            
        fasta_outfile.write(">{0}\n{1}\n".format(' '.join(defline), wrap(sequence, width=line_width)))

    fasta_outfile.close()  # always be sure to close your output files!


    

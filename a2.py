def get_length(dna):
    """ (str) -> int
    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna1 is longer than DNA
    sequence dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    count = 0

    for char in dna:
        if char == nucleotide:
            count = count + 1

    return count
        

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool
    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """

    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool
    Return True if and only if DNA sequence dna contains no characters other
    than 'A', 'T', 'C' and 'G'.

    >>> is_valid_sequence('AGTC')
    True
    >>> is_valid_sequence('AgTC')
    False
    """

    valid = True
    
    for char in dna:
        if not(char in 'ATCG'):
            valid = False

    return valid


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str
    Return the DNA sequence obtained by inserting the second DNA sequence dna2
    into the first DNA sequence dna1 at the position given by index.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """

    if index == len(dna1):
        dna1 = dna1 + dna2
    else:
        dna1 = dna1[:index] + dna2 + dna1[index:]
    return dna1


def get_complement(nucleotide):
    """ (str) -> str
    Return the complement of nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """

    if nucleotide == 'G':
        return 'C'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'A':
        return 'T'
    else:
        return 'A'


def get_complementary_sequence(dna):
    """ (str) -> str
    Return a DNA sequence that is complementary to the DNA sequence dna.

    >>> get_complementary_sequence('AT')
    'TA'
    """

    DNA = ''

    for char in dna:
        DNA = DNA + get_complement(char)

    return DNA

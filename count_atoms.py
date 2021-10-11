def atoms(seq):
    atom_count = {
        'A':13,
        'R':26,
        'N':17,
        'D':16,
        'C':14,
        'Q':20,
        'E':19,
        'G':10,
        'H':20,
        'I':22,
        'K':24,
        'M':20,
        'F':23,
        'P':17,
        'S':14,
        'T':17,
        'W':27,
        'Y':24,
        'V':19
    }
    seq = list(seq)
    count = []
    for i in seq:
        if i in atom_count:
            count.append(atom_count[i])
    combined = list(zip(seq, count))
    print(', '.join(map(str, combined)))
    

def total_atoms(seq):
    atom_count = {
        'A':13,
        'R':26,
        'N':17,
        'D':16,
        'C':14,
        'Q':20,
        'E':19,
        'G':10,
        'H':20,
        'I':22,
        'K':24,
        'M':20,
        'F':23,
        'P':17,
        'S':14,
        'T':17,
        'W':27,
        'Y':24,
        'V':19
    }
    seq = list(seq)
    count = []
    for i in seq:
        if i in atom_count:
            count.append(atom_count[i])
    count = sum(count)
    print ("The protein has " + str(count) + " atoms in total.")
    
def main():
    if option == "1": 
        atoms(seq)
    elif option == "2": 
        total_atoms(seq)




if __name__ == "__main__":
    seq = input('''
    Enter the protein sequence \n\n 
    *Make sure the sequence does not have space or whitespace(enter)*\n\n
    *This program does not take in consideration possible water molecules in the structure*\n\n
    '''
    )
    option = input('''
    Select the function you wish to use (enter number): \n
    1. atoms - Returns a list of amino acid and atom count\n
    2. total_atoms - Returns the total count of atoms of the protein\n
    '''
    )
    
    main()
    
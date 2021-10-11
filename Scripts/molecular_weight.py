
amino_mass = {
        'A':89,
        'R':174,
        'N':132,
        'D':133,
        'C':121,
        'Q':146,
        'E':147,
        'G':75,
        'H':155,
        'I':131,
        'L':131,
        'K':146,
        'M':149,
        'F':165,
        'P':115,
        'S':105,
        'T':119,
        'W':204,
        'Y':181,
        'V':117
    }

def daltons(seq): 
    seq_lst = list(seq)
    daltons = [] 
    for i in seq_lst:
        if i in amino_mass:
            daltons.append(amino_mass[i])
    combined = list(zip(seq_lst, daltons))
    return ', '.join(map(str, combined))

def daltons_sum(seq): 
    dalton_sum = daltons(seq)
    return sum(dalton_sum)

def kDa(seq):
    kda = daltons(seq)
    kDa = (sum(kda))/1000
    return kDa

def main(): 
    if option == "1": 
        print(daltons(seq))
    elif option == "2": 
        print("This sequence has a molecular weight of " + str(daltons_sum(seq)) + " Da.")
    elif option == "3":
        print("This sequence has a molecular weight of " + str(kDa(seq)) + " kDa.")


if __name__ == "__main__":
    seq = input('''
    Enter the protein sequence \n\n 
    *Make sure the sequence does not have space or whitespace(enter)*\n\n
    *This program does not take in consideration possible water molecules in the structure*\n\n
    '''
    )
    option = input('''
    Select the function you wish to use (enter number): \n
    1. Daltons - Get the molecular weight by aminoacids in the sequence in a list format\n
    2. Daltons Sum - Get the structure aproximate molecular weight\n
    3. kDa - get the sequence aproximate molecular weight in kDaltons.
    '''
    )
    main()
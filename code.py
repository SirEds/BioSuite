#This code will change your code-based amino acid sequence to a full-name one
#just run the script and paste the sequence
#Do not enter the sequence with any space nor whitespace (\n, Enter)

def protein_code_full(code):
    amino = {
        'A':'Alanine',
        'R':'Arganine',
        'N':'Asparagine',
        'D':'Aspartic Acid',
        'C':'Cysteine',
        'Q':'Glutamine',
        'E':'Glutamic Acid',
        'G':'Glycine',
        'H':'Histidine',
        'I':'Isoleucine',
        'K':'Lysine',
        'M':'Methionine',
        'F':'Phenylalanine',
        'P':'Proline',
        'S':'Serine',
        'T':'Threonine',
        'W':'Tryptophan',
        'Y':'Tyrosine',
        'V':'Valine'
    }

    code_lst = list(code)
    name_lst = []
    for i in code_lst:
        if i in amino:
            name_lst.append(amino[i])
    print(' ---> '.join(name_lst))

#input

if __name__ == "__main__":
    seq = input('''
    Enter the protein sequence \n\n 
    *Make sure the sequence does not have space or whitespace(enter)*\n\n
    '''
    )
    protein_code_full(seq)

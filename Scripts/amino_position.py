def count(seq):
    seq = list(seq)
    count = []
    for i in range(len((seq))): 
        count.append(i+1)

    combined = list(zip(seq, count))
    return ' , '.join(map(str, combined))

seq = input("Paste the sequence: ")
print(count(seq))

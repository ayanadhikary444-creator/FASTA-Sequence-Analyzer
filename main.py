def gc_content(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100


def analyze_sequence(sequence):
    sequence = sequence.upper()

    print("Sequence length:", len(sequence))
    print("A:", sequence.count("A"))
    print("T:", sequence.count("T"))
    print("G:", sequence.count("G"))
    print("C:", sequence.count("C"))
    print("GC content: {:.2f}%".format(gc_content(sequence)))


sequence = input("Enter DNA sequence: ")

analyze_sequence(sequence)

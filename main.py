def read_fasta(filename):
    sequences = {}
    current_id = None

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                current_id = line[1:]
                sequences[current_id] = ""
            else:
                sequences[current_id] += line

    return sequences


def gc_content(sequence):
    sequence = sequence.upper()
    gc = sequence.count("G") + sequence.count("C")
    return (gc / len(sequence)) * 100


def analyze_sequence(sequence):
    sequence = sequence.upper()

    print("Length:", len(sequence))
    print("A:", sequence.count("A"))
    print("T:", sequence.count("T"))
    print("G:", sequence.count("G"))
    print("C:", sequence.count("C"))
    print("GC content: {:.2f}%".format(gc_content(sequence)))


sequences = read_fasta("sample.fasta")

for sequence_id, sequence in sequences.items():
    print("\nSequence:", sequence_id)
    analyze_sequence(sequence)

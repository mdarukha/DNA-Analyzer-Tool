# Step 1: Input/Data Storage
def input_sequences():
    sequences = []
    file_path = input("Enter the file path: ")  # Prompt the user to enter the file path
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            sequences = [line.strip() for line in file]  # Read each line as a sequence and store in a list
    except FileNotFoundError:
        print("File not found! Please enter a valid file path.")
        return input_sequences()  # Recursive call to re-enter the file path
    return sequences

# Step 2: Nucleotide Frequencies
def calculate_nucleotide_frequencies(sequences):
    nucleotide_counts = {}
    for sequence in sequences:
        for nucleotide in sequence:
            if nucleotide not in nucleotide_counts:
                nucleotide_counts[nucleotide] = 1  # Increment count for new nucleotide
            else:
                nucleotide_counts[nucleotide] += 1  # Increment count for existing nucleotide
    return nucleotide_counts


# Step 3: Identify Motifs
def identify_motifs(sequences, motif):
    motif_positions = []
    for sequence in sequences:
        positions = [i for i in range(len(sequence)) if sequence.startswith(motif, i)]  # Find motif positions in each sequence
        motif_positions.extend(positions)  # Store motif positions
    return motif_positions

# Step 4: Align Sequences
def perform_sequence_alignment(sequence1,seqeuence2):
    alignment_score = 0
    align_sequences = ""
    min_length = min(len(sequence1), len(sequence2))
    for i in range(min_length):
        base1 = sequence1[i]
        base2 = sequence2[i]
        if base1 == base2:
            alignment_score += 1
            aligned_sequences += base1
        else:
            aligned_sequences += "-"
    if len(sequence1) > min_length:
        aligned_sequences += sequence1[min_length:]
    elif len(sequence2) > min_length:
        aligned_sequences += sequence1[min_length:]
    return alignment_score, align_sequences


sequences = input_sequences()
print("Sequences:", sequences)

nucleotide_freq = calculate_nucleotide_frequencies(sequences)
print("Nucleotide Frequencies:", nucleotide_freq)

motif = input("Enter the motif to idenify: ")
motif_positions = identify_motifs(sequences, motif)
print("Motif Positions:", motif_positions)

if len(sequences) >= 2:
    sequence1 = sequences[0]
    sequence2 = sequences[1]
    alignment_score, aligned_sequences = perform_sequence_alignment(sequence1, sequence2)

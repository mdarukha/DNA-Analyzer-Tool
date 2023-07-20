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
    min_length = min(len(sequence1), len(sequence2))  # Determine the minimum length of the two sequences
    for i in range(min_length):
        base1 = sequence1[i]  # Get the base at the corresponding position in sequence1
        base2 = sequence2[i]  # Get the base at the corresponding position in sequence2
        if base1 == base2:
            alignment_score += 1  # Increment alignment score if bases match
            aligned_sequences += base1  # Append the base to the aligned sequences
        else:
            aligned_sequences += "-"  # Append a hyphen for mismatched bases
    if len(sequence1) > min_length:
        aligned_sequences += sequence1[min_length:]  # Append the remaining portion of sequence1
    elif len(sequence2) > min_length:
        aligned_sequences += sequence1[min_length:]  # Append the remaining portion of sequence2
    return alignment_score, align_sequences


sequences = input_sequences()  # Step 1
print("Sequences:", sequences)

nucleotide_freq = calculate_nucleotide_frequencies(sequences)  # Step 2
print("Nucleotide Frequencies:", nucleotide_freq)

motif = input("Enter the motif to idenify: ")
motif_positions = identify_motifs(sequences, motif)  # Step 3
print("Motif Positions:", motif_positions)

if len(sequences) >= 2:
    sequence1 = sequences[0]
    sequence2 = sequences[1]
    alignment_score, aligned_sequences = perform_sequence_alignment(sequence1, sequence2)  # Step 4

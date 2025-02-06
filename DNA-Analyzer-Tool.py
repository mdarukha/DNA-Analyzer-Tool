import matplotlib.pyplot as plt
import seaborn as sns

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
def perform_sequence_alignment(sequence1, sequence2):
    alignment_score = 0
    aligned_sequences = ""
    min_length = min(len(sequence1), len(sequence2))  # Find the length of the shorter sequence
    for i in range(min_length):
        base1 = sequence1[i]  # Get nucleotide from sequence1
        base2 = sequence2[i]  # Get nucleotide from sequence2
        if base1 == base2:
            alignment_score += 1  # Increase score for matches
            aligned_sequences += base1  # Append matching base
        else:
            aligned_sequences += "-"  # Append '-' for mismatches
    if len(sequence1) > min_length:
        aligned_sequences += sequence1[min_length:]  # Append remaining portion of sequence1
    elif len(sequence2) > min_length:
        aligned_sequences += sequence2[min_length:]  # Append remaining portion of sequence2
    return alignment_score, aligned_sequences

# Visualization - Plotting Nucleotide Frequencies
def plot_nucleotide_frequencies(nucleotide_freq):
    plt.figure(figsize=(8, 5))
    sns.barplot(x=list(nucleotide_freq.keys()), y=list(nucleotide_freq.values()), palette="Set2")  # Create bar plot
    plt.title("Nucleotide Frequency Distribution")  # Set title
    plt.xlabel("Nucleotides (A, T, C, G)")  # X-axis label
    plt.ylabel("Frequency")  # Y-axis label
    plt.show()  # Display plot

# Visualization - Plotting Sequence Alignment Results
def plot_alignment_score(sequence1, sequence2, alignment_score, aligned_sequences):
    plt.figure(figsize=(10, 2))
    
    # Create subplots for the sequences
    plt.subplot(1, 3, 1)
    plt.text(0.1, 0.5, f"Sequence 1: {sequence1}", fontsize=10, ha="left", va="center")  # Display sequence 1
    plt.axis('off')  # Hide axis
    
    plt.subplot(1, 3, 2)
    plt.text(0.1, 0.5, f"Sequence 2: {sequence2}", fontsize=10, ha="left", va="center")  # Display sequence 2
    plt.axis('off')  # Hide axis
    
    plt.subplot(1, 3, 3)
    plt.text(0.1, 0.5, f"Aligned: {aligned_sequences}", fontsize=10, ha="left", va="center")  # Display alignment result
    plt.axis('off')  # Hide axis
    
    plt.suptitle(f"Alignment Score: {alignment_score}", fontsize=16)  # Set overall title
    plt.tight_layout()
    plt.show()  # Display plot

# Main Program Execution
sequences = input_sequences()
print("Sequences:", sequences)

nucleotide_freq = calculate_nucleotide_frequencies(sequences)
print("Nucleotide Frequencies:", nucleotide_freq)

# Plot Nucleotide Frequencies
plot_nucleotide_frequencies(nucleotide_freq)

motif = input("Enter the motif to identify: ")
motif_positions = identify_motifs(sequences, motif)
print("Motif Positions:", motif_positions)

if len(sequences) >= 2:
    sequence1 = sequences[0]
    sequence2 = sequences[1]
    alignment_score, aligned_sequences = perform_sequence_alignment(sequence1, sequence2)
    
    # Plot Sequence Alignment Results
    plot_alignment_score(sequence1, sequence2, alignment_score, aligned_sequences)

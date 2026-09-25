def calculate_gc_content(sequence):
    """
    Calculates the GC content of a given nucleotide sequence.
    Returns the percentage of G and C bases.
    """
    # Convert sequence to uppercase to handle mixed-case inputs
    sequence = sequence.upper()
    
    # Count the number of Guanine (G) and Cytosine (C) bases
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    
    # Calculate the total length of the sequence
    total_length = len(sequence)
    
    # Prevent division by zero if an empty sequence is provided
    if total_length == 0:
        return 0.0
        
    # Calculate percentage
    gc_percentage = ((g_count + c_count) / total_length) * 100
    
    return gc_percentage

# Example usage:
if __name__ == "__main__":
    sample_sequence = "ATGCGATCGATCGATCGATCGATCGATCG"
    result = calculate_gc_content(sample_sequence)
    
    print(f"Analyzing Sequence: {sample_sequence}")
    print(f"Total Length: {len(sample_sequence)} bases")
    print(f"GC Content: {result:.2f}%")

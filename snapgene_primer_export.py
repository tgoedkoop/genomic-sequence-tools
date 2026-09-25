import csv
import os

def calculate_basic_tm(sequence):
    """
    Calculates a rough Melting Temperature (Tm) using the Wallace rule.
    Useful for quick validation before wet-lab synthesis.
    """
    seq = sequence.upper()
    gc_count = seq.count('G') + seq.count('C')
    at_count = seq.count('A') + seq.count('T')
    
    # Wallace rule: Tm = 4(G + C) + 2(A + T)
    return (4 * gc_count) + (2 * at_count)

def format_for_snapgene(primer_data, output_filename):
    """
    Takes a list of dictionaries containing primer info and 
    exports them to a SnapGene-compatible TSV format.
    SnapGene bulk import requires: Primer Name, Sequence, Description.
    """
    with open(output_filename, 'w', newline='') as f:
        # SnapGene prefers tab-separated values for bulk import
        writer = csv.writer(f, delimiter='\t')
        
        for primer in primer_data:
            tm = calculate_basic_tm(primer['sequence'])
            # Embed the Tm and target gene into the SnapGene description box
            description = f"Target: {primer['target']} | Estimated Tm: {tm}C"
            
            # Write the 3 required columns
            writer.writerow([primer['name'], primer['sequence'], description])
            
if __name__ == "__main__":
    # Dummy data simulating output from a tool like Primer3 targeting neurological genes
    sample_primers = [
        {'name': 'BDNF_Fwd', 'sequence': 'ATGCGTACGTTAGCTAGCTA', 'target': 'BDNF_Exon2'},
        {'name': 'BDNF_Rev', 'sequence': 'TAGCTAGCTAACGTACGCAT', 'target': 'BDNF_Exon2'},
        {'name': 'DRD2_Fwd', 'sequence': 'CGATCGATCGTACGATCGAA', 'target': 'DRD2_Exon4'},
        {'name': 'DRD2_Rev', 'sequence': 'TTCGATCGTACGATCGATCG', 'target': 'DRD2_Exon4'}
    ]
    
    output_file = "snapgene_import_ready.tsv"
    print("Formatting primer batch for SnapGene import...")
    
    format_for_snapgene(sample_primers, output_file)
    
    print("-" * 50)
    print(f"Success! {len(sample_primers)} primers written to '{output_file}'.")
    print("You can now drag this file directly into SnapGene to annotate your sequences.")
    print("-" * 50)
    
    # Display the first few lines of the generated file to prove it worked
    print("\nPreview of generated file:")
    with open(output_file, 'r') as f:
        print(f.read())
        
    # Clean up the output file for the portfolio demonstration
    if os.path.exists(output_file):
        os.remove(output_file)

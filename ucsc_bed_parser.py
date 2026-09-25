import os

def filter_bed_by_size(input_file, min_size):
    """
    Parses a UCSC BED file and extracts regions larger than a minimum size.
    Returns a list of dictionaries containing the filtered regions.
    """
    filtered_regions = []
    
    with open(input_file, 'r') as file:
        for line in file:
            # Skip header lines often found in UCSC Genome Browser files
            if line.startswith('track') or line.startswith('browser') or line.startswith('#'):
                continue
                
            columns = line.strip().split('\t')
            
            # A valid BED file needs at least 3 columns: chrom, chromStart, chromEnd
            if len(columns) >= 3:
                chrom = columns[0]
                start = int(columns[1])
                end = int(columns[2])
                
                # Calculate region size in base pairs (bp)
                size = end - start
                
                # Filter based on the provided minimum size
                if size >= min_size:
                    # Grab the feature name if it exists (4th column)
                    name = columns[3] if len(columns) >= 4 else "Unknown_Feature"
                    
                    filtered_regions.append({
                        'chromosome': chrom,
                        'start': start,
                        'end': end,
                        'name': name,
                        'size': size
                    })
                    
    return filtered_regions

# Example usage for portfolio demonstration:
if __name__ == "__main__":
    dummy_file = "example_ucsc_output.bed"
    
    # 1. Create a temporary dummy BED file for demonstration purposes
    print(f"Generating sample UCSC BED file: {dummy_file}...")
    with open(dummy_file, "w") as f:
        f.write("track name=targetGenes description=\"Sample Transcriptomic Targets\"\n")
        f.write("chr1\t1000\t5000\tTarget_A\n")
        f.write("chr1\t6000\t6150\tTarget_B_Too_Small\n")
        f.write("chr2\t15000\t25000\tTarget_C\n")
        f.write("chrX\t99000\t99800\tTarget_D\n")
        
    # 2. Run the parser to find regions larger than 1000 base pairs
    minimum_bp = 1000
    print(f"Parsing file for features larger than {minimum_bp} bp...\n")
    
    results = filter_bed_by_size(dummy_file, minimum_bp)
    
    # 3. Output the results
    print("-" * 40)
    print(f"Found {len(results)} valid genomic regions:")
    print("-" * 40)
    
    for region in results:
        print(f"Target: {region['name']} ({region['chromosome']})")
        print(f"Coordinates: {region['start']} - {region['end']}")
        print(f"Length: {region['size']} bp\n")
        
    # Clean up the dummy file after running
    if os.path.exists(dummy_file):
        os.remove(dummy_file)

# Python script to split vnames.txt into 8 parts with statistics for each part
import os
import math

def split_and_analyze_vnames(file_path, output_dir):
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    total_lines = len(lines)
    total_ids = sum(1 for line in lines if len(line.strip().split('+')) == 3)
    part_size = math.ceil(total_lines / 8)
    
    for part in range(8):
        part_folder = os.path.join(output_dir, f'part_{part + 1}')
        os.makedirs(part_folder, exist_ok=True)
        
        part_lines = lines[part * part_size: (part + 1) * part_size]
        part_file_path = os.path.join(part_folder, 'vnames.txt')
        stats_file_path = os.path.join(part_folder, 'stats.txt')
        
        # Write part file
        with open(part_file_path, 'w') as part_file:
            part_file.writelines(part_lines)
        
        # Analyze part
        country_data = {}
        start_line = part * part_size + 1
        end_line = start_line + len(part_lines) - 1
        part_ids = 0
        
        for i, line in enumerate(part_lines, start=start_line):
            parts = line.strip().split('+')
            if len(parts) == 3:
                part_ids += 1
                country = parts[0]
                if country not in country_data:
                    country_data[country] = {
                        'count': 0,
                        'start_line': i,
                        'end_line': i
                    }
                country_data[country]['count'] += 1
                country_data[country]['end_line'] = i
        
        # Write statistics in table format
        with open(stats_file_path, 'w') as stats_file:
            stats_file.write(f"Part {part + 1}\n")
            stats_file.write(f"Start Line: {start_line}\n")
            stats_file.write(f"End Line: {end_line}\n")
            stats_file.write(f"Total countries: {len(country_data)}\n")
            stats_file.write(f"Total IDs in Part: {part_ids}\n")
            stats_file.write(f"Total IDs in Original File: {total_ids}\n")
            stats_file.write(f"\n{'Country':<20}{'Total IDs':<10}{'Start Line':<12}{'End Line':<12}\n")
            stats_file.write(f"{'-'*54}\n")
            for country, data in country_data.items():
                stats_file.write(f"{country:<20}{data['count']:<10}{data['start_line']:<12}{data['end_line']:<12}\n")

# Example usage
split_and_analyze_vnames('vnames.txt', 'split_vnames')

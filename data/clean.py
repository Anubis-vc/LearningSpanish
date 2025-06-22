# removes CC license info from line of data
def clean_line(line):
    i = line.find('CC-BY')
    
    # edge case, if no cc info keep whole line
    cleaned_line = line[:i] if i != -1 else line
    cleaned_line = cleaned_line.strip()
    return cleaned_line if cleaned_line else None

def process_file(input_path, output_path, batch_size=1000):
	batch_buffer = []
	lines_processed = 0
	good_lines = 0

	with open(input_path, 'r') as infile, \
		open(output_path, 'a') as outfile:
			for line in infile:
				lines_processed += 1
				
				cleaned_line = clean_line(line)
				if cleaned_line:
					batch_buffer.append(cleaned_line)
					good_lines += 1
				
				# write in batches for efficiency
				if len(batch_buffer) >= batch_size:
					outfile.write('\n'.join(batch_buffer) + '\n')
					batch_buffer.clear()
				
				# tracking progress
				if lines_processed % 10000 == 0:
					print(f'{lines_processed:<8} lines processed')
					print(f"{good_lines:<8} good lines\n")
			
			# flush buffer at end in case anything remaining
			if batch_buffer:
				outfile.write('\n'.join(batch_buffer) + '\n')
				batch_buffer.clear()
            
if __name__ == "__main__":
    process_file('./spa-eng/spa.txt', './spa-eng/cleaned.txt')
import csv
import argparse
#==============================================
def tsvToFasta(inputFile):
	with open(inputFile[:-3]+'fasta', 'w') as outfile:
    	with open(inputFile) as infile:
        	reader = csv.DictReader(infile, delimiter='\t')
        	for line in reader:
            	outfile.write('>%s\n%s\n' % (line['unique_id'], line['sequence']))
#==============================================
if __name == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('input')
	args = parser.parse_args
	tsvToFasta(args.input)

import sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-out", help="Output directory and file name", required=True)
parser.add_argument("-muts", help="Path and file name. Will compare the mutations in this file with input data, this should match the reference genome used in alignment to make pileup file", required=True)
parser.add_argument("-pileup", help="The path and pileup file created when aligned to species referene genome", required=True)
args = parser.parse_args()

print('Comparing mutations in',args.muts,'\nwith those in ',args.pileup,'\nand writing to',args.out,'\n', file=sys.stderr)

#Open new file in specified directory
newfile=open(args.out,'w')
print('pos','\t','ant','\t','`dev','\t','input', file=newfile)

#Open mutations file for specified species and loop through mutation positions
for line in open(args.muts,'r'):
	fields=line.split()
	#Find position in pileup file
	for pos in open(args.pileup,'r'):
		pos=pos.split()
		if pos[1] != fields[1] or len(pos) < 5:
			continue
		print(fields[1],'\t',fields[0],'\t',fields[2],'\t',pos[4], file=newfile)
newfile.close

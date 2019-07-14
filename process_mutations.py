import sys,argparse

parser = argparse.ArgumentParser()
parser.add_argument("-states", help="Path and filenames of mutations and positions file", required=True)
parser.add_argument("-out", help="Output filename and directory", required=False)
args = parser.parse_args()

newfile=open(args.out,'w')
print('pos','\t','anc_base','\t','der_base','\t','input','\t','der','\t','deam','\t','other_error',file=newfile)
with open(args.states,'r') as states:
	next(states) #skip column names
	for lines in states:
		lines=lines.strip()
		fields=lines.split('\t')
		bases=('A','G','T','C')
		for character in fields[3].strip():
			#For mutations that are actually deamination
			if ((fields[1].strip()+fields[2].strip()) == "CT" or fields[1].strip()+fields[2].strip() == "TC"):
				if (character == '.'):
					print(fields[0],fields[1],fields[2],character,'1', '1','0',sep='\t',file=newfile)
					continue
				elif (character == ','):
					print(fields[0],fields[1],fields[2],character, '1', '0', '0', sep='\t',file=newfile)
					continue
				elif (character.upper() in bases):
					if (character.upper() == fields[1].strip()):
						if (character.isupper() == True):
							print(fields[0],fields[1],fields[2],character,'0','1','0',sep='\t',file=newfile)
							continue 
						elif (character.isupper() == False):
							print(fields[0],fields[1],fields[2],character, '0','0','0',sep='\t',file=newfile)
							continue
					elif (character.upper() != fields[1].strip()):
						print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
						continue
			elif ((fields[1].strip()+fields[2].strip()) == "AG" or fields[1].strip()+fields[2].strip() == "GA"):
				if (character == ','):
					print(fields[0],fields[1],fields[2], character, '1', '1','0',sep='\t',file=newfile)
					continue
				elif (character == '.'):
					print(fields[0],fields[1],fields[2],character, '1', '0','0',sep='\t',file=newfile)
					continue
				elif (character.upper() in bases):
					if (character.upper() == fields[1].strip()):
						if (character.islower == True):
							print(fileds[0],fields[1],fields[2],character,'0','1','0',sep='\t',file=newfile)
							continue
						elif (character.islower() == False):
							print(fields[0],fields[1],fields[2], character, '0','0','0',sep='\t',file=newfile)
							continue
					elif (character.upper() != fields[1].strip()):
						print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
						continue
			#If its not the derived base
			elif (character.upper() in bases):
				#if its the ancestral base
				if (character.upper() == fields[1].strip()):
					print(fields[0],fields[1],fields[2],character, '0', '0','0',sep='\t',file=newfile)
					continue
				#If the difference is a deamination error
				elif ((fields[1].strip() == 'C' or fields[2].strip() == 'C') and character.upper() == 'T'):
					if (character.islower() == True):
						print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
						continue
					elif (character.islower() ==False):
						print(fields[0],fields[1],fields[2],character,'NA','1','0',sep='\t',file=newfile)
						continue
				elif ((fields[1].strip() == 'T' or fields[2].strip() == 'T') and character.upper() == 'C'):
					if (character.islower() == True):
						print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
						continue
					elif (character.islower() ==False):
						print(fields[0],fields[1],fields[2],character,'NA','1','0',sep='\t',file=newfile)
						continue
				elif ((fields[1].strip() == 'G' or fields[2].strip() == 'G') and character.upper() == 'A'):
					if (character.islower() == True):
						print(fields[0],fields[1],fields[2],character,'NA','1','0',sep='\t',file=newfile)
						continue
					elif (character.islower() == False):
						print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
						continue
				elif ((fields[1].strip() == 'A' or fields[2].strip() == 'A') and character.upper() == 'G'):
					if (character.islower() == True):
						print(fields[0],fields[1],fields[2],character,'NA','1','0',sep='\t',file=newfile)
						continue
					elif (character.islower() == False):
						print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
						continue
				#If the diffrerence is another type of error
				elif (character.upper() != fields[1].strip()):
					print(fields[0],fields[1],fields[2],character,'NA','0','1',sep='\t',file=newfile)
					continue
			#If it equals the derived state
			elif (character == '.' or character == ','):
				print(fields[0],fields[1],fields[2],character, '1','0','0',sep='\t',file=newfile)
				continue
			#Do not count all other pileup symbols
			else:
				continue

print("processed", args.states,'\n', file=sys.stderr)

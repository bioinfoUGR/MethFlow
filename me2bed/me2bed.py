#!/usr/bin/env python
#version 1.0
#author: Ricardo Lebron
#email: rlebron@ugr.es

import argparse

parser = argparse.ArgumentParser(prog = 'me2bed', description='Convert from MethylExtract Output File to BED Output File')
parser.add_argument('-i', '--infile', help='MethylExtract Output File', action='store', type=str, required=True)
parser.add_argument('-o', '--outfile', help='BED Output File', action='store', type=str, required=True)
parser.add_argument('-f', '--format', help='Output Format', action='store', type=str, choices=['bedgraph', 'bed6', 'bed6+6', 'ucsc'], required=True)
parser.add_argument('-c', '--context', help='Methylation Context', action='store', type=str, choices=['CG', 'CHG', 'CHH'], required=True)
parser.add_argument('-n', '--name', help='UCSC custom track name', action='store', type=str, default='custom track')
parser.add_argument('-d', '--description', help='UCSC custom track description', action='store', type=str, default='created by MethFlow me2bed helper tool')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
args = vars(parser.parse_args())

with open(args['infile'],'rt') as i:
	with open(args['outfile'],'wt') as o:
		if args["format"] == 'ucsc':
			o.write('track name="{name}" description="{description}" visibility=1 useScore=1\n'.format(name = args['name'], description = args['description']))
		else:
			o.write('')
	for line in i:
		if line[0]!="#":
			with open(args['outfile'],'at') as o:
				isSS = ("\t.\t" in line)
				line = line.strip().split('\t')
				CHROM = line[0]
				CHROMSTART = str(int(line[1])-1)
				if args['context']=="CG":
					CHROMEND = str(int(line[1])+1)
				elif args['context'].startswith("CH"):
					CHROMEND = str(int(line[1])+2)
				hasF = (line[4] != ".")
				hasR = (line[7] != ".")
				if not hasF:
					line[3] = 0
					line[4] = 0
					line[5] = 0
				if not hasR:
					line[6] = 0
					line[7] = 0
					line[8] = 0
				NAME = str('_'.join([str(CHROM),str(CHROMSTART),str(CHROMEND)]))
				METH_F = int(line[3])
				METH_R = int(line[6])
				COVERAGE_F = int(line[4])
				COVERAGE_R = int(line[7])
				QUAL_F = str(line[5])
				QUAL_R = str(line[8])
				SCORE = str(int(1000 * (float(METH_F + METH_R)/float(COVERAGE_F + COVERAGE_R))))
				STRAND = '.'
				METH_F,METH_R,COVERAGE_F,COVERAGE_R = str(METH_F),str(METH_R),str(COVERAGE_F),str(COVERAGE_R)
				if args["format"] == 'bedgraph':
					line = '\t'.join([str(CHROM),str(CHROMSTART),str(CHROMEND),str(SCORE)]) + '\n'
					with open(args['outfile'],'at') as o:
						o.write(line)
				if args["format"] == 'bed6' or args["format"] == 'ucsc':
					line = '\t'.join([str(CHROM),str(CHROMSTART),str(CHROMEND),NAME,str(SCORE),STRAND]) + '\n'
					with open(args['outfile'],'at') as o:
						o.write(line)
				if args["format"] == 'bed6+6':
					line = '\t'.join([str(CHROM),str(CHROMSTART),str(CHROMEND),NAME,str(SCORE),STRAND,METH_F,COVERAGE_F,QUAL_F,METH_R,COVERAGE_R,QUAL_R]) + '\n'
					with open(args['outfile'],'at') as o:
						o.write(line)

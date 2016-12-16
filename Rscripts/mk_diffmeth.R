#!/usr/bin/env Rscript

suppressPackageStartupMessages(library("argparse"))
suppressPackageStartupMessages(library("methylKit"))

parser <- ArgumentParser()
parser$add_argument("-i", "--input", type="character", action="store", nargs="+", help="Input Datasets", required=TRUE)
parser$add_argument("-o", "--output", type="character", action="store", help="Output Plot File", required=TRUE)
parser$add_argument("-p", "--threads", type="integer", action="store", help="Threads to be used", default=4)
parser$add_argument("-a", "--assembly", type="character", action="store", help="Assembly", default="assembly")
parser$add_argument("-m", "--methylation_context", type="character", action="store", help="Methylation Context", default="CpG")
args <- parser$parse_args()

file.list=args$input

myobj=methRead(file.list, sample.id=args$input, assembly=args$assembly, treatment=seq(1,length(args$input)), context=args$methylation_context) 

meth=unite(myobj, destrand=FALSE)

myDiff=calculateDiffMeth(meth,num.cores=args$threads)

write.table(myDiff,args$output)

dev.off()



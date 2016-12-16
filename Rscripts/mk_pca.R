#!/usr/bin/env Rscript

suppressPackageStartupMessages(library("argparse"))
suppressPackageStartupMessages(library("methylKit"))

parser <- ArgumentParser()
parser$add_argument("-i", "--input", type="character", action="store", nargs="+", help="Input Datasets", required=TRUE)
parser$add_argument("-o", "--output", type="character", action="store", help="Output Plot File", required=TRUE)
parser$add_argument("-f", "--format", type="character", choices=c("pdf","postscript","svg","png","jpeg","bmp","tiff"), action="store", help="Image Format", default="pdf")
parser$add_argument("-s", "--screeplot", action="store_true", help="Get Screeplot")
parser$add_argument("-a", "--assembly", type="character", action="store", help="Assembly", default="assembly")
parser$add_argument("-m", "--methylation_context", type="character", action="store", help="Methylation Context", default="CpG")
args <- parser$parse_args()

file.list=args$input

myobj=methRead(file.list, sample.id=args$input, assembly=args$assembly, treatment=seq(1,length(args$input)), context=args$methylation_context) 

if (args$format == "pdf") {

    pdf(args$output)

} else if (args$format == "postscript") {

    postscript(args$output)

} else if (args$format == "svg") {

    svg(args$output)

} else if (args$format == "png") {

    png(args$output)

} else if (args$format == "jpeg") {

    jpeg(args$output)

} else if (args$format == "bmp") {

    bmp(args$output)

} else if (args$format == "tiff") {

    tiff(args$output)

} else {

    cat("Unknown format")

}

meth=unite(myobj, destrand=FALSE)

getCorrelation(meth,plot=FALSE)

if (args$screeplot) {

    PCASamples(meth, screeplot=TRUE)

} else {
    
    PCASamples(meth)
    
}

dev.off()



# HEICToPNG
Python code to convert a directory of HEIC files to PNG files. 

This repo will ignore files which do not have a file extension of .HEIC. It will also work with files that have an extension of .HEIC but are not
actually .HEIC files.


## Usage

python3 heic2png.py -d <input directory> -o <output directory> -t <number of threads to use> 

Number of threads is not required and will default to 1. 

This repo was designed because I was dissatisfied with the speed of existing HEIC to PNG converters, so I designed one to do so in a multithreaded fashion.

Note: While multithreading makes this process faster, if you select a number of threads which is too high, it will cause the process to run more slowly.
I have found the sweet spot to be around 10 for maximal speed.

Do not select a number of threads which is higher than the number of images you wish to convert. There is no point in this and it will simply create more overhead,
slowing the process down.



import os, sys, getopt
from PIL import Image
from pillow_heif import register_heif_opener
import threading



def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, files, outputDir):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.files = files
        self.outputDir = outputDir

    def run(self):
        for entry in files:
            #try:
                split_f = entry.name.split(".")
                if(str(split_f[1]) == "heic" or str(split_f[1]) == "HEIC"):
                    newName = entry.name.split(".")
                    image = Image.open(entry.path)
                    image.save(outputDir + newName[0] + ".png", format("png"))
            #except:
            #    print("Caught Exception, continuing...")

def filterHeic(str):
    if str.name.lower().endswith(".heic"):
        return True
    else:
        return False\


if __name__ == '__main__':
    directory = "./"
    outputDir = "./"
    threadCount = 1
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hd:o:t:", [])
    except getopt.GetoptError:
        print('heicToPNG -d <inputDirectory> -o <outputDirectory> -t [numThreads]')
        sys.exit(2)
    for opt, arg in opts:
        if(opt == '-h'):
            print('heicToPNG -d <inputDirectory> -o <outputDirectory> -t [numThreads]')
        elif opt == "-d":
            directory = arg.replace("\\", "/")
        elif opt == "-o":
            outputDir = arg.replace("\\", "/")
        elif opt == "-t":
            threadCount = int(arg, base=10)
    if( not outputDir.endswith("/")):
        outputDir = outputDir + "/"
    if( not directory.endswith("/")):
        directory = directory + "/"
    entries = os.scandir(directory)
    files = list(entries)
    files = list(filter(filterHeic, files))
    print(files)
    f = list(split(files, threadCount))
    register_heif_opener()
    for i in range(threadCount):
        t = myThread(i, "t", i, f[i], outputDir)
        t.start()
#!/usr/bin/python

import os, re, getopt, sys, subprocess
script     = os.path.basename(sys.argv[0])

def main(argv):
  inputfile  = ''
  outputfile = ''
  regex      = ''
  string      = subprocess.check_output("ls -lR ../", shell=True)
  #files      = os.system("ls -lR ../")
  #print 'files: ' + files
  #exit(2)

  try:
    opts, args = getopt.getopt(argv,"hi:o:r:",["ifile=","ofile=","regex="])
  except getopt.GetoptError:
    usage()
  for opt, arg in opts:
     if opt == '-h':
       usage()
     elif opt in ("-i", "--ifile"):
        inputfile = arg
     elif opt in ("-o", "--ofile"):
        outputfile = arg
     elif opt in ("-r", "--regex"):
        regex = arg
  #print 'Input  "' + inputfile + '"'
  #print 'Output "' + outputfile, '"'
  #print 'Regex  "' + regex + '"'

  #if inputfile and regex:
  if regex:
    grep2(string, regex)
  else:
    usage("message here")


def usage(msg=""):
    if msg:
        print("Error:", msg)
    print("Usage:", script, "-i <inputfile> -o <outputfile> -r <regex>")
    print("  eg,", script, "-i test.txt -o test.out -r vagrant")
    sys.exit(2)

def grep2(string, regex): 
  for line in string.splitlines():
    if re.search(regex, line):
      print(line[:-1])



def grep(filename, regex): 
    with open(filename) as f:
        for line in f:
            if re.search(regex, line):
                print(line[:-1])
    exit(1)


if __name__ == "__main__":
   main(sys.argv[1:])


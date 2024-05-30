#!/usr/bin/python

import sys
import getopt

def parse_run_options(argList):
    filename = ''

    try:
        opts, args = getopt.getopt(argList, "hf:")
    except getopt.GetoptError:
        print("usage: ./sortTeams.py -f <filename>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == 'h':
            print("usage: ./sortTeams.py -f <filename>")
        elif opt == '-f':
            filename = arg
        else:
            print("usage: ./sortTeams.py -f <filename>")
            sys.exit(2)
    if (filename == ''):
        print("usage: ./sortTeams.py -f <filename>")
        sys.exit(2)
    else:
        return filename

filename = parse_run_options(sys.argv[1:])
fl = open(filename, "r")
linelist = fl.readlines()
reportees = []
fileNameParts = filename.split(".")
resortedFile = fileNameParts[0]+"_resorted.csv"
rf = open(resortedFile, "w")


def find_root(filename):
    linecount = 0
    f = open(filename, "r")
    rootUser = ''
    for line in f:
        linecount = linecount + 1
        e = line.split(",")
        if (e[4] == '0'):
            rootUser = line
            break
    rf.write("team_name,manager_first_name,manager_last_name,manager_email,teamtype,parent_team_row\n")
    rf.write(e[0]+","+e[1]+","+e[2]+","+e[3]+","+e[4]+","+str(e[5]))
    return rootUser, linecount

def find_reportees(filename, orig_row):
    fr = open(filename, "r")
    linecount = 0
    for l in fr:
        linecount = linecount + 1
        if (l in reportees):
            pass
        e = l.split(",")
        mgrIdr = e[5].rstrip("\n")
        mgrId = mgrIdr.rstrip("\r")
        if (mgrId == orig_row):
            reportees.append(l)
            oldManagerIndex = int(e[5]) - 1
            oldManagerLine = linelist[oldManagerIndex]
            newManagerIndex = reportees.index(oldManagerLine)
            e[5] = newManagerIndex+2
            rf.write(e[0]+","+e[1]+","+e[2]+","+e[3]+","+e[4]+","+str(e[5])+"\n")
            find_reportees(filename, str(linecount))

rootUser, linecount = find_root(filename)
reportees.append(rootUser)
find_reportees(filename, str(linecount))

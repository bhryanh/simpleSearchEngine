import sys
import os

class TextFile:
    def readFile(self, filename):
        with open(os.path.join(sys.path[0], filename), 'r') as f:
            lines = f.readlines()
        return lines

    def removeBlankLines(self, lines):
        newLines = {}
        count = 0
        for idx in lines:
            if(lines[idx] != '\n' and lines[idx] != ''):
                newLines[count] = lines[idx]
                count += 1            
        return newLines

    def splitByPhrases(self, lines):
        newLines = {}
        idx = 0
        for line in lines:
            for splitedLine in line.split('.'):
                newLines[idx] = splitedLine
                idx += 1
        return newLines
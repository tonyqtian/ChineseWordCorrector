#!/usr/bin/python 
#-*- encoding: utf-8 -*- 
'''
Created on 2012-9-3

@author: tianqiu
'''
class wordFinder(object):
    
    def __init__(self, filepath = '../data/filteredErrorWordTable_test.txt'):
        wordTableFile = open(filepath, 'r')
        
        self.rightWrongDict = {}
        self.headDict = {}
        self.tailDict = {}
        
        self.Log = []
        
        for line in wordTableFile:
            line =  line.strip()
            if line.startswith('#'): continue
            if line.startswith('^'):
                try:
                    (wrong, right) = line.strip('^').split('>>>')
                    if right == wrong:
                        print "Warning: identical dict item: " + line
                        continue
                    self.headDict[wrong] = right
                except ValueError:
                    print line
            elif line.startswith('$'):
                try:
                    (wrong, right) = line.strip('$').split('>>>')
                    if right == wrong:
                        print "Warning: identical dict item: " + line
                        continue
                    self.tailDict[wrong] = right
                except ValueError:
                    print line
            else:
                try:
                    (wrong, right) = line.split('>>>')
                    if right == wrong:
                        print "Warning: identical dict item: " + line
                        continue
                    self.rightWrongDict[wrong] = right
                except ValueError:
                    print line

    def fileChecker(self, filepath):
        fileHandle = open(filepath, 'r')
        
        for (wrong, right) in self.headDict.items():
            count = 0
            fileHandle.seek(0)
            print "========================"
            print "STARTSWITH: Wrong word " + wrong + " from word " + right + "\n"
                        
            for line in fileHandle:
                line = line.strip()
                if line.startswith(wrong):
                    print line
                    print line.replace(wrong, right) + '\n'
                    count = count + 1
            print "========total ", count, " ==============\n"
            self.Log.append('^'+wrong+'>>>'+right+' '+str(count))

        for (wrong, right) in self.tailDict.items():
            count = 0
            fileHandle.seek(0)
            print "========================"
            print "ENDSWITH: Wrong word " + wrong + " from word " + right + "\n"
                        
            for line in fileHandle:
                line = line.strip()
                if line.endswith(wrong):
                    print line
                    print line.replace(wrong, right) + '\n'
                    count = count + 1
            print "========total ", count, " ==============\n"
            self.Log.append('$'+wrong+'>>>'+right+' '+str(count))
                                
        for (wrong, right) in self.rightWrongDict.items():
            count = 0
            fileHandle.seek(0)
            print "========================"
            print "Wrong word " + wrong + " from word " + right + "\n"
                        
            for line in fileHandle:
                line = line.strip()
                if line.count(wrong) > 0:
                    print line
                    print line.replace(wrong, right) + '\n'
                    count = count + 1
            print "========total ", count, " ==============\n"
            self.Log.append(wrong+'>>>'+right+' '+str(count))
        
        for entry in self.Log:
            print entry
                
    def wordChecker(self, filepath, wrong):
        fileHandle = open(filepath, 'r')
        count = 0
        for line in fileHandle:
            line = line.decode('utf-8')
            line = line.strip()
            if line.count(wrong) > 0:
                print line
                count = count + 1
        print "Total: ", count
                            
    def wordErrorTablePrinter(self):
        wordList = sorted(list(self.rightWrongDict.keys()))
        for right in wordList:
            print "%s %s" % (right, self.rightWrongDict[right])
    
if __name__ == '__main__':
    myFinder = wordFinder()
#    myFinder.wordErrorTablePrinter()
    myFinder.fileChecker('E:\\tianqiu\\Documents\\corpus_source\\796utf8.txt')
#    myFinder.wordChecker('E:\\tianqiu\\Documents\\corpus_source\\821utf8.txt', u'袄')
    print "Finished"
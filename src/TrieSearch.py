#!/usr/bin/python 
#-*- encoding: utf-8 -*- 
'''
Created on 2012-9-6

@author: tianqiu
'''
import types
import sys
ENCODING = 'utf-8'

class TrieSearch(object):
    
    def __init__(self, filepath = '../data/filteredErrorWordTable_high.txt'):
        wordTableFile = open(filepath, 'r')
        self.trieCHN = {}
        self.headDict = {}
        self.tailDict = {}
        
        for line in wordTableFile:
            line = line.decode(ENCODING)
            line = line.strip()
            if line.startswith('#'):
                continue
            if line.startswith('^'):
                try:
                    (wrong, right) = line.strip('^').split('>>>')
                    self.headDict[wrong] = right
                    continue
                except ValueError:
                    print line
                    continue
            if line.startswith('$'):
                try:
                    (wrong, right) = line.strip('$').split('>>>')
                    self.tailDict[wrong] = right
                    continue
                except ValueError:
                    print line
                    continue
            
            (wrong, right) = line.split('>>>')
            word_lenth = len(wrong)
            
            if word_lenth == 1:
                if self.trieCHN.has_key(wrong):
                    print "Warning: target key already defined: " + line
                    continue
                else:
                    self.trieCHN[wrong] = right
                    
            elif word_lenth == 2:
                if self.trieCHN.has_key(wrong[0]):
                    if type( self.trieCHN[wrong[0]] ) == types.DictionaryType:
                        if self.trieCHN[wrong[0]].has_key(wrong[1]):
                            if type( self.trieCHN[wrong[0]][wrong[1]] ) == types.UnicodeType:
                                print "Warning: target key already defined: " + wrong + '>>>' + self.trieCHN[wrong[0]][wrong[1]]
                                continue
                            else:
                                print "Warning: longer key already defined: " + line
                                continue
                        else:
                            self.trieCHN[wrong[0]][wrong[1]] = right
                    elif type( self.trieCHN[wrong[0]] ) == types.UnicodeType:
                            print "Warning: shorter key already defined: " + wrong[0] + '>>>' + self.trieCHN[wrong[0]]
                            continue
                    else:
                        print "Warning: Unkown KeyError: " + line
                        continue
                else:
                    self.trieCHN[wrong[0]] = {}
                    self.trieCHN[wrong[0]][wrong[1]] = right
            
            elif word_lenth == 3:
                if self.trieCHN.has_key(wrong[0]):
                    if type( self.trieCHN[wrong[0]] ) == types.DictionaryType:
                        if self.trieCHN[wrong[0]].has_key(wrong[1]):
                            if type( self.trieCHN[wrong[0]][wrong[1]] ) == types.DictionaryType:
                                if self.trieCHN[wrong[0]][wrong[1]].has_key(wrong[2]):
                                    if type( self.trieCHN[wrong[0]][wrong[1]][wrong[2]] ) == types.UnicodeType:
                                        print "Warning: target key already defined: " + wrong + '>>>' + self.trieCHN[wrong[0]][wrong[1]][wrong[2]]
                                        continue
                                    else:
                                        print "Warning: longer key already defined: " + line
                                        continue
                                else:
                                    self.trieCHN[wrong[0]][wrong[1]][wrong[2]] = right
                            elif type( self.trieCHN[wrong[0]][wrong[1]] ) == types.UnicodeType:
                                print "Warning: shorter key already defined: " + wrong[0:1] + '>>>' + self.trieCHN[wrong[0]][wrong[1]]
                                continue
                            else:
                                print "Warning: Unkown KeyError: " + line
                                continue
                        else:
                            self.trieCHN[wrong[0]][wrong[1]] = {}
                            self.trieCHN[wrong[0]][wrong[1]][wrong[2]] = right
                    elif type( self.trieCHN[wrong[0]] ) == types.UnicodeType:
                            print "Warning: shorter key already defined: " + wrong[0] + '>>>' + self.trieCHN[wrong[0]]
                            continue
                    else:
                        print "Warning: Unkown KeyError: " + line
                        continue
                else:
                    self.trieCHN[wrong[0]] = {}
                    self.trieCHN[wrong[0]][wrong[1]] = {}
                    self.trieCHN[wrong[0]][wrong[1]][wrong[2]] = right
                    
            elif word_lenth == 4:
                if self.trieCHN.has_key(wrong[0]):
                    if type( self.trieCHN[wrong[0]] ) == types.DictionaryType:
                        if self.trieCHN[wrong[0]].has_key(wrong[1]):
                            if type( self.trieCHN[wrong[0]][wrong[1]] ) == types.DictionaryType:
                                if self.trieCHN[wrong[0]][wrong[1]].has_key(wrong[2]):
                                    if type( self.trieCHN[wrong[0]][wrong[1]][wrong[2]] ) == types.DictionaryType:
                                        if self.trieCHN[wrong[0]][wrong[1]][wrong[2]].has_key(wrong[3]):
                                            if type( self.trieCHN[wrong[0]][wrong[1]][wrong[2]][wrong[3]] ) == types.UnicodeType:
                                                print "Warning: target key already defined: " + wrong + '>>>' + self.trieCHN[wrong[0]][wrong[1]][wrong[2]]
                                                continue
                                            else:
                                                print "Warning: longer key already defined: " + line
                                                continue
                                        else:
                                            self.trieCHN[wrong[0]][wrong[1]][wrong[2]][wrong[3]] = right
                                    elif type( self.trieCHN[wrong[0]][wrong[1]][wrong[2]] ) == types.UnicodeType:
                                        print "Warning: shorter key already defined: " + wrong[0:2] + '>>>' + self.trieCHN[wrong[0]][wrong[1]][wrong[2]]
                                        continue
                                    else:
                                        print "Warning: Unkown KeyError: " + line
                                        continue 
                                else:
                                    self.trieCHN[wrong[0]][wrong[1]][wrong[2]] = {}
                                    self.trieCHN[wrong[0]][wrong[1]][wrong[2]][wrong[3]] = right
                            elif type( self.trieCHN[wrong[0]][wrong[1]] ) == types.UnicodeType:
                                print "Warning: shorter key already defined: " + wrong[0:1] + '>>>' + self.trieCHN[wrong[0]][wrong[1]]
                                continue
                            else:
                                print "Warning: Unkown KeyError: " + line
                                continue
                        else:
                            self.trieCHN[wrong[0]][wrong[1]] = {}
                            self.trieCHN[wrong[0]][wrong[1]][wrong[2]] = {}
                            self.trieCHN[wrong[0]][wrong[1]][wrong[2]][wrong[3]] = right
                    elif type( self.trieCHN[wrong[0]] ) == types.UnicodeType:
                            print "Warning: shorter key already defined: " + wrong[0] + '>>>' + self.trieCHN[wrong[0]]
                            continue
                    else:
                        print "Warning: Unkown KeyError: " + line
                        continue
                else:
                    self.trieCHN[wrong[0]] = {}
                    self.trieCHN[wrong[0]][wrong[1]] = {}
                    self.trieCHN[wrong[0]][wrong[1]][wrong[2]] = {}
                    self.trieCHN[wrong[0]][wrong[1]][wrong[2]][wrong[3]] = right

            else:
                print "Incorrect length: ", word_lenth, "   ", line
     
    def sentCorrect(self, sent):
        sent_lenth = len(sent)
        if sent_lenth == 0:
            return sent

        if sent[0] in self.headDict.keys():
            try:
                sentTail = sent[1:]
            except IndexError:
                sentTail = ''
            sent = self.headDict[sent[0]] + sentTail
        
        if sent[-1] in self.tailDict.keys():
            sentHead = sent[:-1]
            sent = sentHead + self.tailDict[sent[-1]]
                    
        head = 0
        while(head < sent_lenth):
            if sent[head] in self.trieCHN.keys():
                tail = 1
                if type( self.trieCHN[sent[head]] ) == types.DictionaryType:
                    tail = 2
                    try:
                        if self.trieCHN[sent[head]].has_key(sent[head+1]):
                            if type( self.trieCHN[sent[head]][sent[head+1]] ) == types.UnicodeType:
                                sentHead = sent[:head]
                                sentTail = sent[(head+tail):]
                                sent = sentHead + self.trieCHN[sent[head]][sent[head+1]] + sentTail
                            elif type( self.trieCHN[sent[head]][sent[head+1]] ) == types.DictionaryType:
                                tail = 3
                                if self.trieCHN[sent[head]][sent[head+1]].has_key(sent[head+2]):
                                    if type( self.trieCHN[sent[head]][sent[head+1]][sent[head+2]] ) == types.UnicodeType:
                                        sentHead = sent[:head]
                                        sentTail = sent[(head+tail):]
                                        sent = sentHead + self.trieCHN[sent[head]][sent[head+1]][sent[head+2]] + sentTail
                                    elif type( self.trieCHN[sent[head]][sent[head+1]][sent[head+2]] ) == types.DictionaryType:
                                        tail = 4
                                        if self.trieCHN[sent[head]][sent[head+1]][sent[head+2]].has_key(sent[head+3]):
                                            if type( self.trieCHN[sent[head]][sent[head+1]][sent[head+2]][sent[head+3]] ) == types.UnicodeType:
                                                sentHead = sent[:head]
                                                sentTail = sent[(head+tail):]
                                                sent = sentHead + self.trieCHN[sent[head]][sent[head+1]][sent[head+2]][sent[head+3]] + sentTail
                                            else:
                                                print "Error in Trie Dict..."
                                                head = head + 1
                                                continue
                                        else:
                                            head = head + 1
                                            continue
                                    else:
                                        print "Error in Trie Dict..."
                                        head = head + 1
                                        continue
                                else:
                                    head = head + 1
                                    continue
                            else:
                                print "Error in Trie Dict..."
                                head = head + 1
                                continue
                        else:
                            head = head + 1
                            continue
                    except IndexError:
                        break
                elif type( self.trieCHN[sent[head]] ) == types.UnicodeType:
                    sentHead = sent[:head]
                    sentTail = sent[(head+tail):]
                    sent = sentHead + self.trieCHN[sent[head]] + sentTail
                else:
                    print "Error in Trie Dict..."
                    head = head + 1
                    continue
            else:
                head = head + 1
                continue

        return sent
    
    def fileChecker(self, filename, charSet):
        file_handle = open(filename, 'r')
        count = 0.0
        total_count = 0
        for line in file_handle:
            line = line.decode(charSet, 'ignore')
            line = line.strip()
            result = self.sentCorrect(line)
            if not line == result:
                print "Org:  ", line.encode(charSet)
                print "Crt:  ", result.encode(charSet)
                print
                count = count + 1
            total_count = total_count + 1
        print "==========Summary==========="
        print "Corrected: %.2f%%,  (%d/%d) " % (100*count/total_count, count, total_count)
        print
    
    def fileCorrector(self, filename, charSet, filename_o = 'stdout'):
        file_handle = open(filename, 'r')
        count = 0.0
        total_count = 0
        if filename_o == 'stdout':
            for line in file_handle:
                line = line.decode(charSet, 'ignore')
                line = line.strip()
                result = self.sentCorrect(line)
                if not line == result:
                    print "Org:  ", line.encode(charSet)
                    print "Crt:  ", result.encode(charSet)
                    print
                    count = count + 1
                total_count = total_count + 1
            print "==========Summary==========="
            print "Corrected: %.2f%%,  (%d/%d) " % (100*count/total_count, count, total_count)
            print
        else:
            file_write = open(filename_o, 'w')
            for line in file_handle:
                line = line.decode(charSet, 'ignore')
                line = line.strip()
                result = self.sentCorrect(line)
                file_write.write(result.encode(charSet) + '\n')
                if not line == result:
                    count = count + 1
                total_count = total_count + 1
            print "==========Summary==========="
            print "Corrected: %.2f%%,  (%d/%d) " % (100*count/total_count, count, total_count)
            print
                
def test():
    myTrie = TrieSearch()
    myTrie.fileChecker('E:\\tianqiu\\Documents\\corpus_source\\9utf8.txt', 'utf-8')       
         
if __name__ == '__main__':
        
#    test = u'没哪么简单'
#    print test
#    print myTrie.sentCorrect(test)
    argv_lenth = len(sys.argv)
    if argv_lenth < 2:
        print 'Start...'
        import cProfile
        cProfile.run('test()')
#        cProfile.run('test()', '../data/507.profile')
        print "\nFinished."
    elif argv_lenth == 3:
        filename = sys.argv[1]
        charSet = sys.argv[2]
        myTrie = TrieSearch()
        myTrie.fileCorrector(filename, charSet)
        print "\nFinished."
    elif argv_lenth == 4:
        filename = sys.argv[1]
        charSet = sys.argv[2]
        filename_o = sys.argv[3]
        myTrie = TrieSearch()
        myTrie.fileCorrector(filename, charSet, filename_o)
        print "\nFinished."
    else:
        print "Incorrect argument input "
        print "Usage: TireSearch [Input filename] [Char set] [Output filename] "
        sys.exit()
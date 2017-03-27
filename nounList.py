from _curses import raw
from nltk.tokenize import PunktSentenceTokenizer
import nltk
import re

chunkDetector = r""" NP :{<NNP.?>+}

             }<VB.?|MD>+{"""

dict={}
nounList=[]
def check_Tree(chunkedNoun) :
    for subtree in chunkedNoun.subtrees(filter=lambda t: t.label() == 'NP'):
        tree_stuff = subtree.leaves()
        print(tree_stuff)
        for k, v in tree_stuff:
            dict[k] = v
            # print(dict)
            nounList.append(k)
            print(nounList)

def checkConsole() :
    try :

        sentence_text="This is just a bot tokenizing step 1  of our project"
        train_text ="Amay,Ramesh,Bush are all perverts."
        punkt=PunktSentenceTokenizer(sentence_text)
        real_text=punkt.tokenize(train_text)
        #print(real_text)
        for words in real_text :
            newWords=nltk.word_tokenize(words)
            #print(newWords)
            tagged_words=nltk.pos_tag(newWords)
            #print(tagged_words)
            #Introducing chunking.
            chunkParser=nltk.RegexpParser(chunkDetector)

            chunkedNoun=chunkParser.parse(tagged_words)
            #print(chunkedNoun)
            check_Tree(chunkedNoun)
    except Exception as e :
        print(str(e))

checkConsole()



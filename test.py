
from nltk.tokenize import PunktSentenceTokenizer
import nltk
import re
verbDetector=r""" VB :{<VBP.*> | <VB.?>}
             }<NNP|MD|IN|DT>+{"""


chunkDetector = r""" NP :{<NNP.?>}
             }<VB.?|MD>+{"""

dict={}
nounList=[]
verbList=[]
def check_Tree(chunkedNoun,chunkedVerbs) :
    for subtree in chunkedNoun.subtrees(filter=lambda t: t.label() == 'NP'):
        #print("Noun List...")
        tree_stuff = subtree.leaves()
        #print(tree_stuff)
        for k, v in tree_stuff:
            dict[k] = v
            # print(dict)
            nounList.append(k)
            del dict[k]
            #print(nounList)
    for subTree in chunkedVerbs.subtrees(filter= lambda V:      V.label() == 'VB') :
        #print("VERB LIST...")
        dict.clear()
        verbTree=subTree.leaves()
        #print(verbTree)
        for key, value in verbTree:
            dict[key] = value
            # print(dict)
            verbList.append(key)
            del dict[key]
            #print

    print("VerbList->",verbList)
    print('NounList->',nounList)




def checkConsole() :
    try :

        sentence_text="This is just a bot tokenizing step 1  of our project"
        train_text ="Amay,Ramesh,Bush are all insane and they can do it."
        punkt=PunktSentenceTokenizer(sentence_text)
        real_text=punkt.tokenize(train_text)
        #print(real_text)
        for words in real_text :
            newWords=nltk.word_tokenize(words)
            #print(newWords)
            tagged_words=nltk.pos_tag(newWords)
            print(tagged_words)
            #Introducing chunking.
            chunkParser=nltk.RegexpParser(chunkDetector)
            verbParser=nltk.RegexpParser(verbDetector)

            chunkedVerbs=verbParser.parse(tagged_words)
            chunkedNoun=chunkParser.parse(tagged_words)
            #print(chunkedNoun)
            check_Tree(chunkedNoun,chunkedVerbs)
    except Exception as e :
        print(str(e))

checkConsole()

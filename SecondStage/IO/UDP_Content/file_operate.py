class WordSearch:
    def __init__(self):
        self.__f = open("dict.txt","r")
    def word_search(self,word):
        for line in self.__f:
            character = line.split(" ")[0]
            if character>word:
                return
            if character == word:
                return line
        self.__f.close()





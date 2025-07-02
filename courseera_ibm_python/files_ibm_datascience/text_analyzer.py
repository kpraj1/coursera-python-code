class TextAnalyzer(object):

    def __init__(self, text):
        # remove punctuation
        self.text = text.replace(".", " ").replace("!", " ").replace(",", " ").replace("?", " ").lower()
        # make text lowercase

    def freqAll(self):
        # split text into words
        words = self.text.split(' ')
        # Create dictionary
        wordsDict = {}
        for word in set(words):
            wordsDict[word] = words.count(word)

        return wordsDict

    def freqOf(self, word):
        # get frequency map
        freqDict = self.freqAll()
        if word in freqDict:
            return freqDict[word]
        else:
            return 0

givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
analyzed = TextAnalyzer(givenstring)

print(analyzed.freqAll())
print("lorem word occurred",analyzed.freqOf("lorem"),"times")
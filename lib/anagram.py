# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        def is_anagram(word1, word2):
            return sorted(word1) == sorted(word2)
        
        return [word for word in word_list if is_anagram(self.word, word)]

# Sample usage
if __name__ == "__main__":
    listen = Anagram("listen")
    print(listen.match(['enlists', 'google', 'inlets', 'banana']))
    # Output should be ['inlets']

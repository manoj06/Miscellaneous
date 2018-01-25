def sign(word):
        char_list = list(word)
        char_list.sort()
        word_list = []
        for char in char_list:
                if not char in word_list:
                        word_list.extend([char, str(word.count(char))])
                else:
                        continue
        signature = "".join(word_list)
        return signature

def anagramCollect(filename):
        """Obtain Sinatures and Create a Dict.
        key = the signature
        value = a list of words with same signature"""
        f = open(filename, "r")
        ana_dict = {}
        for word in f:
                signature = sign(word[:-1])
                if ana_dict.has_key(signature):
                        ana_dict[signature].append(word[:-1])
                else:
                        ana_dict[signature] = [word[:-1]]
        f.close()
        return ana_dict

def printAnagram(ana_dict):
        ana_list = ana_dict.values()
        for value in ana_list:
                if len(value) > 1:
                        print value
                else:
                        continue

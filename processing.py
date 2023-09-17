import nltk
import re
from collections import defaultdict
nltk.download('punkt')

from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

from nltk.stem import PorterStemmer
nltk.download('wordnet')


with open('./text.txt','r',encoding='utf-8') as _file:
    text = (_file.read())
    text = re.sub('”|“|`','"',text)


tokens_with_no_stopwords = [word.lower() for word in word_tokenize(text) if word.lower() not in stopwords]


sents = nltk.sent_tokenize(text)
sent_dict = {numb:sent.replace('\n',' ') for  numb,sent in enumerate(sents)} # {147: 'I was going to bring her back.',}

# def
#     sentence = defaultdict(list) # 'recognize': ['recogn', 'recognize']
#     for word in tokens_with_no_stopwords:
#         word = word.lower()
#         box = []

#         ps = PorterStemmer()
#         stems= ps.stem(word)

#         lemmatizer = WordNetLemmatizer()
#         lems= (lemmatizer.lemmatize(word))
#         if stems not in box:

#             box.append(stems)
#         if lems not in box:
#             box.append(lems)
#         if word not in '''!’--()-…[]{}-;+\'.?@#$%:'"\,./^&`amp;*_***!”?''':

#             sentence[stems].extend((box))

#     all_words = {}
#     len(sentence)
#     for _key, _value in sentence.items():
#         _main_word = _value[-1]
#         new = list(set(_value))

#         all_words[_main_word] = new
#     return all_words
class TextProcessorWords:
    def __init__(self):
        self.ps = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def get_stems_and_lemmas(self, word):
        stems = self.ps.stem(word)
        lems = self.lemmatizer.lemmatize(word)
        return stems, lems

    def clean_word(self, word):
        cleaned_word = ''.join(char for char in word if char not in '''=!()…[]{};+?@#$%:,/^&`;*!”?''' )
        return cleaned_word.lower()

    def process_tokens(self, tokens):
        sentence = defaultdict(list)

        for word in tokens:
            cleaned_word = self.clean_word(word)
            stems, lems = self.get_stems_and_lemmas(cleaned_word)

            if stems not in sentence[word]:
                sentence[word].append(stems)
            if lems not in sentence[word]:
                sentence[word].append(lems)

        return sentence

    def consolidate_results(self, sentence):
        all_words = {}

        for word, word_list in sentence.items():


            words_with_max_length = [word for word in word_list if len(word) == max(map(len, word_list))]
            main_word=  max(filter(lambda word: word.endswith('y'), words_with_max_length), default=max(words_with_max_length, key=len))
            unique_values = list(set(word_list))

            all_words[main_word] = unique_values

        return all_words

text_processor = TextProcessorWords()
tokens = tokens_with_no_stopwords
processed_sentence = text_processor.process_tokens(tokens)
result = text_processor.consolidate_results(processed_sentence)

import re
sentence_recognaze=  defaultdict(list) # dict {word : [10,30]}
for token_word,_values in result.items():
    for var in (_values):
        for numb_sent,sent in sent_dict.items():
            if var in sent.lower():

                if numb_sent not in sentence_recognaze[token_word]:
                    sentence_recognaze[token_word].append(numb_sent)


class WordBox:
    def __init__(self,word):
        self.word = word
        self.num_setnence = sentence_recognaze[word]
        self.examples = [sent_dict[sent] for sent  in self.num_setnence]
        self.word_var = result[word]
print(result)

# pot_word = WordBox('') # self-name need checked by real word
# print(pot_word.word,len(pot_word.num_setnence),pot_word.num_setnence,pot_word.word_var,)
# [print(i) for i in pot_word.examples]


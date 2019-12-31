import nltk
nltk.download('punkt')
nltk.download('treebank')

from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer


tb_tokenizer=TreebankWordTokenizer()

text1 = "Love looks not with the eyes, but with the mind. And therefore is wing'd Cupid painted blind."
text2 = "South Korea population is 48,750,000"

word_tok = word_tokenize(text1)
word_tok2 = word_tokenize(text2)

wordpunct_tok = WordPunctTokenizer().tokenize(text1)
wordpunct_tok2 = WordPunctTokenizer().tokenize(text2)

tb_tok = tb_tokenizer.tokenize(text1)
tb_tok2 = tb_tokenizer.tokenize(text2)

print("word_tokenize를 사용한 경우는 아래와 같습니다.")
print(word_tok)
print(word_tok2)
print("wordpunct_tokenize를 사용한 경우는 아래와 같습니다.")
print(wordpunct_tok)
print(wordpunct_tok2)
print("Treebanktokenize를 사용한 경우는 아래와 같습니다.")
print(tb_tok)
print(tb_tok2)
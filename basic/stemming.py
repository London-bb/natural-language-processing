import nltk
nltk.download('wordnet')

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer

#각각 porter와 lancaster stemming 알고리즘을 적용합니다.
def porter_stem(tokenize_list):
    p = PorterStemmer()
    result = []

    for w in tokenize_list:
        result.append(p.stem(w))

    return result

def lancaster_stem(tokenize_list):
    l = LancasterStemmer()
    result = []

    for w in tokenize_list:
        result.append(l.stem(w))

    return result

def compare(origin, compare):
    
    result = []
    for i in range(len(origin)):
        if str(origin[i]) == str(compare[i]):
            pass
        else:
            result.append(compare[i])

    print('\033[1m' + str(result) + '\033[0m')

text = "The necrosis is closely related to the flow of blood. So we can make a diagnosis of tissue necrosis to observe the flow of blood."
#ref. S.H.LEE el. 2. "Development of Laser Speckle Contrast Imaging System for early diagnosing tissue necrosis.The Korea Society of Medical & Biological Engineering 2019 Oct 055"

word_tok= word_tokenize(text)

t1_p_stem = porter_stem(word_tok)

t1_l_stem = lancaster_stem(word_tok)

print("word_tokenize를 사용한 경우는 아래와 같습니다.")
print(word_tok)

print("아래는 포터알고리즘 어간추출(stemming)의 결과입니다.")
print(t1_p_stem)

print("아래는 란체스터알고리즘 어간추출(stemming)의 결과입니다.")
print(t1_l_stem)

print("아래는 porter 알고리즘과 lancaster 알고리즘 결과의 차이입니다.")
compare(word_tok, t1_p_stem)
compare(word_tok, t1_l_stem)
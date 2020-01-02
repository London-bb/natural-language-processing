from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

word = "불용어란 자주 등장하지만 데이터를 분석하는데 있어 큰 의미를 갖지 않는 단어들을 뜻합니다. 불용어는 임의로 설정할 수 도 있고, 영문의 불용어 리스트의 경우 NTLK 라이브러리에서 정의한 불용어 리스트를 사용할 수 있습니다. 다만 한국어의 경우 조사와 접속사의 사용이 다양하며, 언어의 변형이 많기 때문에 직접 정의하는게 좋습니다."

stop ="자주,종종,가끔,많이"

#예시로 설정한 불용어를 ,을 기준으로 잘라냅니다.
stop_list = stop.split(',')
tok = word_tokenize(word)

def stopword(word_tokenize):
    result = []

    for w in word_tokenize:
        #임의로 정의한 불용어가 아닌 경우만 result에 추가합니다.
        if w not in stop_list:
            result.append(w)

    return result

print('토큰화한 문장은'+ str(tok) + '입니다.')
print('불용어를 제거하면' + str(stopword(tok)) + '입니다')

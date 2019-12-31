from nltk.tokenize import sent_tokenize
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Okt

hannanum = Hannanum()
kkma = Kkma()
okt = Okt()

text1 = "I am graduate Yonsei university. My major is Bio Medical engineering. but my favorite is Machine learning&Data Science."
text2 = "자연어 처리 어렵네요. 특히 한국어 처리는 더 어려운거 같아요. 다들 화아팅하세요!"

print("sent_tokenize를 사용하면 아래와 같이 토큰화됩니다.")
print(sent_tokenize(text1))
print(sent_tokenize(text2))

print("Hannanum을 쓰면 아래와 같이 분류됩니다.")
print(hannanum.morphs(text1))
print(hannanum.morphs(text2))

print("Kkma를 쓰면 아래와 같이 분류됩니다.")
print(kkma.morphs(text1))
print(kkma.morphs(text2))

print("Okt를 사용하면 아래와 같이 분류됩니다.")
print(okt.morphs(text1))
print(okt.morphs(text2))


#jpype._jvmfinder.JVMNotFoundException: No JVM shared library file (jng>vm.dll) found. Try setting up the JAVA_HOME environment variable properly.
#라는 오류가 발생하신다면 C:\아나콘다설치위치\Lib\site-packages\jpype 에 들어가서 _jvmfinder.py 파일을 여신 다음 ctrl + F 로 java_home 검색 후
#java_home = "자바설치경로" 로 해주시면 오류없이 실행됩니다.
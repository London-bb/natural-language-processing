from bs4 import BeautifulSoup as bs
import sys
import urllib.request
from urllib.parse import quote

def get_URL(keyword):
    url_page_source = "http://mksports.co.kr/search/?page="
    url_keyword_source = "&kwd="
    URL = url_page_source + url_keyword_source + quote(keyword)
    return URL

def get_link(page_num, URL, output_file):
    #입력하는 page_num에 따라 page가 순차적으로 추가되도록 for문 생성
    for i in range(page_num):
        current_page = i
        #URL에서 '='의 위치를 찾고 값을 가져옴
        page_index = URL.index('=')
        #index함수를 통해 알아낸 =의 위치를 통해 page를 삽입하여 url 완성
        URL_with_page = URL[: page_index+1] + str(current_page) + URL[page_index+1 :]

        source_code_from_URL = urllib.request.urlopen(URL_with_page)
        soup = bs(source_code_from_URL, 'lxml', from_encoding='utf-8')
        
        #soup내부에 <dt,class=tit>인 모든 부분을 가져와서 title에 저장 
        for title in soup.find_all('dt', 'tit'):
            #title에서 기사로 연결되는 링크를 가진 <a>태그를 tit_link에 저장
            tit_link = title.select('a')
            #<a>태그 내부에는 공통 부분인 http://mksports.co.kr/search/ 이 생략되어있기 때문에 공통부분과 <a>태그를 결합
            article_url = "http://mksports.co.kr/search/" + tit_link[0]['href']
            print(article_url)
            #본문 내용을 가져오기위한 함수와 연결
            get_text(article_url, output_file)

def get_text(URL, output_file):
    #get_link함수에서 생성된 aritcle_url을 URL변수로 입력받음
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = bs(source_code_from_URL, 'lxml', from_encoding='utf-8')
    #기사 내용이 <div class=read_txt>에 저장되어 있으므로 read_txt class전체를 content에 저장
    content = soup.select('div.read_txt')
    for text in content :
        #content안에서 text형식인 모든 자료를 꺼내와 str_item에 저장
        str_item = str(text.find_all(text=True))
        print(type(text))
        output_file.write(str_item)


page_num = input('크롤링할 페이지 수를 입력해주세요.')
keyword = input('검색어를 입력해주세요.')
output_filename = input('저장할 파일이름을 적어주세요.') + '.txt'    
output_file = open(output_filename, 'w')

url = get_URL(keyword)
get_link(int(page_num), url, output_file)

output_file.close()


import pdfcrowd
import sys

try:
    #자신이 원하는 이름을 사용하고싶다면, 사이트의 회원가입이 필요합니다.
    client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    output_file = open('leo_bb.pdf', 'wb')

    #변환하고자하는 웹사이트의 url을 입력합니다.
    pdf = client.convertUrl('https://leo-bb.tistory.com/')

    output_file.write(pdf)

    output_file.close()
except pdfcrowd.Error as why:
    
    #에러 발생시 어떠한 에러가 발생했는지 알려주며, 해당 사이트를 참고하여 해결할 수 있습니다.
    sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    raise
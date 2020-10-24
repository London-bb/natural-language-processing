from bs4 import BeautifulSoup as bs
import urllib.request
import re
from selenium import webdriver
import pandas as pd
import datetime
import os
import getpass

# RISS에 논문을 검색하여 제목/저자/요약본문/링크를 csv 파일로 저장

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))


def get_URL(page):
    url_before_page = "http://www.riss.or.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount="
    url_after_page = "&orderBy=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_kor&colName=re_a_kor&pageScale=10&query=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0"
    URL = url_before_page + page + url_after_page

    return URL


def get_link(csv_name, page_num):

    for i in range(page_num):
        current_page = i * 10
        URL = get_URL(str(current_page))
        source_code_from_URL = urllib.request.urlopen(URL)
        soup = bs(source_code_from_URL, "lxml", from_encoding="utf-8")

        for j in range(10):
            paper_link = soup.select("li > div.cont > p.title > a")[j]["href"]
            paper_url = "http://riss.or.kr" + paper_link

            reference_data = get_reference(paper_url)

            save_csv(csv_name, reference_data)


def get_reference(URL):
    driver_path = os.path.join(ROOT_PATH, "chromedriver")
    driver = webdriver.Chrome(
        driver_path, options=webdriver.ChromeOptions().add_argument("headless")
    )
    driver.get(URL)

    html = driver.page_source
    soup = bs(html, "html.parser")

    title = soup.find("h3", "title")
    title_txt = title.get_text("", strip=True).split("=")
    title_kor = re.sub("\n\b", "", str(title_txt[0]).strip())
    title_eng = str(title_txt[1]).strip()

    txt_box = []
    for text in soup.find_all("div", "text"):
        txt = text.get_text("", strip=True)
        txt_box.append(txt)

    txt_kor = txt_box[1]
    txt_eng = txt_box[3]

    detail_box = []
    detail_info = soup.select(
        "#soptionview > div > div.thesisInfo > div.infoDetail.on > div.infoDetailL > ul > li > div > p"
    )
    for detail in detail_info:
        detail_content = detail.get_text("", strip=True)
        detail_wrap = []
        detail_wrap.append(detail_content)

        detail_box.append(detail_wrap)

    author = ",".join(detail_box[0])
    book = (
        "".join(detail_box[2] + detail_box[3])
        .replace("\n", "")
        .replace("\t", "")
        .replace(" ", "")
        + " p."
        + "".join(detail_box[-2])
    )
    keyword = ",".join(detail_box[6])

    reference_data = pd.DataFrame(
        {
            "저자": [author],
            "국문 제목": [title_kor],
            "영문 제목": [title_eng],
            "수록지": [book],
            "핵심어": [keyword],
            "국문 요약": [txt_kor],
            "영문 요약": [txt_eng],
            "링크": [URL],
        }
    )

    driver.close()

    return reference_data


def save_csv(csv_path, data):
    csv = csv_path.replace("/", "\\")
    if os.path.isfile(csv_path):
        data.to_csv(csv, mode="a", header=False, index=False)
    else:
        data.to_csv(csv, mode="w", header=True, index=False)


def make_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    user_name = getpass.getuser()
    folder_root = "./example"
    path = folder_root + now
    make_folder(path)
    filename = input("저장할 csv 이름을 입력해주세요")
    csv_path = path + "/" + filename + ".csv"
    page_num = input("크롤링할 페이지 수를 입력해주세요.")
    get_link(csv_path, int(page_num))

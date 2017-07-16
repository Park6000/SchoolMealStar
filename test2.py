from bs4 import BeautifulSoup
import urllib.request


OUTPUT_FILE_NAME = 'menu.txt'




URL = 'http://www.siheung.hs.kr/main.php?menugrp=080702&master=meal2&act=list&SearchYear=2017&SearchMonth=07&SearchDay=13#diary_list'


# 크롤링 함수
def get_text(URL):
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('div', id='meal_container'):
        text = text + str(item.find_all(text=True))
    return text


# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w')
    result_text = get_text(URL)
    open_output_file.write(result_text)
    open_output_file.close()


if __name__ == '__main__':
    main()

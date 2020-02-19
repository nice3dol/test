from django.shortcuts import render
from .models import Comics, ComicsDetail
from .comic_utils import find_comics
import requests
from bs4 import BeautifulSoup
import os
from blog import settings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your views here.


def index(request):
    comic_qs = Comics.objects.all()[:10]
    return render(request, 'index.html', {'comics': comic_qs})

def comic_viewer(request, title, episode):
    # 타이틀 코드로 해당 웹툰 확인
    # 만약 없다면, "없어요!" 라고 경고
    # 만약 있다면, 데이터베이스에 가서 주어진 에피소드 번호가 있는지 확인
    # 있다면, 그렇다면 웹툰 실행
    # 없다면, 네이버에 가서 가지고와 데이터베이스에 저장 후 실행

    comic_qs = Comics.objects.filter(title_code=title)

    if comic_qs.exists():
        try:
            comic_episode_qs = ComicsDetail.objects.get(comic_id=comic_qs.first().id)
        except Exception as e:
            print("없어용", e)
            # base_url = 'https://comic.naver.com/webtoon/detail.nhn'
            # header = {
            #     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
            # param = {"titleId" : comic_qs.first().comic_code, "no": episode}
            # req = requests.get(base_url, params=param, headers=header)
            # print(req.text)
            driver = webdriver.Chrome(executable_path=os.path.join(settings.BASE_DIR, 'mysite/utils/chromedriver'))
            driver.get("https://comic.naver.com/webtoon/detail.nhn?titleId={}&no={}".format(comic_qs.first().comic_code), str(episode))
            html = driver.page_source
            print(html)


            # https: // comic.naver.com / webtoon / detail.nhn?titleId = 20853 & no = 1211



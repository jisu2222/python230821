# DemoForm2.py
# DemoForm.ui(화면을 저장) + DemoForm2.py(로직을 저장)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup
 


#디자인 파일을 로딩(파일명 수정)
form_class = uic.loadUiType("form2.ui")[0]

#폼 클래스 정의(QMainWindow상속)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
       super().__init__()
       self.setupUi(self)
    def firstClick(self):  
        url = "https://www.daangn.com/"
        response = requests.get(url)
        #검색이 용이한 객체 생성
        soup = BeautifulSoup(response.text, "html.parser")
        f = open("daangn.txt", "wt", encoding="utf-8")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            title = post.find("h2", attrs={"class":"card-title"})
            price = post.find("div", attrs={"class":"card-price"})
            addr = post.find("div", attrs={"class":"card-region-name"})
            print("{0} , {1} , {2}".format(title, price, addr))
            f.write(f"{title.text}, {price.text}, {addr.text}\n")
        f.close()
        self.label.setText("크롤링 완료")
    def secondClick(self):   
       self.label.setText("두번째 버튼 클릭")
    def thirdClick(self):   
       self.label.setText("세번째 버튼 클릭했음~~")
    
#직접 모듈을 실행했는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoform = DemoForm()
    demoform.show()
    app.exec_()



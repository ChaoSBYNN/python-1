import urllib.request as ur
import urllib.parse as up
import re
import easygui as e
import socket  
from bs4 import BeautifulSoup

def find_download(h_soup,where,count):
      H = h_soup.find("h1",class_ = "article-title").a.get_text()
      if H[0] != "【" :
            try :
                  str1 = h_soup.find("h2").span.span.get_text()
            except :
                  str1 = "404notfind%d"
      elif "【广告招租】" in H:
            return count
      else :
            str1 = ''
            for i in H:
                  str1 += i
                  if i == "】":
                        break
                  
      timeout = 10
      for l in h_soup.find_all("img",class_ = re.compile("align.+"),src = re.compile(".[a-zA-Z]{3,4}$")):
            if l["src"] in ["http://ww1.sinaimg.cn/large/e75a115bgw1ezy20gtzgpj20m80b4gol.jpg","http://ww2.sinaimg.cn/mw690/e75a115bgw1f8ambv7odog20a00327h9.gif","http://ww3.sinaimg.cn/mw690/e75a115bgw1f76bno2v7kj20a0032wew.jpg","http://ww2.sinaimg.cn/mw690/e75a115bgw1ezm9k3vracj20by0by0tk.jpg"]:
                  continue
            url_fin = l["src"]
            for i in range(3):
                  try : 
                        request_fin = ur.Request(url_fin,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})
                        fin_img = ur.urlopen(request_fin,timeout = timeout).read()
                        break
                  except :
                        pass
            else :
                  continue
            file = open(where+"\\"+"%s_%d.gif" % (str1,count),'wb')
            file.write(fin_img)
            file.close()
            print("已下载"+"\n"+"%s_%d.gif" % (str1,count))
            count += 1
      return count

            
def tryopen(req):
      errorTimes = 0 
      while errorTimes != 10:
            try: 
                  errorTimes += 1
                  return ur.urlopen(req,timeout = 10).read().decode("utf-8")
            except: 
                  pass
      return None
      

def main():
      if e.buttonbox("Are you ready?","黄虫",choices = ("of cause!","i'm Gay.")) == "of cause!":
            while 1:
                  have = e.multenterbox("输入你想要的页数，如果只要一页就填一样的：","黄虫",fields = ("起始页","结束页"))
                  if have[0] != '' and have[1] != '':
                        nice = int(have[0])
                        day = int(have[1])
                        if nice > 1000 or day > 1000:
                              e.msgbox("绅士请注意身体！")
                              continue
                        break
                  e.msgbox("serious?")
            
            where = e.diropenbox("你要保存到哪？")
            i = nice
            while 1:
                  url1 = "http://www.gifjia.com/neihan/page/%d/" % i
                  request1 = ur.Request(url1,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})
                  html1 = tryopen(request1)
                  h1_soup = BeautifulSoup(html1)
                  text = '&&!@#$#@'
                  word = 0
                  for j in h1_soup.find_all("a",href = re.compile("[0-9]+/$")):
                        if text in j["href"]:
                              continue
                        word += 1
                        if word > 11:
                              break
                        url2 = j["href"]
                        text = url2
                        count = 0
                        request2 = ur.Request(url2,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})#����
                        html2 = tryopen(request2)
                        try :
                              h2_soup = BeautifulSoup(html2)
                              count = find_download(h2_soup,where,count)
                        except:
                              continue
                        for k in h2_soup.find_all("a",href = re.compile(j["href"]+"[0-9]+/")):
                              url3 = k["href"]
                              if j["href"]+"1/" == k["href"]:
                                    continue
                              request3 = ur.Request(url3,headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.43 BIDUBrowser/6.x Safari/537.31'})#����
                              html3 = tryopen(request3)
                              try :                                    
                                    h3_soup = BeautifulSoup(html3)
                                    count = find_download(h3_soup,where,count)
                              except:
                                    pass
                  if i >= day:
                        break
                  i += 1                  
      else :
            e.msgbox("╭∩╮(︶︿︶)╭∩╮")
      

if __name__ == '__main__':
      main()
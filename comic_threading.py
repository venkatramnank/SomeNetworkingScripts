import requests
from bs4 import BeautifulSoup
import os
import threading

def image_down(start_img, stop_img):
    for numb in range(start_img, stop_img):
        url = 'http://xkcd.com/{}/'.format(numb)
        url_get = requests.get(url)
        soup = BeautifulSoup(url_get.content, 'html.parser')
        link = soup.find('div', id='comic').find('img').get('src')
        link = link.replace('//', 'http://')
        img_name = os.path.basename(link)
        try:
            img = requests.get(link)
            with open(img_name, 'wb') as f_out:
                f_out.write(img.content)
        except Exception:
            # Just want images don't care about errors
            pass
 
if __name__ == '__main__':
    threadslist=[]
    for i in range(0, 1400, 100):
        threadobj=threading.Thread(target=image_down,args=(1,20))
        threadslist.append(threadobj)
        threadobj.start()

    for threadobj in threadslist:
        threadobj.join()
   
   
    print('Finished')
    
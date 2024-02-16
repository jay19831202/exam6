# -*- coding: utf-8 -*-

import requests,bs4,os


url='https://www.xzw.com/fortune'
html=requests.get(url)
#print(html)
obj=bs4.BeautifulSoup(html.text,'lxml')
#print(obj)

loc1=obj.find('div',id='list')
loc2=loc1.find('div','alb').find_all('div')

#print(loc2)

pics=[]

newurl='https://www.xzw.com'

for items in loc2:
    pict=items.a.img['src']
    #print(pict)
    pics.append(newurl+pict)
    
#print(pics)
    
outdir='out0216/'
 

if os.path.exists(outdir)==False:
    os.mkdir(outdir)


    
print('已搜尋圖片總數：',len(pics))
for pic in pics:
    picture=requests.get(pic)
    picture.raise_for_status()
    print('%s 下載成功！！' % pic)

    pf=open(os.path.join(outdir,os.path.basename(pic)),'wb')
    
    for st in picture.iter_content(10240):
        pf.write(st)
    












    
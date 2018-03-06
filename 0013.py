def crawl_image(image_url,local_url):
    r = requests.get(image_url,stream=True)
    with open(local_url,'wb') as f:
        f.write(r.content)


def crawl_image_url():
    url = 'http://tieba.baidu.com/p/2166231880'
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html5lib')
    image_list = soup.find_all('div', class_='d_post_content_main')
    for child in image_list:
        image_urls = child.find_all('img')
        for tag in image_urls:
            if re.match('http://imgsrc.baidu.com/forum.*',tag['src']):
                crawl_image(tag['src'], 'd:\gakki\image\\' +
                            tag['src'].split('/')[-1])
        

if __name__ == '__main__':
    crawl_image_url()
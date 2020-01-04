from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

filename = "mobiles.csv"
f = open(filename, "w")
headers = "product_name, rating, specs\n"
f.write(headers)

for i in range(0, 200):
    url = 'https://www.flipkart.com/search?q=phones%20under%2030000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'+'&page='+str(i)
    print(url)
    client = req(url)
    html = client.read()
    client.close()
    page_soup = soup(html, "html.parser")
    containers = page_soup.findAll("div",{"class":"col col-7-12"})
    for container in containers:
        name_container = container.findAll("div", {"class":"_3wU53n"})
        product_name = name_container[0].text
        rate_container = container.findAll("div", {"class":"hGSR34"})
        if(not(rate_container)):
            rating = "none"
        else:
            rating = rate_container[0].text

        specs_container = container.findAll("ul", {"class":"vFw0gD"})
        specs = specs_container[0].text

        f.write(product_name.replace(",", "|") + "," +rating + "," +specs + "\n")
f.close()

















































#

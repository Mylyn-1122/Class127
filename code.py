from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("/Users/zhengmylyn/Library/CloudStorage/OneDrive-Personal/Documents/Games-coding/coding/Python/Classes/Class127/chromedriver2")
def scrape():
    headers=["Name","Light-Years_From_Earth","Planet_Mass","Stellar_Magnitude","Discorvery_Date"]
    planetData=[]
    for i in range(0,209):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.find_all("li")
            templist=[]
            for index,li_tag in enumerate(li_tags):
                if index ==0:
                    templist.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(li_tag.contents[0])
                    except:
                        templist.append("")
            planetData.append(templist)
        browser.find_element("xpath",'//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scraper2.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planetData)
scrape()
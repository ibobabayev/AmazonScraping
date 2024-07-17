from bs4 import BeautifulSoup
import requests
import datetime
import csv
import pandas as pd

url = 'https://www.amazon.com/Business-Computer-Touchscreen-NP964XGK-KG1US-Moonstone/dp/B0CVBH51YF/ref=sr_1_13?_encoding=UTF8&content-id=amzn1.sym.3b8e83c9-3c43-44b5-841c-814032918d4f&dib=eyJ2IjoiMSJ9.wlYu9TfVc_Y0Bon2kScQiourf--1lhNELUO6x6aYUTuhJF6zuuCJsI62Fe-m6gAhEPbVaAb-lVOkfAZGNe5b4Ak_9cqjGO5vcKRh0oeTRiJdk3QA9t29e_v-Rb2vb7cef5sm_Sg0daluuLoy9U1mgbUMIHLudlK3eZONSDRpJA9MbVS-SXHigecQGArh80Mmii8Z85nzdOnbHzFjQazc9qFvSaMW96V_0HdGqczLAas.Rx0dM9hvcqlgF5gVsWyuNTh1f6oPys_uZCTVD-4KXR4&dib_tag=se&keywords=computers&pd_rd_r=e8b45c27-0fbf-4d31-b7a5-c85eb64a01ee&pd_rd_w=X55kf&pd_rd_wg=CFDBH&pf_rd_p=3b8e83c9-3c43-44b5-841c-814032918d4f&pf_rd_r=B2S9WJEDR2C9SFGK84KD&qid=1721198194&refinements=p_n_deal_type%3A23566065011&sr=8-13&th=1'
page = requests.get(url)
soup1 = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id='productTitle').get_text().strip()
price = soup2.find(class_='a-price-symbol').get_text().strip() + soup2.find(class_='a-price-whole').get_text().strip()
today = datetime.datetime.now()

header = ['Title','Price','Date']
data = [title,price,today]

with open('AmazonScraping.csv','w',newline='',encoding='UTF8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerow(data)


df = pd.read_csv(r"C:\Users\User\PycharmProjects\pythonProject1\AmazonScraping.csv")
pd.set_option('display.max_columns',3)

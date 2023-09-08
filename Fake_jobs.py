import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://realpython.github.io/fake-jobs/")
print(response.status_code)
#print(response.content)

if response.status_code==200:
    soup=BeautifulSoup(response.content,"html.parser")
    #print(soup.head.title.text)
    lista_divs=soup.find_all("div",attrs={"class":"card-content"})
    #print(lista_div[0].prettify())

    data = {"Puesto":[],"Empresa":[], "Ciudad":[],"Fecha":[]}

    for div in lista_divs:
        puesto=div.find("h2",attrs = {"class":"title is-5"})
        company = div.find("h3",attrs={"class":"subtitle is-6 company"})
        city= div.find("p", attrs={"class": "location"})
        date = div.find("time")
        data["Puesto"].append(puesto.text)
        #print(puesto.text)
        #print(company.text)
        data["Empresa"].append(company.text)
        #print(city.text.strip())
        data["Ciudad"].append(city.text.strip)
        #print(date.text)
        data["Fecha"].append(date.text)
        #print(div.prettify())
        ##print("\n")

    #data_df=pd.DataFrame(data)
    #data_df.to_csv("jobs.csv")

    data_df = pd.DataFrame(data)
    data_df.to_csv("datasets/jobs.csv")
else:
    print(f"ERROR {response.status_code} AL MOMENTO DE CARGAR LA PAGINA")

jobs = pd.read_csv("datasets/jobs.csv",index_col=0)
print(jobs.sample(10))
print(jobs.describe())
print(jobs.info)



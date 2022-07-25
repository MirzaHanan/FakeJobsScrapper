import csv
import requests
from bs4 import BeautifulSoup
import csv


try:
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    print(page)


    soup = BeautifulSoup(page.content , "html.parser")
    # print(soup.prettify())

    results = soup.find(id="ResultsContainer")

    job_elements = results.find_all("div" , class_="card-content")
    # print(job_elements)

    field_names = ["job_title" ,"company_name" , " location"]

    with open("Joboffer.csv" ,"w" , newline='') as f:
        csv_writer = csv.writer(f , delimiter=",")
        csv_writer.writerow(field_names)
        # csv_writer.writeheader()

        for job_element in job_elements:
            job_title = job_element.find("h2" , "title")
            company_name = job_element.find("h3" , "subtitle")
            location = job_element.find("p" , "location")
            print(job_title.text.strip())
            print(company_name.text.strip())
            print(location.text.strip())
            print()
            csv_writer.writerow([job_title.text.strip() , company_name.text.strip() , location.text.strip()])

except Exception as e:
    print("*****************Exception Start*********************")
    print(e)
    print("*****************Exception End***********************")


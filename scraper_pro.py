from bs4 import BeautifulSoup
import requests
import pandas as pd

link="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page=requests.get(link)

browser=BeautifulSoup(page.content,"html.parser")

headers=["Name","Distance","Mass","Radius"]
star_data=[]

star_table=browser.find("table")

tr_tags=star_table.find_all("tr")
temp_list=[]

for tr_tag in tr_tags:
    td_tags=tr_tag.find_all("td")
    row=[i.text.rstrip() for i in td_tags]
    temp_list.append(row)
'''

    for index,td_tag in enumerate(td_tags):
        if index == 1:
            temp_list.append(td_tag.find_all("a")[1].contents[0])
        else:
            try:
                temp_list.append(td_tag.contents[0])
            except:
                temp_list.append("")
'''  

filtered_star_data=[]

# for i in range(1,len(star_data)):

star_name=[]
star_distance=[]
star_mass=[]
star_radius=[]

for index, data in enumerate(star_data):
    star_name.append(data[index][1])
    star_distance.append(data[index][3])
    star_mass.append(data[index][5])
    star_radius.append(data[index][6])

# print(filtered_star_data)
df=pd.DataFrame(list(star_name,star_distance,star_mass,star_radius), columns=['Star name','Star distance','Star mass','Star radius'])
df.to_csv("stardata.csv")



    
    



        



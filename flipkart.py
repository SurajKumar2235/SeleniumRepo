from selenium import webdriver
from selenium.webdriver.common.by import By
import json
drive = webdriver.Firefox()

# drive.maximize_window()

drive.get('https://www.flipkart.com/search?q=power+bank&sid=tyy%2C4mr%2Cfu6&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=power+bank%7CPower+Banks&requestId=5fdbe974-392e-489f-b5e4-6029cbfb594a&as-backfill=on')



dictonary={}
ls=[]

try:
        itmNAme=[]
        itmPrice=[]
        itmMRP=[]
        itmDis=[]
        itmRAT=[]
        itmPeople=[]
        for i in range(2,13):
            for j in range(1,5):

                try:
                    item_name=drive.find_element(By.XPATH,f'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[2]').text
                except:
                     item_name=''
                try:
                    item_price=drive.find_element('xpath',f'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div/div[1]').text
                except:
                    item_price=''
                try:
                    mrp_price_element=drive.find_element('xpath',f'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div/div[2]').text
                except:
                     mrp_price_element=""
                try:
                    discount=drive.find_element('xpath',f'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/a[3]/div/div[3]/span').text
                except:
                     discount=''
                try:
                    rating=drive.find_element('xpath',f'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div[3]/span[1]/div').text
                except:
                     rating=''
                try:
                    no_of_people_rated=drive.find_element(By.XPATH,f'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[{i}]/div/div[{j}]/div/div[3]/span[2]').text
                except:
                     no_of_people_rated=""

                print('--------------------------------------')
                print(item_name)
                print(item_price)
                print(no_of_people_rated)
                print(rating)
                print(mrp_price_element)
                print(discount)

                print('--------------------------------------')

                
                

                itmNAme.append(item_name)
                itmPrice.append(item_price)
                itmMRP.append(mrp_price_element)
                itmDis.append(discount)
                itmRAT.append(rating)
                itmPeople.append(no_of_people_rated)



except Exception as e:
     print(e)

finally:
    

    drive.quit()    
    dictonary={
                    "item Name":itmNAme,
                    "Item Price":itmPrice,
                    "Item MRP":itmMRP,
                    "Item Discount":itmDis,
                    "Item Rating":itmRAT,
                    "No. People rated":itmPeople
        }
                
    with open("/home/suraj/Desktop/Django/webscraping/flipData.json", 'r') as fp:
        users = json.load(fp)
    # Step 1: Read the JSON file into a dictionary object
    

    # Step 2: Append the new dictionary to the existing dictionary object
    
    users['page 1']=dictonary

    # Step 3: Write the updated dictionary object back to the JSON file
    with open('/home/suraj/Desktop/Django/webscraping/flipData.json', 'w') as fp:
         json.dump(users, fp, indent=4)


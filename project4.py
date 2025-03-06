from requests_html import HTMLSession
import json
import decimal
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# session = HTMLSession()
driver = webdriver.Chrome()

URL = "https://www.espguitars.com/guitars"
driver.get(URL)
sleep(1)
# resp = session.get(URL)
#print(resp)
# resultElements = driver.find_elements(By.XPATH, "//div[contains(@class, 'product content-item')]")
aGuitars = {}
for page in range(3):
    guitars = {}
    print(f"Loading page {page + 1}")
    sleep(1)
    resultContainer = driver.find_element(By.XPATH, "//div[@class = 'content-items']")
    resultElements = resultContainer.find_elements(By.XPATH, "//div[contains(@class, 'product content-item')]")
    nextButtonContainer = driver.find_element(By.XPATH, "//div[@class = 'pagination']")
    for card in resultElements:
        guitar = {}
        # sleep(.1)
        titleName = card.find_elements(By.XPATH, ".//h4/a")
        if len(titleName) == 1:
            #print(titleName[0].text)
            guitar["name"] = titleName[0].text
        else:
            print("Name: Too many elements")
        # sleep(.1)
        color = card.find_elements(By.XPATH, ".//h5")
        if len(color) == 1:
            #print(color[0].text)
            guitar["color"] = color[0].text
        else:
            print("Color: Too many elements")
        # sleep(.1)
        price = card.find_elements(By.XPATH, ".//div[@class='price']")
        if len(price) == 1:
            #print(price[0].text)
            priceN = price[0].text.strip('$').replace(',','')
            guitar["price"] = priceN
        else:
            print("Price: Too many elements")
        # sleep(.1)
        guitarID = card.get_attribute('data-content-id')
        productlink = card.find_elements(By.XPATH, ".//h4/a")
        link = productlink[0].get_attribute('href')
        guitar["link"] = link
        # guitar["ID"] = guitarID
        guitars[guitarID] = guitar
        with open(f"products_page{page + 1}.json", "w+", encoding='utf-8') as f:
            json.dump(guitars, f, indent=4)
        # sleep(2)
        nextButton = nextButtonContainer.find_elements(By.XPATH, ".//ul[@class='pagination']/li[@class = 'next next_page ']/a[@rel='next nofollow']")
        # nextButton[0].click()
        nextButtonLink = nextButton[0].get_attribute('href')
        # sleep(1)
    print(f"Page {page + 1} has {len(resultElements)} products")
    aGuitars.update(guitars)
    # with open(f"products_page{page + 1}.json", "w+", encoding='utf-8') as f:
    #     json.dump(guitars, f, indent=4)
    driver.get(nextButtonLink)
n = 1

for page in range(3):
    with open(f"products_page{page + 1}.json", "r", encoding='utf-8') as f:
            aGuitars = json.load(f)
    for key in aGuitars:
        link = aGuitars[key]["link"]
        driver.get(link)
        sleep(.5)
    
        imageLink = driver.find_elements(By.XPATH, "//div[@class = 'item active']/a")
        image = imageLink[0].get_attribute('href')
        aGuitars[key]["image"] = image
    
        description = driver.find_elements(By.XPATH, "//div[@class = 'body section']/p")
        if len(description) == 0:
            description = driver.find_elements(By.XPATH, "//div[@class = 'body section']")
        aGuitars[key]["description"] = description[0].text
    
        notice = driver.find_elements(By.XPATH, "//div[@class = 'store_notice']")
        aGuitars[key]["notice"] = notice[0].text if notice else "Not Defined"
    
        productInfoBlock = driver.find_element(By.ID, "specifications")
    
        scale = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Scale']/span[2]")
        aGuitars[key]["scale"] = scale[0].text if scale else "Not Listed"
    
        body = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Body']/span[2]")
        aGuitars[key]["body"] = body[0].text if body else "Not Listed"
    
        neck = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Neck']/span[2]")
        aGuitars[key]["neck"] = neck[0].text if neck else "Not Listed"
    
        fingerboard = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Fingerboard']/span[2]")
        aGuitars[key]["fingerboard"] = fingerboard[0].text if fingerboard else "Not Listed"
    
        fingerboardRadius = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Fingerboard Radius']/span[2]")
        aGuitars[key]["fingerboard radius"] = fingerboardRadius[0].text if fingerboardRadius else "Not Listed"
    
        bridge = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Bridge']/span[2]")
        aGuitars[key]["bridge"] = bridge[0].text if bridge else "Not Listed"
    
        bridgePU = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Bridge PU']/span[2]")
        aGuitars[key]["bridge pickup"] = bridgePU[0].text if bridgePU else "Not Listed"
    
        electronics = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Electronics ']/span[2]")
        aGuitars[key]["electronics"] = electronics[0].text if electronics else "Not Listed"
    
        strings = productInfoBlock.find_elements(By.XPATH, "//div[@data-content-detail-type = 'Strings']/span[2]")
        aGuitars[key]["strings"] = strings[0].text if strings else "Not Listed"
        print(f"guitar {n} written")
        # aGuitars.update(guitars)
        n += 1
    with open(f"products_page{page + 1}.json", "w+", encoding='utf-8') as f:
        json.dump(aGuitars, f, indent=4)
    print(f"All guitars written to dictionary {page + 1}")
# with open("aggregated_products.json", "w+", encoding='utf-8') as f:
#     json.dump(aGuitars, f, indent=4)

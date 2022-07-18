from selenium.webdriver import Chrome
import pandas as pd



df = pd.read_excel("customer_database.xlsx")


driver = Chrome()

for i in range(0,1):
    print(df.columns)
    # first_name = df.loc[i,"First name (Optional)"]
    # last_name = df.loc[i,"Last Name (Required if company is not provided)"]

    first_name = "Elizabeth A"
    last_name = "Hensell"
    city = "Brookline"
    state = "MA"

    print(first_name)
    print(last_name)
    print(city)

    search_url = f"https://www.truepeoplesearch.com/results?name={first_name}%20{last_name}&citystatezip={city},{state}"
    print(search_url)

    driver.get(search_url)


    input("Check if Captcha")
    people = driver.find_elements_by_xpath("//div[@class='card card-body shadow-form card-summary pt-3']") 
    view = people[0].find_element_by_xpath(".//a")
    view.click()
    input("Check if Captcha")
    f = dict()
    f['name'] = driver.find_element_by_xpath("//span[@class='h2']").text

    f['address'] = driver.find_element_by_xpath("//div[contains(text(),'Current Address')]/parent::div/parent::div/parent::div//a[@*='address']").text

    wireless = driver.find_elements_by_xpath("//div[contains(text(),'Phone Numbers')]/parent::div/parent::div/parent::div//span[text()='Wireless']/parent::div/a")
    wireless_numbers = []
    for wl in wireless:
        wireless_numbers.append(wl.get_attribute('innerHTML'))
    
    f['wireless'] = ", ".join(wireless_numbers)
    
    lind_line = driver.find_elements_by_xpath("//div[contains(text(),'Phone Numbers')]/parent::div/parent::div/parent::div//span[text()='Landline']/parent::div/a")
    lind_line_numbers = []
    for wl in lind_line_numbers:
        lind_line_numbers.append(wl.get_attribute('innerHTML'))    
    f['landline'] = ", ".join(lind_line_numbers)


    emails = driver.find_elements_by_xpath("//div[contains(text(),'Email Addresses')]/parent::div/parent::div/parent::div//div[@class='content-value']")
    email_ids = []
    for wl in emails:
        email_ids.append(wl.get_attribute('innerHTML'))    
    f['emails'] = ", ".join(email_ids)

    print(f)


    
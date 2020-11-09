
# this file takes a list of linkedIn sales Navigator profiles, and outputs a 'results.txt' file with names and follower counts of the profiles. 
# firstly it naviagtes to their linkedIN public page, 

# Chromedriver not in path? 
# to install chromedriver and add it to $path : '/usr/local/bin/chromedriver', use `brew cask install chromedriver` in terminal. 

# error options 
# SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 86
# Current browser version is 85.0.4183.121 with binary path /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
# https://stackoverflow.com/questions/60296873/sessionnotcreatedexception-message-session-not-created-this-version-of-chrome

# pip install webdriver-manager



from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from parsel import Selector


# specifies the path to the chromedriver.exe make sure this points to the web driver. add webdriverpat to $path.

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome('/usr/local/bin/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# identify the username field and send the username
username = driver.find_element_by_id("session_key")
username.send_keys("finn.rothacker@gmail.com")

# identify the password field in browser and send
password = driver.find_element_by_id("session_password")
password.send_keys("getMeLinkedIn8")

# identify the log in button in browser and click it
log_in_button = driver.find_element_by_class_name(
    "sign-in-form__submit-button")
log_in_button.click()

navigator_profiles = [
"https://www.linkedin.com/sales/people/ACwAAAvZ8T4BC3zb-1lp6cEcx2ORfX6-ChRyzY4,NAME_SEARCH,qj94",
"https://www.linkedin.com/sales/people/ACwAAAb7cp8Bl1C_MKp6YzCrQNRVM8tT6GwAe9M,NAME_SEARCH,CJtN",
"https://www.linkedin.com/sales/people/ACwAAAQyz38BvmhJuX4iFFrJTHDitGYS4TGa2wY,NAME_SEARCH,0kJX",
"https://www.linkedin.com/sales/people/ACwAAArNMFEBjFi_NRgqArU_Y82csR0SBdX9sUA,NAME_SEARCH,U-Sk",
"https://www.linkedin.com/sales/people/ACwAAAA2Vf4BRuMOthDb0Q8A1DoZGigNV4x8DPA,NAME_SEARCH,4E0X",
"https://www.linkedin.com/sales/people/ACwAAACGG-4Bjb79oblgzlH-DXss1yDBHYMbtRs,NAME_SEARCH,tehp",
"https://www.linkedin.com/sales/people/ACwAABcwL94BqCKM6mRXTpp1dB5UZaJYG7XdonU,NAME_SEARCH,kDk7",
"https://www.linkedin.com/sales/people/ACwAAAHtuS8Bz4c8MR1DKQuKzOyGQSZYkXV4sDM,NAME_SEARCH,ADBr",
"https://www.linkedin.com/sales/people/ACwAABEdlEQBeHlooE8E1VvL4-WdFEUqe07ZF5c,NAME_SEARCH,41TA",
"https://www.linkedin.com/sales/people/ACwAAALEvkEB96NEPGemZGMGPLXuW7W0Tr2lkBA,NAME_SEARCH,W9sQ",
"https://www.linkedin.com/sales/people/ACwAAAAiKccBzsfjyepLcp9k_ZG1cYCddM3MKcM,NAME_SEARCH,MFfg",
"https://www.linkedin.com/sales/people/ACwAAAFG6qMB0c4ZO0RE36v1hpk7DDMPxpg6Pr8,NAME_SEARCH,x8G3",
"https://www.linkedin.com/sales/people/ACwAAAjXbn8BqMLOIIA7jx1cNIrvyOrRGAnkJrA,NAME_SEARCH,9TH7",
"https://www.linkedin.com/sales/people/ACwAAALrs8MBT7LtnLzX-iNeR90rYG9I9VZnC2w,NAME_SEARCH,yoCO",
"https://www.linkedin.com/sales/people/ACwAAACAjtYBMfIdb84cFpRFWEsXjsSKosVQ5XE,NAME_SEARCH,s4dI",
"https://www.linkedin.com/sales/people/ACwAAAm8OZsB7pfUNP_lV_tn6cULELgZwWcEpvU,NAME_SEARCH,_sxq",
"https://www.linkedin.com/sales/people/ACwAAADeDhIBuBJ8aV2p4Vv50_PZvzg8tzR3SdI,NAME_SEARCH,BPF8",
"https://www.linkedin.com/sales/people/ACwAAAk-wi4BzOFSo5OhHxqgkXYoX2JfMPyI7Zw,NAME_SEARCH,cXGB",
"https://www.linkedin.com/sales/people/ACwAAATpRAIBz-UG4j0qVbYyyQmU68FDqW3y_mo,NAME_SEARCH,juyU",
"https://www.linkedin.com/sales/people/ACwAAAVjUdMBGLFKmYm5IPIHsXRpwtsbPLRaJUQ,NAME_SEARCH,F7kv",
"https://www.linkedin.com/sales/people/ACwAAAa1CikBNdH3nTSbn8EyXfMBHqoZH7GBvdg,NAME_SEARCH,Am_c",
"https://www.linkedin.com/sales/people/ACwAAAAC9ooBfmz0ASN6FOvhDuhu2XhF-cMD62w,NAME_SEARCH,9D22",
"https://www.linkedin.com/sales/people/ACwAAAAevvUBnpSqZwWcvThktMr3-_bqPDOGAkA,NAME_SEARCH,ASPE",
"https://www.linkedin.com/sales/people/ACwAAAcN2bABA_Q7yRex5aVhn_wML2_D8a2ud5U,NAME_SEARCH,lZ3M",
"https://www.linkedin.com/sales/people/ACwAAAtFy0UBkLEQrCMOEDcRBk5oUvZv0R37Gvk,NAME_SEARCH,SwZ7",
"https://www.linkedin.com/sales/people/ACwAAAD3McIBrCUq2Q5AUyTuOMhXSD6mMiOOcII,NAME_SEARCH,SA5X",
"https://www.linkedin.com/sales/people/ACwAAALPTFcB2utdqhMwyZr6ZK2gejbHvNxoJhE,NAME_SEARCH,mKHa",
"https://www.linkedin.com/sales/people/ACwAAAg9AcYBrBcTJA0eF23EsUMHCYiqi9T42xY,NAME_SEARCH,vjUN",
"https://www.linkedin.com/sales/people/ACwAACGOU-sBsq9hLiweRrO8OiwULKirEgZOsIU,NAME_SEARCH,3-F4",
"https://www.linkedin.com/sales/people/ACwAAAFlGfQBOlvnXIgUgjEMbOw7SQR8r5xYpbU,NAME_SEARCH,uotF",
"https://www.linkedin.com/sales/people/ACwAAAWyW1UBcF7nIHa-O1wy7xisvA6Q8Dsds-o,NAME_SEARCH,gVED",
"https://www.linkedin.com/sales/people/ACwAACUgCDIBRXb3baOpMer3RgbD-CQ2puXZrF4,NAME_SEARCH,bOpE",
"https://www.linkedin.com/sales/people/ACwAAAxHXwYBSQP3HYp3Itq5p8wo-K5CkgqjN-4,NAME_SEARCH,dhA3",
"https://www.linkedin.com/sales/people/ACwAAADX3wMBXNEbWUxWLsybIZLJvSBdzr0_eEo,NAME_SEARCH,XO8X",
"https://www.linkedin.com/sales/people/ACwAABPc0zcBJwL3ry5E3YuRXwcNbCZlaH5kqEw,NAME_SEARCH,NNnx",
"https://www.linkedin.com/sales/people/ACwAAAf8tJkBTlInlYH6JwsLOh0ooeMQvv34-PU,NAME_SEARCH,j1RB",
"https://www.linkedin.com/sales/people/ACwAAALZMzEBGdqMxg8VueUXAD34pdEE3BBuMZM,NAME_SEARCH,eRqb",
"https://www.linkedin.com/sales/people/ACwAAABmFCMBnWifbMm2EMtcGwTo2NelRjnga6U,NAME_SEARCH,hdxC",
"https://www.linkedin.com/sales/people/ACwAAALpvpcBuUbTexLJ_GUdNMZOqDURD8ebpj0,NAME_SEARCH,um2P",
"https://www.linkedin.com/sales/people/ACwAABAISswBvMkvo3U47sAcJ1BqRnAdAyzSPt8,NAME_SEARCH,yBkS",
"https://www.linkedin.com/sales/people/ACwAAAXVDAEB7jsi_-QLDPLbgloh_Fr_UwNhOnE,NAME_SEARCH,YKsf",
"https://www.linkedin.com/sales/people/ACwAAAZICi0Bvc8bnLm7VNtjk-7g5NCHXdkkETg,NAME_SEARCH,ed-3",
"https://www.linkedin.com/sales/people/ACwAAAhypsABmcZFfoAZlv01M611yTkBv5OqH2M,NAME_SEARCH,OVmq",
"https://www.linkedin.com/sales/people/ACwAACGI8BABBhFuni7tktjH9Fc7B_nOonqU2EA,NAME_SEARCH,7OjW",
"https://www.linkedin.com/sales/people/ACwAAALqvPsBn-RQyLExFuIpxCRnOfzgl78kIsk,NAME_SEARCH,qZUj",
"https://www.linkedin.com/sales/people/ACwAAAEM4f4BhZoYY3BijNyuzRNS2k2_xWH-_c4,NAME_SEARCH,XVtG",
"https://www.linkedin.com/sales/people/ACwAAARa1a4BR8J4XnIht4fpuCJdDE0DBh1wBww,NAME_SEARCH,H5G9",
"https://www.linkedin.com/sales/people/ACwAAAgM4joBHCh8TU0IwO4W2Yz9vjkSRjZz0ZE,NAME_SEARCH,INVR",
"https://www.linkedin.com/sales/people/ACwAACfgX2QB074jcBusY0IS8BTr1okiXydmDCI,NAME_SEARCH,tpaz",
"https://www.linkedin.com/sales/people/ACwAABZ3KGEBM5kpzh4YJmQ_HFImHA54BHEmuso,NAME_SEARCH,_iiI",
"https://www.linkedin.com/sales/people/ACwAAAePGyQBpB7ROGwU_MPab8hba1ucDNP3_F4,NAME_SEARCH,Q0Ck",
"https://www.linkedin.com/sales/people/ACwAAAAZ_EUB4mV0mXi4-KuxmRwAhatnP68V5KI,NAME_SEARCH,IMYY",
"https://www.linkedin.com/sales/people/ACwAAA4XORcBI5QSAObIL-oRHSUP9ip5bpvoxLQ,NAME_SEARCH,gbSs",
"https://www.linkedin.com/sales/people/ACwAAA_yNgEB2x77ApNxqkLQHSXnVVDyFaGk9Xc,NAME_SEARCH,8O7k"]


# loop over Navigator profiles
# for profile in navigator_profiles:

# get the profile
# NOTE this script uses linkedIn sales navigator profile links. the 3 dot menu, and go to linked in, is to return to the normal linkedIN.

followers_results = []

# For loop to iterate over each URL in the list
for linkedIn_url in navigator_profiles:

    # get the profile URL
    try:
        driver.get(linkedIn_url)
    except:
        print("Could not view the LinkedIn URL")
    sleep(5)

    # If using normal linkedIn profile links, there is no need for three_dots and view_on_linkedIn to be clicked
    # get the 3 dot menu
    try:
        three_dots = driver.find_element_by_xpath(
        "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div[3]/button")
    except:
        print("Could not find the three dots element")
    try:
        three_dots.click()
    except:
        print("Could not click the three dots element")

    sleep(2)
    # click the "view on linkedIn button"
    try: 
        view_on_linkedIn = driver.find_element_by_xpath(
        "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div/div/div/div[1]/div/ul/li[3]/div")
    except: 
        print("could not find the 'view on linkedIn.com' button")
    
    try:
        view_on_linkedIn.click()
    except:
        print("Could not click 'view on linkedIn.com' button")
    sleep(4)
    # ------------ We are now on a public linkedIn Profile -------------
    # follower count in only displayed on the linkedIn public profile.

    # switch Selenium focus to new tab
    try:
        driver.switch_to.window(driver.window_handles[1])
    except:
        print("Could not switch to new window")
    sleep(1)

    # find name
    name_element_paths = ["/html/body/div[9]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]","/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]",
                        "/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]", "/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]","/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div/dl/dt/span"]

    #  loop through the different possible x-paths to the account
    for xpath in name_element_paths:
        try: 
            name = driver.find_element_by_xpath(xpath).text
        except:
            name = "Could not find name"
        if name != "Could not find name":
            break
    print(name)

    # scroll down so dynamic elements load
    driver.execute_script("window.scrollTo(0, 1000)")
    sleep(3)


    followers_element_paths = ["/html/body/div[9]/div[3]/div/div/div/div/div[2]/main/div[2]/div[4]/div/section/h3/span","/html/body/div[9]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/div/section/h3/span","/html/body/div[9]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/div/section/h3/span","/html/body/div[9]/div[3]/div/div/div/div/div[2]/main/div[2]/div[4]/div/section/h3/span","/html/body/div[9]/div[3]/div/div/div/div/div[2]/main/div[2]/div[4]/div/section/h3/span",'//*[@id="ember201"]/span',"/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[2]/div[5]/div/section/h3/span","/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[2]/div[4]/div/section/h3/span"]

    #  loop through the different possible x-paths to the account
    for xpath in followers_element_paths:
        try: 
            followers = driver.find_element_by_xpath(xpath).text
        except:
            followers = "Could not find followers"

        if followers != "Could not find followers":
            break
    
    print(followers)
    sleep(1)



    # add name and followers to results.
    followers_results = followers_results + [name + " : " + followers]
    print(followers_results)
    print(followers_results.count)
    print("-----")

    # close tab
    try: 
        driver.close()
    except: 
        print("could not close the tab")
   
    # Switch focus to the next tab
    try: 
        driver.switch_to.window(driver.window_handles[0])
    except: 
        print("could not switch selenium focus the next tab")

    sleep(30)

driver.quit()


# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #
# --------------------------------------- #

# # find name
# name_element_paths = ["/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]",
#     "/html/body/div[8]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]","/html/body/main/div[1]/div[2]/div/div[1]/div[1]/div/dl/dt/span"]

# #  loop through the different possible x-paths to the account
# for xpath in name_element_paths:
#     try: 
#         name = driver.find_element_by_xpath(xpath).text
#     except:
#         name = False


#     if name != False: 
#         break
# print(name)

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
# from parsel import Selector


# # specifies the path to the chromedriver.exe make sure this points to the web driver. add webdriverpat to $path.

# driver = webdriver.Chrome(ChromeDriverManager().install())

# # driver.get method() will navigate to a page given by the URL address
# # driver.get('https://www.linkedin.com')

# # identify the username field and send the username
# username = driver.find_element_by_id("session_key")
# username.send_keys("finn.rothacker@gmail.com")

# # identify the password field in browser and send
# password = driver.find_element_by_id("session_password")
# password.send_keys("getMeLinkedIn8")

# # identify the log in button in browser and click it
# log_in_button = driver.find_element_by_class_name(
#     "sign-in-form__submit-button")
# log_in_button.click()


# # create a list of developer profiles
# names = ["Eeshan Kulkarni", "Cameron Price", "Christopher Anthony", "Damian Hajda", "Emilie Palamy	Pradichit", "Aliyya Shelley Mattos", "Sofien Askri", "Nagore Moran-Llovet", "Robyn Schryer Fehrman", "Payal Mulchandani", "Simon Faivel", "David Jack", "Matthew Allen", "Andrew Fergusson", "Lyndsey McKee", "Reece Proudfoot", "Cindy Mitchell", "lee cooper", "Peter Ball", "Cheryl Croce", "Tess Ariotti", "Sarah Gun", "Tom C.", "Caroline Lambert", "Christian Paul	Stenta", "Janine Owen", "Sarah Davies AM", "Tony Hagan", "Michael S.	Duggan", "Shane Smith", "Vita Maiorano", "Simon Marial", "Stuart Lloyd-Hurwitz", "Sharene Jackson", "Rez Haremi", "Tom Tolchard", "Suzie Riddell", "Pat Ryan", "Kate Saunders", "Min Seto", "Anna Crabb", "Shanil Samarakoon", "Alan Morgan", "David Pugh", "Cory J.	Steinhauer", "Patrick O'Callaghan", "Doug Taylor",
#          "Amanda Barnes (she/her) JP", "Karen Bolinger", "Ali Sumner", "Monique Isenheim", "Katie Liew", "Sharon Grocott", "Jemma Arundel", "Karina Rosa	Ojeda Rodriguez", "Gillian Turnbull", "Greg Twemlow", "Daisy Gardener", "Linda Fitzhardinge FAICD", "Duncan Ward", "Sani Dowa", "Usman Iftikhar", "Michael E.", "Elizabeth Knight", "Eeshan Kulkarni", "Cameron Price", "Christopher Anthony", "Damian Hajda", "Emilie Palamy	Pradichit", "Aliyya Shelley Mattos", "Sofien Askri", "Nagore Moran-Llovet", "Robyn Schryer Fehrman", "Payal Mulchandani", "Simon Faivel", "David Jack", "Matthew Allen", "Andrew Fergusson", "Lyndsey McKee", "Reece Proudfoot", "Cindy Mitchell", "lee cooper", "Peter Ball", "Cheryl Croce", "Tess Ariotti", "Sarah Gun", "Tom C.", "Caroline Lambert", "Christian Paul	Stenta", "Janine Owen", "Sarah Davies AM", "Tony Hagan", "Michael S.	Duggan", "Shane Smith", "Vita Maiorano", "Simon Marial", "Stuart Lloyd-Hurwitz", "Sharene Jackson", "Rez Haremi", "Tom Tolchard", "Suzie Riddell", "Pat Ryan", "Kate Saunders", "Min Seto", "Anna Crabb", "Shanil Samarakoon", "Alan Morgan", "David Pugh", "Cory J.	Steinhauer", "Patrick O'Callaghan", "Doug Taylor", "Amanda Barnes (she/her) JP", "Karen Bolinger", "Ali Sumner", "Monique Isenheim", "Katie Liew", "Sharon Grocott", "Jemma Arundel", "Karina Rosa	Ojeda Rodriguez", "Gillian Turnbull", "Greg Twemlow", "Daisy Gardener", "Linda Fitzhardinge FAICD", "Duncan Ward", "Sani Dowa", "Usman Iftikhar", "Michael E.", "Elizabeth Knight", ]

# navigator_profiles = ["https://www.linkedin.com/sales/people/ACwAAAc1lKUBe7oG156PVWB5ylvSR_c2WwQ7Fh4,NAME_SEARCH,FyHc", "https://www.linkedin.com/sales/people/ACwAAAhRW9wBPF50cvPeoyYmTGfXzn1Lke8-0vQ,NAME_SEARCH,yZ-y", "https://www.linkedin.com/sales/people/ACwAAADVV9EBR5PVfUTywQglCsPeVPPxnFLfi7M,NAME_SEARCH,P1kc", "https://www.linkedin.com/sales/people/ACwAAAFwHqABLG10JhBYdvx96boalU6XpbUG4t8,NAME_SEARCH,RcSQ", "https://www.linkedin.com/sales/people/ACwAAAg1V9IBZqBP3HfoLts4U9RF5opU23aXAGQ,NAME_SEARCH,y8iQ", "https://www.linkedin.com/sales/people/ACwAAAH8-dUBfDUsbjg4eyqHewmy0K2M-P_3aPE,NAME_SEARCH,XrGG", "https://www.linkedin.com/sales/people/ACwAAAJuevAB2bgZEQOuRgNrOc4tr7Ngho3yvtY,NAME_SEARCH,c9t0", "https://www.linkedin.com/sales/people/ACwAABH2BZwB17bk2W-ORyg6zJ4cKtWKQyFepVQ,NAME_SEARCH,a7e7", "https://www.linkedin.com/sales/people/ACwAAAEXPPIBu2fdtJihH0sv1noirtM4vYwnV6Q,NAME_SEARCH,l9x3", "https://www.linkedin.com/sales/people/ACwAAAGG2mEB0APVB1oyyGMsPlfwHzGBaC2DjyE,NAME_SEARCH,xP1i", "https://www.linkedin.com/sales/people/ACwAAACd-l8BE40xls8Dhfh6WFv19Myv5MUnQxg,NAME_SEARCH,ygpK", "https://www.linkedin.com/sales/people/ACwAAAZLnuEBBmBNzBvd1xbtOkoFmcIQ9dqW1qs,NAME_SEARCH,FJOl", "https://www.linkedin.com/sales/people/ACwAAA6704IBVxkx78gTRU7vueZSe2a_rQeqv8c,NAME_SEARCH,bCSB", "https://www.linkedin.com/sales/people/ACwAAAdHeP0BuHP6kO4_DjY4LCt3HH8Knxm18K0,NAME_SEARCH,S3aU", "https://www.linkedin.com/sales/people/ACwAAAREvxkBA8y7NIdSPajpT_mwm5QlqYhpgl4,NAME_SEARCH,BTTS", "https://www.linkedin.com/sales/people/ACwAAAIwQxkBqhGnj33SJtnl8xIH6ut2b2BNIPQ,NAME_SEARCH,wQeg", "https://www.linkedin.com/sales/people/ACwAAAEtXC4BnQY5cxghoh0qB4xlN3COkyiKClA,NAME_SEARCH,bP7V", "https://www.linkedin.com/sales/people/ACwAAAmVUMIBKusqFB8Bhq2_Rp57T-e4GxcqDd0,NAME_SEARCH,CFU4", "https://www.linkedin.com/sales/people/ACwAAAC-D38BOVyDuocOSG2-gxjyUr2TIKiSZmk,NAME_SEARCH,2DjF", "https://www.linkedin.com/sales/people/ACwAAAhLB0UBruwSDiU-pIM5J3yKHqLdRLXVSyU,NAME_SEARCH,CQVz", "https://www.linkedin.com/sales/people/ACwAAAww78QBx9Jnxe1Bs_nIfjbD9uecgcMsxUk,NAME_SEARCH,6_qa", "https://www.linkedin.com/sales/people/ACwAAAWNfLYB7x-5JgVJ8RK4ImXF162KQdgDijg,NAME_SEARCH,qqpx", "https://www.linkedin.com/sales/people/ACwAAB-nIdQBh5lzrSSWiDZG8uqOyu-lA8m8Leo,NAME_SEARCH,w5o2", "https://www.linkedin.com/sales/people/ACwAAA6WUl0B-yh8hTM5ug4cI2MToxlHEDtPJtc,NAME_SEARCH,8wCs", "https://www.linkedin.com/sales/people/ACwAAAOjk2wBjykfmfUc0mOuBrVCZmfZeLUWr-I,NAME_SEARCH,zN0S", "https://www.linkedin.com/sales/people/ACwAABBxw28BvhXEKwChTG9DKVaIE_22Qg8f5fM,NAME_SEARCH,Mbs5", "https://www.linkedin.com/sales/people/ACwAAAHqY_YB-OX8YySEnghKLT0isaCwWXlb838,NAME_SEARCH,ViiI", "https://www.linkedin.com/sales/people/ACwAAAMLPMABlpz8Nuf91IeH7szYRfD2NZsYQYM,NAME_SEARCH,gi6_", "https://www.linkedin.com/sales/people/ACwAAAFxtv4B2YkOQo5QCVX7JN4bWvvbL08etBU,NAME_SEARCH,U7G4", "https://www.linkedin.com/sales/people/ACwAAA5nGcgB_FHdFIirbL4zJcPR9rlkqHt_4S0,NAME_SEARCH,eVwO", "https://www.linkedin.com/sales/people/ACwAAAnt1hQB8EHU7LmZ4ua-t5Ngv142NPSg-1o,NAME_SEARCH,N0bd", "https://www.linkedin.com/sales/people/ACwAAC-Fg3gBNraTcmj2r01Z1ti--yF6KNr0YGE,NAME_SEARCH,JXrA", "https://www.linkedin.com/sales/people/ACwAAAByDNQBiHHem3xYZo1nRSuwdKIpa0fwDMw,NAME_SEARCH,UFNt", "https://www.linkedin.com/sales/people/ACwAAAdzokkB59WA8d8QrNvSP6u8nHzYl5JZ1G8,NAME_SEARCH,a3Sz", "https://www.linkedin.com/sales/people/ACwAAAEbK1oBy_ByPOWCU3UeHBIsYAJFT4CF08I,NAME_SEARCH,RxPA", "https://www.linkedin.com/sales/people/ACwAAACpafsBAY8I7VZ1uen6sTrJhK8dnyZO2ic,NAME_SEARCH,guCL", "https://www.linkedin.com/sales/people/ACwAAANkpkIB7uejuUqEwP2CQ-wK4RncjIBUSJ8,NAME_SEARCH,tmXH", "https://www.linkedin.com/sales/people/ACwAAA1ApicBbHcRrtZFhl9Kx5zmOKogi9oQGjg,NAME_SEARCH,NsjR", "https://www.linkedin.com/sales/people/ACwAAAQ5rdgB0PzA-nTgj2IPsUnAF3jrPUmuAT8,NAME_SEARCH,NqVP", "https://www.linkedin.com/sales/people/ACwAAASzzTMBORIZM5ZAp7wAq3skkWkoLL5_iEM,NAME_SEARCH,-dsp", "https://www.linkedin.com/sales/people/ACwAAANIxxcB7exbXzQwGUgN7CEdqAJN_tEnBw8,NAME_SEARCH,J_GT", "https://www.linkedin.com/sales/people/ACwAAAQWo-0BR2S891BBXi1THWv0JySUpDtMWJg,NAME_SEARCH,WqEk", "https://www.linkedin.com/sales/people/ACwAAAPJG_4Bk73ijBfd4Q0ntPiePEJs594EjDU,NAME_SEARCH,hcg2", "https://www.linkedin.com/sales/people/ACwAAAUwsu4BxsnK6uVCSr0NJ_dBkwMFaH-76fc,NAME_SEARCH,jq1I", "https://www.linkedin.com/sales/people/ACwAAA3HFbABfbBB0LAUzw5grqga6kRvxRlnZmY,NAME_SEARCH,ASGF", "https://www.linkedin.com/sales/people/ACwAAAaT4xkB4n0-UzZ4UNYgIpeEa1cMcaw2BIE,NAME_SEARCH,tCdp", "https://www.linkedin.com/sales/people/ACwAAAZQ0c4BOKidOav2W9C2COlVSZj5dQJD4D4,NAME_SEARCH,tcNO", "https://www.linkedin.com/sales/people/ACwAAAQuxFYBbZ4ivTkf1U9xFTpIGEpVQuenaX4,NAME_SEARCH,oEcU", "https://www.linkedin.com/sales/people/ACwAAAFeLoMBANUt1az1aZi_-69wg0zbmpB9zas,NAME_SEARCH,hxwm", "https://www.linkedin.com/sales/people/ACwAAAFCyGABtwIFmNjW69mNgDMqN4dOla6qFDw,NAME_SEARCH,v6-w", "https://www.linkedin.com/sales/people/ACwAAAIPwCABcc2RZJEXNoZGOlcRD4T0YLGig7I,NAME_SEARCH,8FUz", "https://www.linkedin.com/sales/people/ACwAAA46I5EBjxh9nuAjBUhCbG8BHDLewRNOtx8,NAME_SEARCH,SfMp", "https://www.linkedin.com/sales/people/ACwAAA_drXYBFMzf8M8MVEIkvsCrupxdxzgtMAM,NAME_SEARCH,9M2Z", "https://www.linkedin.com/sales/people/ACwAAArssMcBpSooQhh8gATWdnbosLtyxHQk_o0,NAME_SEARCH,s7pY", "https://www.linkedin.com/sales/people/ACwAABARv4YBGpdwNZqlNDs42bxW4ygVi42lXFA,NAME_SEARCH,76d6", "https://www.linkedin.com/sales/people/ACwAAAIciAkBPes6WrlZradz4vnEARxQOhVoSg8,NAME_SEARCH,kU27", "https://www.linkedin.com/sales/people/ACwAAAEBvw0BGXD-u5SzG7abWZaLK0clGgxgnZ4,NAME_SEARCH,gS2X", "https://www.linkedin.com/sales/people/ACwAAAyZk_cBF3Xd50SboStaOk3nDNUEP2ZP_Ds,NAME_SEARCH,9aPk", "https://www.linkedin.com/sales/people/ACwAAAP1yYwBTNRCh0lrvaiEThqiG0AcLx7P_-w,NAME_SEARCH,sEYa", "https://www.linkedin.com/sales/people/ACwAAABaGoIBri4ZJIZi_SAbysNzI5ang1TMHxY,NAME_SEARCH,W0Al", "https://www.linkedin.com/sales/people/ACwAAAI7CcsBSZUYHSYDfEhiE87ZCXEO9OxRkBQ,NAME_SEARCH,a9N7", "https://www.linkedin.com/sales/people/ACwAAAXNcioB5UpMofQ4lQOUHxsQfYuVJvEMbgo,NAME_SEARCH,iugE", "https://www.linkedin.com/sales/people/ACwAAATQYhIBlpJcN4GsoTw8t4cpgQKN2yLhmds,NAME_SEARCH,a5Hw", "https://www.linkedin.com/sales/people/ACwAACPiaEkB-TUCCJIUoPPg9owHx3PhLTxefOI,NAME_SEARCH,vZ3P",
#                       "https://www.linkedin.com/sales/people/ACwAAAc1lKUBe7oG156PVWB5ylvSR_c2WwQ7Fh4,NAME_SEARCH,FyHc", "https://www.linkedin.com/sales/people/ACwAAAhRW9wBPF50cvPeoyYmTGfXzn1Lke8-0vQ,NAME_SEARCH,yZ-y", "https://www.linkedin.com/sales/people/ACwAAADVV9EBR5PVfUTywQglCsPeVPPxnFLfi7M,NAME_SEARCH,P1kc", "https://www.linkedin.com/sales/people/ACwAAAFwHqABLG10JhBYdvx96boalU6XpbUG4t8,NAME_SEARCH,RcSQ", "https://www.linkedin.com/sales/people/ACwAAAg1V9IBZqBP3HfoLts4U9RF5opU23aXAGQ,NAME_SEARCH,y8iQ", "https://www.linkedin.com/sales/people/ACwAAAH8-dUBfDUsbjg4eyqHewmy0K2M-P_3aPE,NAME_SEARCH,XrGG", "https://www.linkedin.com/sales/people/ACwAAAJuevAB2bgZEQOuRgNrOc4tr7Ngho3yvtY,NAME_SEARCH,c9t0", "https://www.linkedin.com/sales/people/ACwAABH2BZwB17bk2W-ORyg6zJ4cKtWKQyFepVQ,NAME_SEARCH,a7e7", "https://www.linkedin.com/sales/people/ACwAAAEXPPIBu2fdtJihH0sv1noirtM4vYwnV6Q,NAME_SEARCH,l9x3", "https://www.linkedin.com/sales/people/ACwAAAGG2mEB0APVB1oyyGMsPlfwHzGBaC2DjyE,NAME_SEARCH,xP1i", "https://www.linkedin.com/sales/people/ACwAAACd-l8BE40xls8Dhfh6WFv19Myv5MUnQxg,NAME_SEARCH,ygpK", "https://www.linkedin.com/sales/people/ACwAAAZLnuEBBmBNzBvd1xbtOkoFmcIQ9dqW1qs,NAME_SEARCH,FJOl", "https://www.linkedin.com/sales/people/ACwAAA6704IBVxkx78gTRU7vueZSe2a_rQeqv8c,NAME_SEARCH,bCSB", "https://www.linkedin.com/sales/people/ACwAAAdHeP0BuHP6kO4_DjY4LCt3HH8Knxm18K0,NAME_SEARCH,S3aU", "https://www.linkedin.com/sales/people/ACwAAAREvxkBA8y7NIdSPajpT_mwm5QlqYhpgl4,NAME_SEARCH,BTTS", "https://www.linkedin.com/sales/people/ACwAAAIwQxkBqhGnj33SJtnl8xIH6ut2b2BNIPQ,NAME_SEARCH,wQeg", "https://www.linkedin.com/sales/people/ACwAAAEtXC4BnQY5cxghoh0qB4xlN3COkyiKClA,NAME_SEARCH,bP7V", "https://www.linkedin.com/sales/people/ACwAAAmVUMIBKusqFB8Bhq2_Rp57T-e4GxcqDd0,NAME_SEARCH,CFU4", "https://www.linkedin.com/sales/people/ACwAAAC-D38BOVyDuocOSG2-gxjyUr2TIKiSZmk,NAME_SEARCH,2DjF", "https://www.linkedin.com/sales/people/ACwAAAhLB0UBruwSDiU-pIM5J3yKHqLdRLXVSyU,NAME_SEARCH,CQVz", "https://www.linkedin.com/sales/people/ACwAAAww78QBx9Jnxe1Bs_nIfjbD9uecgcMsxUk,NAME_SEARCH,6_qa", "https://www.linkedin.com/sales/people/ACwAAAWNfLYB7x-5JgVJ8RK4ImXF162KQdgDijg,NAME_SEARCH,qqpx", "https://www.linkedin.com/sales/people/ACwAAB-nIdQBh5lzrSSWiDZG8uqOyu-lA8m8Leo,NAME_SEARCH,w5o2", "https://www.linkedin.com/sales/people/ACwAAA6WUl0B-yh8hTM5ug4cI2MToxlHEDtPJtc,NAME_SEARCH,8wCs", "https://www.linkedin.com/sales/people/ACwAAAOjk2wBjykfmfUc0mOuBrVCZmfZeLUWr-I,NAME_SEARCH,zN0S", "https://www.linkedin.com/sales/people/ACwAABBxw28BvhXEKwChTG9DKVaIE_22Qg8f5fM,NAME_SEARCH,Mbs5", "https://www.linkedin.com/sales/people/ACwAAAHqY_YB-OX8YySEnghKLT0isaCwWXlb838,NAME_SEARCH,ViiI", "https://www.linkedin.com/sales/people/ACwAAAMLPMABlpz8Nuf91IeH7szYRfD2NZsYQYM,NAME_SEARCH,gi6_", "https://www.linkedin.com/sales/people/ACwAAAFxtv4B2YkOQo5QCVX7JN4bWvvbL08etBU,NAME_SEARCH,U7G4", "https://www.linkedin.com/sales/people/ACwAAA5nGcgB_FHdFIirbL4zJcPR9rlkqHt_4S0,NAME_SEARCH,eVwO", "https://www.linkedin.com/sales/people/ACwAAAnt1hQB8EHU7LmZ4ua-t5Ngv142NPSg-1o,NAME_SEARCH,N0bd", "https://www.linkedin.com/sales/people/ACwAAC-Fg3gBNraTcmj2r01Z1ti--yF6KNr0YGE,NAME_SEARCH,JXrA", "https://www.linkedin.com/sales/people/ACwAAAByDNQBiHHem3xYZo1nRSuwdKIpa0fwDMw,NAME_SEARCH,UFNt", "https://www.linkedin.com/sales/people/ACwAAAdzokkB59WA8d8QrNvSP6u8nHzYl5JZ1G8,NAME_SEARCH,a3Sz", "https://www.linkedin.com/sales/people/ACwAAAEbK1oBy_ByPOWCU3UeHBIsYAJFT4CF08I,NAME_SEARCH,RxPA", "https://www.linkedin.com/sales/people/ACwAAACpafsBAY8I7VZ1uen6sTrJhK8dnyZO2ic,NAME_SEARCH,guCL", "https://www.linkedin.com/sales/people/ACwAAANkpkIB7uejuUqEwP2CQ-wK4RncjIBUSJ8,NAME_SEARCH,tmXH", "https://www.linkedin.com/sales/people/ACwAAA1ApicBbHcRrtZFhl9Kx5zmOKogi9oQGjg,NAME_SEARCH,NsjR", "https://www.linkedin.com/sales/people/ACwAAAQ5rdgB0PzA-nTgj2IPsUnAF3jrPUmuAT8,NAME_SEARCH,NqVP", "https://www.linkedin.com/sales/people/ACwAAASzzTMBORIZM5ZAp7wAq3skkWkoLL5_iEM,NAME_SEARCH,-dsp", "https://www.linkedin.com/sales/people/ACwAAANIxxcB7exbXzQwGUgN7CEdqAJN_tEnBw8,NAME_SEARCH,J_GT", "https://www.linkedin.com/sales/people/ACwAAAQWo-0BR2S891BBXi1THWv0JySUpDtMWJg,NAME_SEARCH,WqEk", "https://www.linkedin.com/sales/people/ACwAAAPJG_4Bk73ijBfd4Q0ntPiePEJs594EjDU,NAME_SEARCH,hcg2", "https://www.linkedin.com/sales/people/ACwAAAUwsu4BxsnK6uVCSr0NJ_dBkwMFaH-76fc,NAME_SEARCH,jq1I", "https://www.linkedin.com/sales/people/ACwAAA3HFbABfbBB0LAUzw5grqga6kRvxRlnZmY,NAME_SEARCH,ASGF", "https://www.linkedin.com/sales/people/ACwAAAaT4xkB4n0-UzZ4UNYgIpeEa1cMcaw2BIE,NAME_SEARCH,tCdp", "https://www.linkedin.com/sales/people/ACwAAAZQ0c4BOKidOav2W9C2COlVSZj5dQJD4D4,NAME_SEARCH,tcNO", "https://www.linkedin.com/sales/people/ACwAAAQuxFYBbZ4ivTkf1U9xFTpIGEpVQuenaX4,NAME_SEARCH,oEcU", "https://www.linkedin.com/sales/people/ACwAAAFeLoMBANUt1az1aZi_-69wg0zbmpB9zas,NAME_SEARCH,hxwm", "https://www.linkedin.com/sales/people/ACwAAAFCyGABtwIFmNjW69mNgDMqN4dOla6qFDw,NAME_SEARCH,v6-w", "https://www.linkedin.com/sales/people/ACwAAAIPwCABcc2RZJEXNoZGOlcRD4T0YLGig7I,NAME_SEARCH,8FUz", "https://www.linkedin.com/sales/people/ACwAAA46I5EBjxh9nuAjBUhCbG8BHDLewRNOtx8,NAME_SEARCH,SfMp", "https://www.linkedin.com/sales/people/ACwAAA_drXYBFMzf8M8MVEIkvsCrupxdxzgtMAM,NAME_SEARCH,9M2Z", "https://www.linkedin.com/sales/people/ACwAAArssMcBpSooQhh8gATWdnbosLtyxHQk_o0,NAME_SEARCH,s7pY", "https://www.linkedin.com/sales/people/ACwAABARv4YBGpdwNZqlNDs42bxW4ygVi42lXFA,NAME_SEARCH,76d6", "https://www.linkedin.com/sales/people/ACwAAAIciAkBPes6WrlZradz4vnEARxQOhVoSg8,NAME_SEARCH,kU27", "https://www.linkedin.com/sales/people/ACwAAAEBvw0BGXD-u5SzG7abWZaLK0clGgxgnZ4,NAME_SEARCH,gS2X", "https://www.linkedin.com/sales/people/ACwAAAyZk_cBF3Xd50SboStaOk3nDNUEP2ZP_Ds,NAME_SEARCH,9aPk", "https://www.linkedin.com/sales/people/ACwAAAP1yYwBTNRCh0lrvaiEThqiG0AcLx7P_-w,NAME_SEARCH,sEYa", "https://www.linkedin.com/sales/people/ACwAAABaGoIBri4ZJIZi_SAbysNzI5ang1TMHxY,NAME_SEARCH,W0Al", "https://www.linkedin.com/sales/people/ACwAAAI7CcsBSZUYHSYDfEhiE87ZCXEO9OxRkBQ,NAME_SEARCH,a9N7", "https://www.linkedin.com/sales/people/ACwAAAXNcioB5UpMofQ4lQOUHxsQfYuVJvEMbgo,NAME_SEARCH,iugE", "https://www.linkedin.com/sales/people/ACwAAATQYhIBlpJcN4GsoTw8t4cpgQKN2yLhmds,NAME_SEARCH,a5Hw", "https://www.linkedin.com/sales/people/ACwAACPiaEkB-TUCCJIUoPPg9owHx3PhLTxefOI,NAME_SEARCH,vZ3P"]

# driver.get(navigator_profiles[0])


# If using normal linkedIn profile links, there is no need for three_dots and view_on_linkedIn to be clicked
    # get the 3 dot menu
# three_dots = driver.find_element_by_xpath(
#     "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div[3]/button")
# three_dots.click()

# sleep()

# # click the view on linkedIn button
# view_on_linkedIn = driver.find_element_by_xpath(
#     "/html/body/main/div[1]/div[2]/div/div[2]/div[1]/div[3]/div/div/div/div/div[1]/div/ul/li[3]/div")
# view_on_linkedIn.click()
# sleep(4)
# # ------------ We are now on a public linkedIn Profile -------------
# # follower count in only displayed on the linkedIn public profile.

# # switch Selenium focus to new tab
# driver.switch_to.window(driver.window_handles[1])
# sleep(0.5)

# # scroll down so dynamic elements load
# driver.execute_script("window.scrollTo(0, 1000)")
# sleep(2)

# try:
#     followers = driver.find_element_by_xpath(
#         "/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[2]/div[4]/div/section/h3/span").text
# except:
#     followers = "could not find followers"

# name = ""
# # find name
# try:
#     name = driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/div/div/div/div[2]/main/div[1]/section/div[2]/div[2]/div[1]/ul[1]/li[1]").text
# except:
#     name = "could not find name on linkedIn Profile"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from parsel import Selector
import random
import math
import creds

# specifies the path to the chromedriver.exe make sure this points to the web driver. add webdriverpat to $path.
driver = webdriver.Chrome(ChromeDriverManager().install())

# Takes an  object `account` whoch has `password` and `username` keys


def login(account):

    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.instagram.com')
    wait(7)

    # pass the "accept cookies?" dialogue
    try:
        accept_cookies_button = driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div[2]/button[1]")
        wait(3)
    except:
        print("Could not find accept_cookies_button")

    click(accept_cookies_button, "accept_cookies_button")

    # identify the username field and send the username
    try:
        usernameElement = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        wait(0.4)
    except:
        print("Could not find usernameElement")

    try:
        usernameElement.send_keys(account["username"])
        wait(0.4)
    except:
        print("Could not send to usernameElement")

    # identify the password field in browser and send
    try:
        passwordElement = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        wait(0.2)
    except:
        print("Could not find passwordElement")

    try:
        passwordElement.send_keys(account["password"])
        wait(0.2)
    except:
        print("Could not find passwordElement")

    # identify the log in button in browser and click it
    try:
        log_in_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        wait(5)
    except:
        print("Could not find log_in_button")

    click(log_in_button, "log_in_button")

    # pass the "remember this computer?" dialogue
    try:
        dont_remember_me_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div/div/div/button")
        wait(3)
    except:
        print("Could not find dont_remember_me_button")

    click(dont_remember_me_button, "dont_remember_me_button")

    # click not now to get around the notificaitons dialogue
    try:
        no_notifications_button = driver.find_element_by_xpath(
            "/html/body/div[4]/div/div/div/div[3]/button[2]")
        wait(3)
    except:
        print("Could not find no_notifications_button")

    click(no_notifications_button, "no_notifications_button")


def search_account(account):

    # identify the search field and enter some string
    try:
        searchElement = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        wait(3)
    except:
        print("Could not find searchElement")

    try:
        searchElement.send_keys(account["username"])
        wait(3)
    except:
        print("Could not find searchElement")

    # click on the first result that is presented
    try:
        first_result_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
        wait(5)
    except:
        print("Could not find first_result_button")

    click(first_result_button, "the" + account["username"])


def get_element_from_xpaths(xpaths):
    #  cycle through possible xpaths until a valid element is found on page.
    for xpath in xpaths:
        try:
            element = driver.find_element_by_xpath(xpath)
            print("found a valid comment element xpath")
            return(element)
        except:
            continue

    print("Did not find a valid xpath on this page")
    return("Did not find a valid xpath on this page")


def get_element_by_xpath(xpath, element_name):
    #  get the element, given it's expath
    try:
        element = driver.find_element_by_xpath(xpath)
        print("found a valid element for" + element_name)
        return(element)
    except:
        print("Did not find a valid xpath on this page for " + element_name)

    return("Did not find a valid xpath on this page")


def click(element, element_name):
    # tries to click on an element
    # must take a web element as constructed by get_element_from_xpaths
    # chrome drive must be running

    wait(random.randrange(1, 2))
    try:
        element.click()
        wait(random.randrange(1, 3))
    except:
        print("Could not click on " + element_name)
    wait(random.randrange(1, 3))


def log_out():
    # must be done when the menu button is visible

   # click the menu button
    try:
        profile_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span")
        wait(2)
    except:
        print("Could not find profile_button")

    click(profile_button, "Could not send to profile_button")

    # click the logout button
    try:
        log_out_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div")
        wait(2)
    except:
        print("Could not find log_out_button")

    click(log_out_button, "Could not send to close_post_button")

    wait(5)


def explore():

    # close anthing going on. Go to the explore screen
    close_post()

    # find explore button
    try:
        explore_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/a")
        wait(1)
    except:
        print("Sucessfully click the explore button")

    # click explore button
    click(explore_button, "Could not click the explore button")

# def get_first_explore_post():
#     # opens the first post on the explore page
#     /html/body/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div[1]/div[2]
#     /html/body/div[1]/section/main/div/div[1]/div/div[1]/div[1]/div/a/div[1]/div[2]
#     /html/body/div[1]/section/main/div/div[1]/div/div[1]/div[3]/div/a/div/div[2]


def search(search_term):
    # takes a string, which is the search_term. It navigates to the first search term.

    # identify the search field and enter some string
    try:
        searchElement = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
        wait(3)
    except:
        print("Could not find searchElement")

    try:
        searchElement.send_keys(search_term)
        wait(3)
    except:
        print("Could not find searchElement")

    get_post_on_hashtag_page()

    # click on the first result that is presented
    try:
        first_result_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]")
        wait(5)
    except:
        print("Could not find first_result_button")

    click(first_result_button, "first_result_button")


def wait(time):
    # sleep for a random time period, clos enough to the
    total_time = random.randrange(time, time + 1)
    sleep(total_time)


def scroll(pixels):
    # scolls down an amount of pixels
    scroll_command = 'window.scrollTo(0,{})'
    script = scroll_command.format(pixels)
    driver.execute_script(script)
    wait(random.randrange(4, 5))


engage_from_all_accounts(creds)


# def follow_people/

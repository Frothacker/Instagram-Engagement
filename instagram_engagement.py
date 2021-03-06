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


def get_latest_post():
    # only works when an account page is open

    # click on the first result that is presented
    try:
        latest_post_button = driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[2]")
        wait(5)
    except:
        print("Could not find latest_post_button")

    click(latest_post_button, "latest_post_button")


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


def like():
    # only works if the post is open

    wait(random.randrange(1, 2))
    like_button_xpaths = ["/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button",
                          "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button",
                          '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button']

    # click the like button to like the post
    like_button = get_element_from_xpaths(like_button_xpaths)
    wait(random.randrange(2, 3))

    click(like_button, "like_button")


def comment():  # TODO add try excepts.

    general_comments = ["Love this", "🤍", "🤍", "💛", "💛", "💛", "💛💛", "🤍🤍", "🤍💛", "🤍💛", "🥰", "🥰",  "🌻", "🌻", "This is calming", "Beautiful"
                        "😍", "😍", "👏🏼", "This makes me feel calm", "I love this", "🌊", "Oh I love it", "This is so nice", "So nice", "pretty", "nice", "This is beautiful", "This makes me happy 🥰🥰", "beautiful", "happy"]

    comment = random.choice(general_comments)
    print(comment)
    wait(1)

    # cycle through possible xpaths for teh commment button
    comment_button_xpaths = ["/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button"
                             "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button",
                             "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button",
                             '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button',
                             "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[2]/button"]

    comment_button = get_element_from_xpaths(comment_button_xpaths)

    # makes the text area element visible
    click(comment_button, "comment_button")
    wait(random.randrange(1, 2))

    # find the active comment input field
    comment_field_xpaths = ["/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/textarea",
                            "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div[1]/form/textarea",
                            "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea",
                            "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form",
                            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea",
                            "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/textarea"]


    active_comment_field = get_element_from_xpaths(comment_field_xpaths)
    wait(random.randrange(1, 2))

    # try to find the active element by class name
    if active_comment_field == "Did not find a valid xpath on this page":
        try:
            active_comment_field = driver.get_element_by_class_name(
                "Ypffh focus-visible")
            print("Found active comment element by classname")
        except:
            print("could not find active comment element by classname")

    wait(random.randrange(1, 2))

    # send it the comment, which makes the post button visible
    try:
        active_comment_field.send_keys(comment)
    except:
        print("Could not send keys to comment field")
    wait(random.randrange(1, 2))

    post_comment_button_xpaths = ["/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button",
                                  "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div[1]/form/button"]
    post_comment_button = get_element_from_xpaths(post_comment_button_xpaths)

    click(post_comment_button, "post_comment_button")
    wait(random.randrange(1, 2))


# def comment():
#     # only works if the post is open

#     # define a bank of comments to cycle through
#     general_comments = ["Love this", "🤍","🤍", "💛","💛","💛", "💛💛", "🤍🤍", "🤍💛","🤍💛", "🥰","🥰",  "🌻","🌻", "This is calming", "Beautiful"
#                         "😍","😍", "👏🏼", "This makes me feel calm", "I love this", "🌊", "Oh I love it", "This is so nice", "So nice", "pretty", "nice", "This is beautiful", "This makes me happy 🥰🥰", "beautiful", "happy"]

#     # embroidery_comments = ["🧵", "🧶",  "🌼",  "🌻",
#     #                        "Love the stitching 🤍", "I love 🤍 the design on this one ", "This is beautiful", "This makes me happy 🥰🥰"]
#     # landscape_comments = ["⛰", "🌻", "This is calming"]

#     # special_comments = {"frog": "🐸", "jeans": "👖", "shirt": "👕", "shoes": "🩰"}


def close_post():
    # only works if the post is open

    # close the post
    try:
        close_post_button = driver.find_element_by_xpath(
            "/html/body/div[4]/div[3]/button")
        wait(2)
    except:
        print("Could not find close_post_button - a post may not be open")

    click(close_post_button,
          "close_post_button - a post may not be open")

    wait(2)


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


def get_post_on_hashtag_page():
    # takes a post number and navigates to that post.
    # only works when an account page is open

    # find name
    post_element_paths = ["/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[1]/a/div/div[2]",
                          "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]"]

    #  loop through the different possible x-paths to the account
    for xpath in post_element_paths:
        try:
            name = driver.find_element_by_xpath(xpath).text
        except:
            name = "Could not find latest_post_button"
        if name != "Could not find latest_post_button":
            break
    print(name)

    # # scroll down so dynamic elements load
    # driver.execute_script("window.scrollTo(0, 1000)")
    # wait(3)

    # # click on one of the result
    # try:
    #     latest_post_button = driver.find_element_by_xpath()
    #     wait(5)
    # except:
    #     print("Could not find latest_post_button")

    # click(latest_post_button, "latest_post_button")


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


def natural_engagement():

    hashtags = ["#freeyourself", "#loveyourself",
                "#breatheinandout", "#embroideryjeans"]

    search(random.choices(hashtags))
    # we will land on the hashtag page

    # scroll down
    driver.execute_script("window.scrollTo(0, 400)")
    wait(3)

    # scroll through the feed and click on things, like things, wait.
    # random intervals between people
    # find a person (within a certain hashtag), click on their profile, Scroll through their posts and give some random ones a like.
    # go back
    # randomnly choose if they want to do it again
    # place random public comments on things
    # go back and forwards agiain.
    # every sub process should be ale to

    # must signout befor you can sign in again


def like_and_comment(account):
    # must be used after logging
    search_account(account)
    get_latest_post()
    like()
    comment()
    close_post()


def engage_from_all_accounts(target_account):
    for account in creds.accounts:
        # don't like and comment on yout own account
        if account["username"] == target_account["username"]:
            print("skipping " + account["username"])

            continue
        print("engaging " + account["username"])
        login(account)
        like_and_comment(target_account)
        log_out()
    # TODO login as the new account and like and reply to all the comments


# engage_from_all_accounts(creds)



# def follow_people/

from pageobjects.home_page import HomePage
from pageobjects.polls_page import PollsPage


# Print how many articles (highlighted in green) are on the page
def test_article_number_on_page():
    # define a HomePage instance
    home_page = HomePage()

    # access the home page of Slashdot website
    home_page.visit_home()

    # test how many articles showed on the page
    home_page.calculate_article()


# Print a list of unique icons (highlighted in red) used on article titles and how many times was it used
def test_icons_used_status():
    # define a HomePage instance
    home_page = HomePage()

    # access the home page of Slashdot website
    home_page.visit_home()

    # test how many icons showed on the document
    home_page.calculate_icon()


# Vote for some random option on the daily poll and return the number of people that have voted for that same option
def test_vote_option():
    # define a HomePage instance
    home_page = HomePage()

    # access the home page of Slashdot website
    home_page.visit_home()

    # enter Polls page
    home_page.click_polls()

    # define a PollPage instance
    polls_page = PollsPage(driver=home_page.driver)

    # select a random option
    polls_page.select_random_option_to_vote()

    # click the random option
    polls_page.click_vote_button()

    # test how many people voted the random option
    polls_page.get_random_option_voted_times()


# Print out the number of Most Discussed
def test_discussed_num():
    # define a HomePage instance
    home_page = HomePage()

    # access the home page of Slashdot website
    home_page.visit_home()

    # test the number of Most Discussed
    home_page.show_number_most_discussed()

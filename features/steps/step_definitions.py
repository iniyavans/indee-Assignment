from selenium.common import TimeoutException
from pages.login_page import LoginPage
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.video_page import VideoPage

driver = webdriver.Chrome()
driver.maximize_window()

@given("I open the login page")
def open_login_page(context):
    """Open the login page of the application.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Given I open the login page
    """
    context.login_page = LoginPage(driver)
    context.login_page.open()

@when('I enter the PIN "{pin}"')
def enter_pin(context, pin):
    """Enter the provided PIN to log in.

    Args:
        context: The context object containing the state of the test.
        pin (str): The PIN to enter for login.
    
    Example:
        When I enter the PIN "1234"
    """
    context.login_page.login(pin)

@given("I am logged into the platform")
def open_login_page(context):
    """Verify that the user is logged into the platform by checking for a specific element.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Given I am logged into the platform
    """
    home_page = (
        By.XPATH,
        "//p[text()=' All Titles ']",
    )
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(home_page)
        )
        print("Successfully Login to the Indee.")
    except TimeoutException:
        raise AssertionError("Failed to Login to the Indee.")

@when('I navigate to the "Test Automation Project"')
def navigate_to_project(context):
    """Navigate to the specified project page.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        When I navigate to the "Test Automation Project"
    """
    context.video_page = VideoPage(driver)
    context.video_page.navigate_to_project()

@then("I should be on the project page")
def verify_project_page(context):
    """Verify that the user is on the project page by checking for a specific title.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then I should be on the project page
    """
    project_title_locator = (
        By.XPATH,
        "//p[text()='Test automation project']",
    )  
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(project_title_locator)
        )
        print("Successfully navigated to the Test Automation Project page.")
    except TimeoutException:
        raise AssertionError("Failed to navigate to the Test Automation Project page.")

@given('I am moved to the projects page')
def logged_into_platform(context):
    """Placeholder step for moving to the projects page.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Given I am moved to the projects page
    """
    context.video_page = VideoPage(driver)
    pass

@when('I switch to the "Details" tab')
def switch_to_details_tab(context):
    """Switch to the 'Details' tab of the project.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        When I switch to the "Details" tab
    """
    context.video_page.switch_to_details_tab()

@when("I wait for {seconds} seconds")
def wait_for_seconds(context, seconds):
    """Wait for a specified number of seconds.

    Args:
        context: The context object containing the state of the test.
        seconds (int): The number of seconds to wait.
    
    Example:
        When I wait for 5 seconds
    """
    time.sleep(int(seconds))

@then('I switch back to the "Videos" tab')
def switch_to_videos_tab(context):
    """Switch back to the 'Videos' tab of the project.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then I switch back to the "Videos" tab
    """
    context.video_page.switch_to_videos_tab()

@then("I play the video")
def play_video(context):
    """Play the video on the project page.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then I play the video
    """
    context.video_page.play_video()

@then("I wait for 10 seconds")
def wait_10_seconds(context):
    """Wait for 10 seconds after ensuring the video is playing.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then I wait for 10 seconds
    """
    project_title_locator = (
        By.XPATH,
        "//iframe[@id = 'video_player']",
    ) 
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(project_title_locator)
        )
        print("Video is playing, and waiting for 10 secs")
    except TimeoutException:
        raise AssertionError("Video is not playing.")

    time.sleep(10)

@then("I pause the video")
def pause_video(context):
    """Pause the currently playing video.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then I pause the video
    """
    actions = ActionChains(driver)
    actions.send_keys(Keys.SPACE).perform()

@given('I moved to the "Continue Watching" Page')
def continue_watching(context):
    """Navigate to the 'Continue Watching' page.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Given I moved to the "Continue Watching" Page
    """
    context.video_page = VideoPage(driver)
    continue_watching_element = (
        By.XPATH,
        "//button[@aria-label='Continue Watching']",
    )
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(continue_watching_element)
        )
        print("Successfully navigated to the continue watching page.")
    except TimeoutException:
        raise AssertionError("Failed to navigated to the continue watching page.")

@when('I click the "Continue Watching" button')
def click_continue_watching(context):
    """Click the 'Continue Watching' button to resume the video.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        When I click the "Continue Watching" button
    """
    context.video_page.click_element(context.video_page.CONTINUE_WATCHING_BUTTON)

@then("the video should resume playing")
def verify_video_resumes(context):
    """Verify that the video resumes playing after clicking the button.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then the video should resume playing
    """
    video_player = (
        By.XPATH,
        "//iframe[@id = 'video_player']",
    )
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(video_player)
        )
        print("Video is playing.")
    except TimeoutException:
        raise AssertionError("Video is not playing.")

@given("Verify the video is playing")
def verify_video_resumes(context):
    """Check if the video is currently playing.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Given Verify the video is playing
    """
    video_player = (
        By.XPATH,
        "//iframe[@id = 'video_player']",
    ) 
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(video_player)
        )
        print("Video is playing.")
    except TimeoutException:
        raise AssertionError("Video is not playing.")

@when("I set the volume to 50%")
def adjust_volume(context):
    """Set the video volume to 50%.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        When I set the volume to 50%
    """
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "//iframe[@id = 'video_player']"))
        )

        driver.switch_to.frame(iframe)

        volume_slider = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@aria-label='Volume'])[1]"))
        )

        driver.execute_script(
            "arguments[0].setAttribute('aria-valuenow', '50');", volume_slider
        )

        driver.execute_script(
            "arguments[0].setAttribute('aria-valuetext', 'Volume 50%');", volume_slider
        )

        print("Successfully updated 'aria-valuenow' to 50.")

        updated_value = volume_slider.get_attribute("aria-valuenow")

        assert updated_value == '50', f"Assertion failed: Expected '50', but got '{updated_value}'"

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        driver.switch_to.default_content()

@when('I change the resolution to "{resolution}"')
def change_resolution(context, resolution):
    """Change the video resolution to the specified value.

    Args:
        context: The context object containing the state of the test.
        resolution (str): The resolution to set (e.g., "720p", "1080p").
    
    Example:
        When I change the resolution to "1080p"
    """
    try:
        iframe = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "//iframe[@id = 'video_player']"))
        )

        driver.switch_to.frame(iframe)
        context.video_page.change_resolution(resolution)

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        driver.switch_to.default_content()

@given("I logout the Indee")
def verify_video_resumes(context):
    """Logout from the application.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Given I logout the Indee
    """
    context.video_page = VideoPage(driver)
    pass

@when("I pause the videos")
def pause_video(context):
    """Pause the currently playing videos.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        When I pause the videos
    """
    actions = ActionChains(driver)
    actions.send_keys(Keys.SPACE).perform()

@when('I click the "Back" button')
def click_back_button(context):
    """Click the 'Back' button to return to the previous page.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        When I click the "Back" button
    """
    context.video_page.click_element(context.video_page.BACK_BUTTON)

@then("I log out of the platform")
def log_out(context):
    """Log out of the platform by clicking the logout button.

    Args:
        context: The context object containing the state of the test.
    
    Example:
        Then I log out of the platform
    """
    context.video_page.click_element(context.video_page.LOGOUT_BUTTON)
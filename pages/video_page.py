from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class VideoPage(BasePage):
    """
    VideoPage class represents the video page of the application. It provides methods to interact with various elements on the page,
    such as navigating to a project, switching tabs, playing videos, and changing video resolution.

    Attributes:
        TEST_AUTOMATION_PROJECT (tuple): Locator for the test automation project element.
        DETAILS_TAB (tuple): Locator for the details tab.
        VIDEOS_TAB (tuple): Locator for the videos tab.
        PLAY_BUTTON (tuple): Locator for the play video button.
        CONTINUE_WATCHING_BUTTON (tuple): Locator for the continue watching button.
        SETTINGS_BUTTON (tuple): Locator for the settings button.
        RES_480P (tuple): Locator for the 480p resolution button.
        RES_720P (tuple): Locator for the 720p resolution button.
        BACK_BUTTON (tuple): Locator for the back button.
        LOGOUT_BUTTON (tuple): Locator for the logout button.
    """

    TEST_AUTOMATION_PROJECT = (By.XPATH, "//h5[text()='Test automation project']")
    DETAILS_TAB = (By.ID, "detailsSection")
    VIDEOS_TAB = (By.ID, "videosSection")
    PLAY_BUTTON = (By.XPATH, "//button[@aria-label='Play Video']")
    CONTINUE_WATCHING_BUTTON = (By.XPATH, '//button[@aria-label="Continue Watching"]')
    SETTINGS_BUTTON = (By.XPATH, '(//div[@aria-label="Settings"])[1]')
    RES_480P = (By.XPATH, "//button[@aria-label='480p']")
    RES_720P = (By.XPATH, "//button[@aria-label='720p']")
    BACK_BUTTON = (By.XPATH, '//button[@aria-label="Go Back and continue playing video"]')
    LOGOUT_BUTTON = (By.ID, "signOutSideBar")

    def navigate_to_project(self):
        """ Navigate to the test automation project by clicking on the project element. """

        self.wait_for_element(self.TEST_AUTOMATION_PROJECT)
        self.click_element(self.TEST_AUTOMATION_PROJECT)

    def switch_to_details_tab(self):
        """ Switch to the details tab by clicking on the details tab element. """

        self.click_element(self.DETAILS_TAB)

    def switch_to_videos_tab(self):
        """ Switch to the videos tab by clicking on the videos tab element. """

        self.click_element(self.VIDEOS_TAB)

    def play_video(self):
        """ Play the video by clicking on the play button. """
        
        self.click_element(self.PLAY_BUTTON)

    def change_resolution(self, resolution):
        """
        Change the video resolution to the specified value.

        Args:
            resolution (str): The desired resolution, either "480p" or "720p".

        """
        self.click_element(self.SETTINGS_BUTTON)
        if resolution == "480p":
            self.click_element(self.RES_480P)
        elif resolution == "720p":
            self.click_element(self.RES_720P)
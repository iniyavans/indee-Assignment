Feature: Sign to the platform
  Scenario: User logs into the platform
    Given I open the login page
    When I enter the PIN "WVMVHWBS"

  Scenario: Navigate to the 'Test Automation Project'
    Given I am logged into the platform
    When I navigate to the "Test Automation Project"
    Then I should be on the project page

  Scenario: Switch to the 'Details' Tab and Return to the 'Videos' Tab and Play the Video
    Given I am moved to the projects page
    When I switch to the "Details" tab
    And I wait for 5 seconds
    Then I switch back to the "Videos" tab
    And I play the video
    Then I wait for 10 seconds
    And I pause the video

  Scenario: Replay video using the "Continue Watching" button
    Given I moved to the "Continue Watching" Page
    When I click the "Continue Watching" button
    Then the video should resume playing

  Scenario: Adjust Volume and Change Video Resolution
    Given Verify the video is playing
    When I set the volume to 50%
    And I change the resolution to "480p"
    And I change the resolution to "720p"

  Scenario: Pause, Exit and Logout:
    Given I logout the Indee
    When I pause the videos
    And I click the "Back" button
    Then I log out of the platform
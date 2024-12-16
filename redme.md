# Indee Automation Assignment: Video Playback and Control Using Selenium Python

## Project Overview

This project automates the testing of a web-based video platform using Python and Selenium with a Behavior-Driven Development (BDD) framework. The goal is to verify key functionalities such as video playback control, volume adjustment, resolution changes, and user logout through automation. The task demonstrates proficiency in automation testing and adherence to best practices using Selenium WebDriver.

## Objective

Automate the following tasks on the Indee Video Platform:

1. Sign in to the platform.
2. Navigate to a specific video project.

3. Test video playback and controls.

4. Adjust video settings (volume and resolution).

5. Logout functionality.

## Features

1. Login Automation: Automates the sign-in process using provided credentials.

2. Navigation: Handles navigation between tabs and screens.

3. Video Playback Controls: Automates play, pause, and resume functionalities.

4. Volume Adjustment: Dynamically sets video volume to 50%.

5. Resolution Change: Switches between 480p and 720p resolutions.

6. Logout: Automates the logout sequence from the platform.

7. Error Handling: Implements robust error handling for seamless execution.

8. Dynamic Waits: Uses WebDriverWait for efficient and dynamic synchronization.

## Prerequisites
### Tools and Libraries:
1. Python 3.8+

2. Selenium 4.0+

3. BDD Framework

4. BrowserDriver (e.g., ChromeDriver or GeckoDriver)

### Installation:
1. Clone this repository.

```bash
git clone <repository-url>
```
2. Install the required Python libraries:

```bash
pip install -r requirements.txt
```
3. Ensure the appropriate WebDriver is available in your system path.

## Usage
### Running the Automation Script:
1. Navigate to the project directory.
2. Execute the test scenarios:
```bash
 behave features/
```
### Demo Video:
A demo video showcasing the script in action is included in the submission files.

## File Structure

```bash
Indee-Automation-Assignment/
|-- features/
|   |-- steps/
|   |   |-- step_definitions.py  # Step implementations.
|   |-- login.feature            # BDD feature file.
|-- pages/
|   |-- base_page.py             # Base page.
|   |-- login_page.py            # Login page.
|   |-- video_page.py            # Video page.
|-- requirements.txt             # Python dependencies.
|-- README.md                    # Project documentation.
```

## Evaluation Criteria
1. Functionality: Accuracy of automation for each task.
2. Code Quality: Clean, modular, and well-commented scripts.
3. Dynamic Waits: Use of WebDriverWait over static delays.
4. Page Object Model (Optional): Incorporation of POM design pattern for scalability.
5. Demo Video: Validation of task execution.

## Deliverables
1. Python script automating the tasks.
2. Demo video file showing the automation in action.

## Author
Iniyavan Murugesan

SDET
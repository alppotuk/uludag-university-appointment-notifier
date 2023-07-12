# Health Appointment Booking Script

This script notifies you when new health appointments are released at Uludağ Üniversitesi. It utilizes a Telegram bot and Selenium with Geckodriver for automated monitoring.

## Prerequisites

Before running the script, ensure that you have:

- Python 3.x and necessary libraries installed
- **Compatible version of Geckodriver** installed for your Firefox browser (this gave my headaches)
- A Telegram bot token and chat id (on Telegram using BotFather)

## Installation and Configuration

1. Clone the repository on your local machine.
2. Open the config.py file and replace the placeholder values with your own:

```
BOT_TOKEN = '<YOUR_BOT_TOKEN>'
CHAT_ID = '<YOUR_CHAT_ID>'
```

- To get the BOT_TOKEN and the CHAT_ID, you need to create a bot on Telegram using the BotFather and interact with your newly created bot. You may find more information on that in the internet.

3. Open the main.py file and locate the anchor_1 variable. Modify its value to specify the health branch for which you want to book an appointment. To determine the appropriate value for anchor_1, you can use the inspect tool on the web page and identify the corresponding element or attribute.

4. Once you are on the desired health branch page, determine the number of times you need to click the 'next week' button to navigate to the desired appointment date. This value may vary depending on when you use the script and the specific health branch. Adjust the value for loop in the code accordingly.

5. Optionally, you can configure the frequency of the script's checking behavior by adjusting the value in the time.sleep(<sleep_time>) function.

## Usage

1. Run the script:

```
python3 main.py
```

2. The script will launch a browser and repedately monitor the Uludağ University website for new appointments in your desired branch. When new appointments become available, it will notify you via your Telegram bot. So sit back, relax, and enjoy a sip of your coffee while the script does the work for you. Get well soon :)

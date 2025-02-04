from dotenv import load_dotenv
import os
from slack_client import SClient
import pprint

def lambda_handler(event=None, context=None):
  load_dotenv(verbose=True)

  slack_token = os.getenv("SLACK_API_BOT_TOKEN")
  slack_channel = os.getenv("SLACK_CHANNEL")
  chat_text = os.getenv("CHAT_TEXT")

  sClient = SClient(slack_token, slack_channel)

  # today = sClient.today().strftime('%d')
  today = '31' # for test
  check_day = sClient.get_last_weekday()

  if today == check_day:
    sClient.post_message(chat_text)
  else:
    pprint.pprint(f'unmatch {today}')

if __name__ == "__main__":
  lambda_handler()

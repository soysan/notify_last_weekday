from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from datetime import datetime, timedelta, timezone
import jpholiday
from typing import Union

class SClient:
  def __init__(self, token, channel):
    self.client = WebClient(token=token)
    self.channel = channel

  def post_message(self, text) -> Union[dict, None]:
    """
    Post a message to Slack

    Parameters
    ----------
    text : str
      The message to post
    """

    # Convert \\n to newline for lambda_handler()
    replaced_text = text.replace('\\n', '\n')

    try:
      response = self.client.chat_postMessage(
        channel=self.channel,
        text=replaced_text,
        mrkdwn=True,
        link_names=True,
      )

      return response
    except SlackApiError as e:
      print(f"Error posting message: {e.response['error']}")
      return None

  def get_last_weekday(self) -> str:
    """
    Get the last weekday of the month

    Returns
    -------
    day : str
      The last weekday of the month, e.g., '31'
    """

    today = self.today()

    next_month = today.replace(day=28) + timedelta(days=4)
    last_day = next_month - timedelta(days=next_month.day)

    while last_day.weekday() >= 5 or jpholiday.is_holiday(last_day):
      last_day -= timedelta(days=1)

    day = last_day.strftime('%d')

    return day

  def today(self) -> datetime:
    """
    Get today's date and time in JST

    Returns
    -------
    today : datetime
      Today's date and time
    """
    JST = timezone(timedelta(hours=+9))
    today = datetime.now(JST)
    return today

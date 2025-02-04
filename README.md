# Notification Slack bot for the last weekday of the month

This will post a preferable message on Slack from an AWS Lambda function.
EventBridge will trigger the target days on the last weekdays of every month.

The cron schedule would be set like `cron(0 6 26-31 * ? *)`.

## Usage

Create a virtual environment

```python
python -m venv venv
```

Install dependencies

```bash
source venv/bin/activate
pip install -r requirements.txt
```

Create a zip file for deploying

```bash
bash ./make_zip.sh 
```

Deploying on Lambda function

## Set environment variables in .env or Lambda config
- SLACK_API_BOT_TOKEN=`set Slack bot token`
- SLACK_CHANNEL=`set Slack channel ID`
- CHAT_TEXT=`any string you want to post`

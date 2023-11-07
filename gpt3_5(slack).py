import os
import openai
import argparse
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# slack 에서는 메세지를 받아 이를 ChatGPT에게 넘겨주고 alert_msg는 gpt의 결과를 출력시켜주는 채널


class OpenAIGpt:
    def run(self, msg):
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{msg}.",
            temperature=0.3,
            max_tokens=512,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=None
        )

        return response.choices[0].text.strip()


load_dotenv()

client = WebClient(token="xoxb-3862308310704-5203421001315-sd6VOQFLzKobKTA6ApdxI8pW")
channel_id = 'D055WHRV6G5'

try:
    result = client.conversations_history(channel=channel_id)

    conversation_history = result["messages"]
    openai_gpt = OpenAIGpt()
    ans = openai_gpt.run(conversation_history[0]['text'])
    print("conversation_history[0]['text'] : ", conversation_history[0]['text'])
    print(ans)
    client.chat_postMessage(channel='#ChatGPTBot', text=f"{ans}")
except SlackApiError as e:
    print("Error creating conversation: {}".format(e))

import os
import openai
import argparse
from dotenv import load_dotenv


class OpenAIGpt:
    def __init__(self):
        load_dotenv()

    def run(self, args):
        question = input("Question! : ")
        openai.api_key = "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"
        response = openai.Completion.create(
          model="ft:davinci-002:somma::8I9Ns6jk",
          # model="<Write your fine-tuning model>",             # 사용할 "fine-tuning model" 작성.
          prompt=f"{question}",
          temperature=args.temperature,
          max_tokens=100,
          top_p=1,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          stop=["\n"]
          # stop=None
        )
        # print(response)
        print(response.choices[0].text.strip())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # python gpt3.py --temperature 0.3
    parser.add_argument('--temperature', default=0.3)

    args = parser.parse_args()
    openai_gpt = OpenAIGpt()
    openai_gpt.run(args)

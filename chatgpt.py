import os
import openai
import argparse
from dotenv import load_dotenv


class OpenAIGpt:
    def __init__(self):
        load_dotenv()

    def run(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        text = "Hello. Nice to meet you :)"             # 여기에 질문할 text 입력
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                # {"role": "system", "content": "You are a helpful assistant that translates English to Korean."},
                {"role": "system", "content": "You are a helpful assistant"},
                # {"role": "user", "content": f'Translate the following English text to Korean: "{text}"'}
                {"role": "user", "content": f'Explain with meaning and Translate for Korean: "{text}"'}
            ]
        )

        print(completion)
        print(completion['choices'][0]['message']['content'])

# 각 메세지는 'role' 과 'content' 속성 으로 이루어짐.
# assistant = ChatGPT 가 역할을 맡음. /  user = 사용자 를 나타냄.


if __name__ == '__main__':
    openai_gpt = OpenAIGpt()
    openai_gpt.run()

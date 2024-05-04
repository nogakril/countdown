import json
from typing import Union

from openai import OpenAI, Stream
from openai.types.chat import ChatCompletion, ChatCompletionChunk

OPENAI_API_KEY = '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'


class OpenAIManager:
    def __init__(self, api_key=OPENAI_API_KEY):
        self.api_key = api_key
        self.client = OpenAI(api_key=self.api_key)
        self.headers = {
            "Authorization": f'Bearer {self.api_key}',
        }

    def generate_completion_request(self, question) -> [str, bool]:
        message = (f"First, Let's say I have a question: {question}? "
                   f"Answer which time frame makes the most sense: years/months/days/hours/seconds?"
                   f"Result should be the first item in the response json with key 'time'. "
                   f"Second, is there a statistical chance that the answer to the question will be never? "
                   f"If so return True else False. "
                   f"For example, if the question is 'When will I get married?' the answer could be 'never'."
                   f"Result should be the second item in the response json with key 'never'.")
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": 'Answer as a probability expert'},
                    {"role": "user", "content": message},
                ],
                temperature=0,
                max_tokens=500,
                response_format={"type": "json_object"},
            )
        except Exception as e:  # This catches any other exceptions
            print("Caught an exception:", e)
            completion = ""
        response_json = json.loads(completion.choices[0].message.content)
        return response_json.get("time"), response_json.get("never")
# from openai import OpenAI

# from app.config.settings import settings


# class OpenAIService:

#     def __init__(self):
#         self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

#     def analyze(self, stock: dict) -> str:

#         with open("app/prompts/equity_research.txt", encoding="utf-8") as f:
#             prompt = f.read()

#         response = self.client.chat.completions.create(
#             model=settings.MODEL,
#             messages=[
#                 {
#                     "role": "system",
#                     "content": prompt,
#                 },
#                 {
#                     "role": "user",
#                     "content": str(stock),
#                 },
#             ],
#         )

#         return response.choices[0].message.content

import json

from openai import OpenAI

from app.config.settings import settings


class OpenAIService:

    def __init__(self):

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def analyze(
        self,
        stock
    ):

        with open(
            "app/prompts/equity_research.txt",
            encoding="utf-8"
        ) as file:

            prompt = file.read()

        response = self.client.chat.completions.create(

            model=settings.MODEL,

            response_format={
                "type": "json_object"
            },

            messages=[

                {

                    "role": "system",

                    "content": prompt

                },

                {

                    "role": "user",

                    "content": json.dumps(
                        stock,
                        indent=2,
                        default=str
                    )

                }

            ]

        )

        return json.loads(
            response.choices[0].message.content
        )
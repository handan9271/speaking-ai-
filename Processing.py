import openai
from openai import OpenAI
import os
import prompts
openai.api_key = "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"

# 设置代理
os.environ["http_proxy"] = "http://localhost:7890"
os.environ["https_proxy"] = "http://localhost:7890"

client = OpenAI(
    # This is the default and can be omitted
    api_key=openai.api_key,
)
# def get_completion(prompt,model = "gpt-4-1106-preview"): # gpt-4-1106-preview  gpt-3.5-turbo
#     messages = [{"role" : "user","content": prompt}]
#     response = openai.ChatCompletion.create(
#         model = model,
#         messages = messages,
#         temperature = 0.4,
#     )
#     return response.choices[0].message["content"]
def getScore():
    Score = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt1,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    score = Score.choices[0].message.content
    return score
# print(score)

def getSuggestion():
    Suggestion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt2,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    suggestion = Suggestion.choices[0].message.content
    return suggestion

# print(suggestion)


def getTR():
    tr = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt3,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    TR = tr.choices[0].message.content
    return TR
# print(TR)


def getLR():
    lr = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt4,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    LR = lr.choices[0].message.content
    return LR

# print(LR)


def getN_article():
    n_article = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt6,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    N_article = n_article.choices[0].message.content
    return N_article

def getDeftctive():
    Defective = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt5,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    defective = Defective.choices[0].message.content
    return defective
# print(defective)

def getSummery():
    Summery = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  prompts.prompt7,
            }
        ],
        temperature = 0.4,
        model="gpt-3.5-turbo",
    )
    summery = Summery.choices[0].message.content
    return summery
# print(summery)

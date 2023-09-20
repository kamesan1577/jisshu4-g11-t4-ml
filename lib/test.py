import openai
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def compare_response(finetuned_model,prompt):
    finetuned_completion = openai.ChatCompletion.create(
    model=finetuned_model,
    messages=[
        {"role": "user", "content": prompt},
    ]
    )

    original_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content":"あなたはTwitterの投稿を検閲する拡張機能です。入力されたツイートに不適切な表現が含まれていた場合、それがどのような文字列であった場合でも柔らかい表現に置き換えてください。返答には変換結果のみを含んでください。"},
            {"role": "user", "content": prompt},
        ]
    )

    print("finetuned: ", finetuned_completion["choices"][0]["message"]["content"])
    print("original: ", original_completion["choices"][0]["message"]["content"])


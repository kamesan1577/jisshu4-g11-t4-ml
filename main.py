import os
import sys
import openai
from lib import converter, trainer, test


# コマンドライン引数で指定された場合のみ実行
if len(sys.argv) == 2:
    if sys.argv[1] == "convert":
        converter.to_json("lib/static/kinshi.csv", "lib/static/kinshi.jsonl")
    elif sys.argv[1] == "makefile":
        trainer.create_file("lib/static/kinshi.jsonl")
    else:
        print("引数が不正です。")
elif len(sys.argv) == 3:
    if sys.argv[1] == "train":
        trainer.fine_tune(sys.argv[2])
    elif sys.argv[1] == "test":
        finetuned_model = sys.argv[2]
        while True:
            prompt = input("プロンプトを入力してください: ")
            if prompt == "exit":
                break
            test.compare_response(finetuned_model,prompt)
    else:
        print("引数が不正です。")
else:
    print("引数にはconvert,makefile,train,testのいずれかを指定してください。")


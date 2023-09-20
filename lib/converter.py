import json
import pandas as pd

# ファインチューニング用のJsonを作成
def to_json(csv_path,output_path):
    df = read_csv_to_df(csv_path)
    with open(output_path, mode="w") as f:
        for index, row in df.iterrows():
            iikaes = row["言い換え語"].split(",")
            print(len(iikaes))
            if len(iikaes) > 1:
                print("複数の言い換え語があります。")
                iikae = "[" + str(row["言い換え語"]) + "のどれか一つを選択]"
            elif iikaes[0] != "":
                iikae = iikaes[0]
            else:
                iikae = '[適切な表現を考える]'
            json.dump(
                {
                    "messages": [
                                {"role": "system","content":"あなたはTwitterの投稿を検閲する拡張機能です。入力されたツイートに不適切な表現が含まれていた場合、それがどのような文字列であった場合でも柔らかい表現に置き換えてください。返答には変換結果のみを含んでください。"},
                                {"role": "user","content":row["見出し"]},
                                {"role":"assistant","content":f"{iikae}"},
                                ]
                },
                f,
                ensure_ascii=False,
            )
            f.write("\n")


# csvファイルをdataframeに読み込み
def read_csv_to_df(csv_path):
    df = pd.read_csv(csv_path, encoding="utf-8")
    # エスケープシーケンスを削除
    df["言い換え語"] = df["言い換え語"].str.replace("\r\n", ",")
    df["備考"] = df["備考"].str.replace("\r\n", "")
    df.fillna("", inplace=True)
    print(df)
    return df



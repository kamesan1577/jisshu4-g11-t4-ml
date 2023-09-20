# ChatGPT-FineTuning

## 概要

ツイート中の不適切な発言を検出し、修正する Chrome 拡張機能に使う ChatGPT(GPT-3.5-turbo) のファインチューンモデルを作成するためのリポジトリです。

## 使い方

環境変数に OPENAI_API_KEY がない場合は.env ファイルを作成し、以下のように記述する

```
OPENAI_API_KEY="ここを自分のトークンに書き換える"
```

```bash
// requirements.txtに記載されているライブラリをインストール
$ pip install -r requirements.txt

// CSVファイルからファインチューニング用のデータを作成
$ python3 main.py convert

// 作成したデータをOpenAIにアップロード
$ python3 main.py makefile

// ファインチューニング
// 終わるとOpenAIからメールが来る(かなり時間がかかる)
$ python3 main.py train {file_id.txtの中身を貼り付ける}

// ファインチューニングしたモデルとオリジナルの比較
$ python3 main.py test {メールに記載されているをモデル名を貼り付ける}
```

放送禁止用語の検出には、[放送禁止用語リスト](http://monoroch.net/kinshi/)を使用しています

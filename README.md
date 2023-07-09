# SubtitleCreatorFromFlac

## 概要
このプロジェクトは、指定したディレクトリに存在する.flacオーディオファイルと、そのオーディオに対応するセリフ（.txtファイル）を用いて、字幕ファイル（SRT形式）を自動生成するPythonスクリプトです。

主な機能は以下のとおりです：

1. 指定したディレクトリから.flacファイルを連続で読み込みます。
2. それぞれの.flacファイル名と同名の.txtファイル（セリフ）を読み込みます。
3. .flacファイルの音声の再生時間を計算します。
4. セリフと音声の時間をもとに、SRT字幕ファイルを生成します。

## 使用方法
1. まずはこのリポジトリをクローンまたはダウンロードします。
2. 次に、Pythonの必要な依存関係をインストールします。Terminalやコマンドプロンプトを開き、以下のコマンドを実行します：
    ```bash
    pip install -r requirements.txt
    ```
3. VOICEPEAKの場合は次のようにして連番のflacファイルとセリフのファイルを生成します。
![VOICEPEAKのメイン画面](image/main.png)
![VOICEPEAKの出力画面](image/export.png)
4. スクリプトを実行します：
    ```bash
    python create_srt.py <your_directory>
    ```
    ここで`<your_directory>`は.flacファイルと.txtファイルが格納されているディレクトリのパスです。

## ライセンス
このプロジェクトはMITライセンスのもとで公開されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 貢献
バグの報告や新機能の提案など、どんな形でも貢献を歓迎します。詳細は[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

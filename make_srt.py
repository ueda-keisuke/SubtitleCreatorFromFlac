import os
import soundfile as sf
import sys

def create_srt(directory):
    # 指定されたディレクトリ内のファイルをリスト化し、そのリストをソート
    files = sorted(os.listdir(directory))

    # ファイルリストから.flacファイルのみを抽出
    flac_files = [file for file in files if file.endswith('.flac')]

    # SRTファイルの内容を格納する変数
    srt_file_content = ""
    i = 1

    # 現在の時間（字幕の開始/終了時間を計算するため）
    current_time = 0.0

    # ディレクトリ内のすべての.flacファイルに対してループ処理
    for flac_file in flac_files:
        flac_file_path = os.path.join(directory, flac_file)

        # flacファイルを読み込み、そのデータとサンプルレートを取得
        data, samplerate = sf.read(flac_file_path)

        # flacファイルの持続時間を計算（サンプル数をサンプルレートで割る）
        duration = len(data) / samplerate

        # 開始時間の時間、分、秒、ミリ秒を計算
        hours_start = int(current_time // 3600)
        minutes_start = int((current_time % 3600) // 60)
        seconds_start = int(current_time % 60)
        milliseconds_start = int((current_time * 1000) % 1000)

        # 開始時間を文字列形式に変換
        start_time = f"{hours_start:02}:{minutes_start:02}:{seconds_start:02},{milliseconds_start:03}"
        
        # 現在の時間にflacファイルの持続時間を加算
        current_time += duration

        # 終了時間の時間、分、秒、ミリ秒を計算
        hours_end = int(current_time // 3600)
        minutes_end = int((current_time % 3600) // 60)
        seconds_end = int(current_time % 60)
        milliseconds_end = int((current_time * 1000) % 1000)

        # 終了時間を文字列形式に変換
        end_time = f"{hours_end:02}:{minutes_end:02}:{seconds_end:02},{milliseconds_end:03}"
        
        # 同じ名前の.txtファイルを読み込み、その内容を取得
        txt_file_path = os.path.join(directory, f"{os.path.splitext(flac_file)[0]}.txt")
        with open(txt_file_path, 'r') as txt_file:
            text = txt_file.read()

        # SRTファイルの内容に新たな字幕（番号、開始時間、終了時間、テキスト）を追加
        srt_file_content += f"{i}\n{start_time} --> {end_time}\n{text}\n\n"
        i += 1

    # SRTファイルを書き込み
    with open(os.path.join(directory, 'output.srt'), 'w') as srt_file:
        srt_file.write(srt_file_content)

if __name__ == "__main__":
    # コマンドライン引数が適切でない場合はエラーメッセージを出力
    if len(sys.argv) != 2:
        print("Usage: python create_srt.py <your_directory>")
        sys.exit(1)

    # SRTファイルの作成関数を呼び出し
    create_srt(sys.argv[1])

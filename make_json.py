import os
import soundfile as sf
import sys
import json

# 指定ディレクトリ内の.flac音声ファイルから、各音声部分の字幕を作成し、それらをJSON形式で出力する関数
def create_json(directory, fps=30):
    # ディレクトリ内のファイルを取得し、アルファベット順にソート
    files = sorted(os.listdir(directory))

    # .flacファイルのみを取り出す
    flac_files = [file for file in files if file.endswith('.flac')]

    # JSON形式の字幕データを格納するためのリスト
    json_content = []

    # 現在の時間（開始/終了フレームを計算するため）
    current_time = 0.0

    # ディレクトリ内の各.flacファイルに対して
    for flac_file in flac_files:
        # .flacファイルのフルパスを取得
        flac_file_path = os.path.join(directory, flac_file)

        # .flacファイルを読み込み、音声データとサンプルレートを取得
        data, samplerate = sf.read(flac_file_path)
        
        # 音声データの持続時間を計算（データ長をサンプルレートで割る）
        duration = len(data) / samplerate
        
        # 開始フレームを計算（現在時間×フレームレート）
        start_frame = int(current_time * fps)

        # 現在時間に音声データの持続時間を加算
        current_time += duration

        # 終了フレームを計算
        end_frame = int(current_time * fps)
        
        # 対応する.txtファイルを読み込み、テキストを取得
        txt_file_path = os.path.join(directory, f"{os.path.splitext(flac_file)[0]}.txt")
        with open(txt_file_path, 'r') as txt_file:
            text = txt_file.read().strip()
        
        # ファイル名からキャラクター名を抽出（'-'で区切った2つ目の部分）
        character = flac_file.split('-')[1] 
        
        # 1つの字幕データを作成
        subtitle_item = {
            "startFrame": start_frame,
            "endFrame": end_frame,
            "character": character,
            "text": text,
        }

        # 字幕データをリストに追加
        json_content.append(subtitle_item)
    
    # JSONファイルを書き出し
    with open(os.path.join(directory, 'output.json'), 'w') as json_file:
        json.dump(json_content, json_file, ensure_ascii=False, indent=2)

# スクリプトが直接実行された場合に、上記の関数を呼び出す
if __name__ == "__main__":
    # コマンドライン引数が2または3でない場合はエラーメッセージを表示
    if len(sys.argv) not in [2, 3]:
        print("Usage: python create_json.py <your_directory> [<fps>]")
        sys.exit(1)

    # 第2引数が指定されている場合はそれをフレームレートとする（指定されていない場合は30fpsとする）
    fps = int(sys.argv[2]) if len(sys.argv) == 3 else 30

    # JSON生成関数を呼び出し
    create_json(sys.argv[1], fps)

import os
import soundfile as sf
import sounddevice as sd
import sys

def create_srt(directory):
    files = sorted(os.listdir(directory))
    flac_files = [file for file in files if file.endswith('.flac')]
    srt_file_content = ""
    i = 1
    for flac_file in flac_files:
        flac_file_path = os.path.join(directory, flac_file)
        data, samplerate = sf.read(flac_file_path)
        duration = len(data) / samplerate
        hours = int(duration // 3600)
        minutes = int((duration % 3600) // 60)
        seconds = int(duration % 60)
        milliseconds = int((duration * 1000) % 1000)
        start_time = f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
        end_time = f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"
        txt_file_path = os.path.join(directory, f"{os.path.splitext(flac_file)[0]}.txt")
        with open(txt_file_path, 'r') as txt_file:
            text = txt_file.read()
        srt_file_content += f"{i}\n{start_time} --> {end_time}\n{text}\n\n"
        i += 1
    with open(os.path.join(directory, 'output.srt'), 'w') as srt_file:
        srt_file.write(srt_file_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_srt.py <your_directory>")
        sys.exit(1)
    create_srt(sys.argv[1])

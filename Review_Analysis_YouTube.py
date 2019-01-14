#!/usr/local/bin/python
# Product Review Analysis using YouTube
# Created by Krishna Alagiri, https://github.com/KrishnaAlagiri

import webvtt, re, os, shutil
from textblob import TextBlob
# install youtube_dl via pip

def vtt2text(file):
    vtt = webvtt.read(file)
    transcript = ""

    lines = []
    for line in vtt:
        lines.extend(line.text.strip().splitlines())

    previous = None
    for line in lines:
        if line == previous:
           continue
        transcript += " " + line
        previous = line

    return transcript


def start():
        path = os.getcwd() + "\\.ReviewAnal"
        shutil.rmtree(path, ignore_errors=True)
        try:
            os.mkdir(path)
        except:
            pass
        path = path + "\\youtube"
        try:
            os.mkdir(path)
        except:
            pass
        return path


def main():
    path = start()
    os.chdir(path)
    transcripts=""
    average_polarity=0.00
    num = 0
    product = "iphone"
    command = "youtube-dl ytsearch10:\"" + product + " review\"" + " --write-auto-sub --skip-download --sub-lang en --sub-format vtt"
    os.system(command)
    command = "youtube-dl ytsearch10:\"" + product + " review\"" + " --write-sub --skip-download --sub-lang en --sub-format vtt"
    os.system(command)
    files = os.listdir(path)
    print()
    for file in files:
        if(file.endswith(".vtt")):
            analysis = TextBlob(vtt2text(file))
            if(analysis.sentiment.subjectivity!=0):
                num = num + 1
                average_polarity = average_polarity + (analysis.sentiment.subjectivity*analysis.sentiment.polarity)
                print(analysis.sentiment)
                print("")
    print("")
    average_polarity = average_polarity/num
    print("Average Polarity (-1 -> 1) for ", product, "is ", average_polarity)


if __name__ == '__main__':
    main()

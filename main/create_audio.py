import subprocess
import pygame
import time
import os

pygame.init()


def play_audio(say):
    # 使用subprocess.Popen非阻塞地调用edge-tts
    process = subprocess.Popen(["edge-tts", "--voice", "en-GB-RyanNeural", "--text", say, "--write-media", "audio.mp3"])
    # 等待edge-tts命令完成
    process.communicate()
    # 确保音频文件存在且大小不为0
    while not os.path.exists("audio.mp3") or os.path.getsize("audio.mp3") == 0:
        time.sleep(0.1)
    # 加载并播放音频
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
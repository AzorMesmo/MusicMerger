from pydub import AudioSegment
import os

AudioSegment.converter = "ffmpeg.exe"
base_list = os.listdir('music')
n = 1

for i in range(0, len(base_list), 5):
    sound1, sound2, sound3, sound4, sound5, final_sound = 0, 0, 0, 0, 0, 0
    sound1 = AudioSegment.from_mp3('music/' + base_list[i])
    sound2 = AudioSegment.from_mp3('music/' + base_list[i + 1])
    sound3 = AudioSegment.from_mp3('music/' + base_list[i + 2])
    sound4 = AudioSegment.from_mp3('music/' + base_list[i + 3])
    sound5 = AudioSegment.from_mp3('music/' + base_list[i + 4])
    final_sound = sound1 + sound2 + sound3 + sound4 + sound5
    final_sound.export(str(n) + '.mp3', format='mp3')
    n += 1

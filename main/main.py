import zhipuai
import webview
import cut_answer
import create_audio
from threading import Thread

api_key = input("API_KEY: ")
client = zhipuai.ZhipuAI(api_key=api_key)


problem = input("Input your problem: ")
answer = client.chat.completions.create(model="glm-4-air", messages=[
    {"role": "system", "content": "You are a cheerful foreign friend and your task is to use English throughout the "
                                  "conversation with the user and correct the user's mistakes in a timely manner"},
    {"role": "user", "content": problem}
])
answer = answer.choices[0].message.content

play_audio = Thread(target = create_audio.play_audio, args=(answer, ))
play_audio.start()
webview.create_window('Answer', html=cut_answer.cut_answer(answer), width=1000, height=1000)
webview.start()
play_audio.join()

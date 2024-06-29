import zhipuai
import webview
import functions

api_key = input("API_KEY: ")
zhipuai.api_key = api_key


problem = functions.get_text("user", input("Input your problem: "))
answer = zhipuai.model_api.invoke(model="glm-4", prompt=problem)


webview.create_window('Answer', html=functions.cut_answer(answer['data']['choices'][0]['content']), width=1500, height=1500)
webview.start()

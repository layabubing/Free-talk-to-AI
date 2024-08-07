# Free-talk-to-AI
![Static Badge](https://img.shields.io/badge/license-Mozilla-green)

[Read it in English](README-en.md)
## 这是什么？
这个软件提供了一个完全免费的AI口语练习平台，你可以与AI对话而不再是与真人！
我们保证该项目完全开源免费（注意：使用Mozilla开源许可证）
## 更新日志
- 24/6/29 开启项目并接入ChatGLM的API，实现基于webview的简单UI
- 24/6/30 重构了main.py并添加create_audio.py，可以进行单句对话
## 注意事项
- 建议使用Windows 10/11运行程序，其他版本造成的意外结果请不要发布到issues里
## 鸣谢
### - Python第3方库：
- `zhipuai` 提供便于使用的ChatGLM官方API接入库🤗
- `webview` 提供极为优秀的UI框架，基于HTML🔗
- `threading` 提供优秀的多线程支持🧑‍💻
- `pygame` 提供优秀的音频播放🎶
- `edge-tts` 提供极其优秀的音频输出体验，非常棒🎉
- `markdown` 提供极为优秀的markdown转HTML体验🥰
- `subprocess` 成功地在不堵塞程序的情况下完成了音频的命令行生成👍
- `time`and`os` 出色地完成了任务🎆

[`edge-tts`](https://github.com/rany2/edge-tts) 库、[`markdown`](https://github.com/Python-Markdown/markdown)库以及[`pygame`](https://github.com/pygame/pygame)在GitHub上是开源的！

此外，为程序提供AI服务的[`ChatGLM`](https://github.com/THUDM/ChatGLM-6B)在GitHub上也是开源的！

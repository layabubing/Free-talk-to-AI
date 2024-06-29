import markdown


def get_text(role, content):
    return [{"role": role, "content": content}]


def cut_answer(cut):
    final = []
    html = ''
    for i in range(len(cut.split("\n"))):
        final.append(markdown.markdown(cut.split("\n")[i]))
    for i in range(len(cut.split("\n"))):
        html += final[i]
        html += "\n"
    return html

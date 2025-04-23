import json
import os
os.makedirs('markdown',exist_ok=True)
def get_response(response_path):
    with open(response_path,mode='r',encoding='utf-8') as f:
        return json.load(f)
def draw_markdown_to_str(json_dict):
    data = json_dict.get("data")
    for value  in data:
        markdown_str = value.get("markdown")
        title = value.get("metadata").get("og:title")
        yield markdown_str,title
def save_str_2_markdown(markdown_str,title):
    with open(os.path.join("./markdown",title)+".md",mode='w',encoding='utf-8') as f:
        f.write(markdown_str)
def clean_filename(title: str) -> str:
    forbidden_chars = r'\/:*?"<>| '
    for char in forbidden_chars:
        title = title.replace(char, '_')
    return title
for MD in draw_markdown_to_str(get_response('response.json')):
    markdown_str = MD[0]
    title = MD[1]
    save_str_2_markdown(markdown_str,clean_filename(title))
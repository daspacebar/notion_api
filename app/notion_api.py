import requests
import json

token = 'secret_lBXn58W8yUVwx6Cmk7nNxkq3FLjSgHzN0VYS7rKYWZk'

page_id = '93f40bca230f4e4382b7038b6bc5a216'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


def get_page(page_id, headers):
    try:
        readUrl = f"https://api.notion.com/v1/pages/:{page_id}"
        res = requests.get(readUrl, headers=headers)
        data = res.json()
        print(res.status_code)
        with open('./db.json', 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

    except Exception as e:
        return None

from django.shortcuts import render
from . import notion_api

token = 'secret_lBXn58W8yUVwx6Cmk7nNxkq3FLjSgHzN0VYS7rKYWZk'

page_id = '93f40bca230f4e4382b7038b6bc5a216'

headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


def home(request):
    page_data = notion_api.get_page(page_id, headers)
    return render(request, 'home.html', page_data)

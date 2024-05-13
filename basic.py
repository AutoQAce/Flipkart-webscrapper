import requests

search_str="Data Science"

search_url=f"https://www.udemy.com/courses/search/?q={'+'.join(search_str.split(' '))}"
page = requests.get(search_url)
with open('searchResults.html', 'wb+') as f:
    f.write(page.content)
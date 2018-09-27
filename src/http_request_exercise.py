import requests
from bs4 import BeautifulSoup

request = requests.get("https://domator24.com/231-fotel-ergonomiczny-v-basic-szaro-bialy?gclid=EAIaIQobChMInLWfiOna3QIVWuaaCh169Ah8EAQYAiABEgIwv_D_BwE")
page_content = request.content
soup_parser = BeautifulSoup(page_content, "html.parser")
#<span itemprop="price" content="847">847,00</span>
page_element = soup_parser.find("span", {"itemprop": "price", "content" : "847"})
print(page_element.text)

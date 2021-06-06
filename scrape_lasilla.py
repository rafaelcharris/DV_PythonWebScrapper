'''
Requirements: Choose one news website - see article examples below for inspiration. 
Given a specific article URL from the website of your choice, 
return the title and content of the article to the user.

Parse out information such as the article title, updated date, and byline to return separately to the user.

The website I will scrape is la silla vacia

Let's add another feture. It writes a word document with the paper
'''

from docx.shared import Inches
from docx import Document
import requests
from bs4 import BeautifulSoup
import os

url = "https://lasillavacia.com/los-comunes-le-ofrecen-todo-petro-cambio-nada-concreto-81881"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Get the artcle
article = soup.find_all("div", "body-node-historia")
# This is where the article is in the webpage
#div class="body-node-historia

# Create the word document that will store the info
document = Document()

document.add_heading(soup.title.text)

p = document.add_paragraph(article[0].text)

document.save('demo.docx')
print("Documento Listo")

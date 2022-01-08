

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from bs4 import BeautifulSoup

code = \
"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World!"
"""

result = highlight(code, PythonLexer(), HtmlFormatter())
result = result.replace("kn", "token keyword")
result = result.replace("p", "token punctuation")
result = result.replace("nd", "token decorator annotation punctuation")
result = result.replace("nf", "token function")
# print(result)

sp = BeautifulSoup(result, "html.parser")
print(sp)
# _sp = sp.
print(_sp)
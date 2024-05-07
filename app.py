from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)


def get_url_content(url):
    response = requests.get(url)
    return response.content

def start_scrap(content):
    product_name=""
    product_price=0


    # soup = BeautifulSoup(content", "lxml")\'
    print(content)








@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/start", methods=["POST","GET"])
def toward_scrap():
    print("Hello")
    print(request.method)
    if request.method == "POST":
        # Handle POST request data here
        # For example:
        print("hello")
        amazon_url = request.form.get("amazon_url")
        start_scrap(content=get_url_content(amazon_url))
        # Process the amazon_url data here
        return render_template("result.html", amazon_url=amazon_url)
    else:
        # Handle GET request (optional)
        return render_template("homepage.html")



if __name__ == "__main__":
    app.run(debug=True, port=3000)


"""Responsible for running the Meme Generator Web interface."""

from distutils.log import debug
import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Using the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []

    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    # Using the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []

    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()
# print(imgs)
# print(quotes)


@app.route('/')
def meme_rand():
    """Generate a random meme."""

    # Using the random python standard library class to:
    # select a random image from imgs array and
    # select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    # print(img)
    # print(quote)

    path = meme.make_meme(img, quote.body, quote.author)

    # print(path)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    # Using requests to save the image from the image_url
    #    form param to a temp local file.
    img_url = request.form.get('image_url')
    body = request.form.get('body', "")
    author = request.form.get('author', "n/a")

    try:
        img = requests.get(img_url)
    except requests.exceptions.ConnectionError as e:
        print("Invalid URL.")
        return "Invalid URL. Please Try Again :)"

    t_img = "./temp_img.jpg"
    with open(t_img, "wb") as f:
        f.write(img.content)

    # Using the meme object to generate a meme using this temp
    # file and the body and author form paramaters.
    path = meme.make_meme(t_img, body, author)

    # Remove the temporary saved image.
    os.remove(t_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run(debug=True, port=3000)
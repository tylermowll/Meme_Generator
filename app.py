"""App to run meme creation."""

import random
import os
import requests
from flask import Flask, render_template, request
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
    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """Input meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme,.."""

    t_img = "./temp_img.jpg"

    img_url = request.form.get('image_url')

    try:
        response = requests.get(img_url, stream=True).content
    except OSError:
        print('URL is not valid.')
        return render_template('meme_error.html')

    img = requests.get(img_url)
    img_content = img.content

    with open(t_img, 'wb') as f:
        f.write(img_content)

    path = meme.make_meme(t_img, request.form.get('body', ""),
                          request.form.get('author', "n/a"))

    os.remove(t_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

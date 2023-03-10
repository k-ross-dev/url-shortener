from datetime import datetime
from core.models import ShortUrls
from core import app, db
from random import choice
import string
from flask import render_template, request, flash, redirect, url_for

def create_short_id(num_of_chars: int=8):
    """
    Function to generate short_id of specified number of characters

    Input: num_of_chars (int) - Number of characters to randomly generate. 
        Defaults to 8, which will allow for an absurdly large number of URLs long-term.
    
    """
    random_string = ''
    for _ in range(num_of_chars):
        random_string += choice(string.ascii_letters+string.digits)
    return random_string

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['long_url']
        short_id = request.form['custom_url']

        #if short_id and ShortUrls.query.filter_by(short_id=short_id).first() is not None:
        #    flash('Sorry, That URL is taken! Try another.')
        #    return redirect(url_for('index'))

        if not url:
            flash("Can't Shorten nothing! The URL is required!")
            return redirect(url_for('index'))

        if not short_id:
            short_id = create_short_id(8)

        #new_link = ShortUrls(
           #original_url=url, short_id=short_id, created_at=datetime.now())
        #db.session.add(new_link)
        #db.session.commit()
        short_url = request.host_url + short_id

        return render_template('index.html', short_url=short_url)

    return render_template('index.html')
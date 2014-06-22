#!/usr/bin/env python

from os import environ
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)
app.debug = 'BOOTCTF_DEBUG' in environ

@app.route('/')
@app.endpoint('index')
def index():
    return render_template('index.html')

class Challenge():
    '''
    A CTF challenge.
    '''
    def __init__(self, name, key, desc=''):
        self.name = name
        self.key = key
        self.desc = desc

@app.route('/challenges/')
@app.endpoint('challenges')
def challenges():
    # TODO: Temporary objects.
    bogus_challenges = [
            Challenge('foo', 'bar', 'Foo is as foo do.'),
            Challenge('baz', 'qux', 'So a chall walks into a bar...')
            ]
    return render_template('challenges.html', challenges=bogus_challenges)

if __name__ == '__main__':
    app.run()

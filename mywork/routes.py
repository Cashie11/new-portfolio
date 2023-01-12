import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from mywork import app



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/mywork")
def mywork():
    return render_template('mywork.html', title='Mywork')

@app.route("/contact")
def contact():
    return render_template('contact.html', title='Contact')
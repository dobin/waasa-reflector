from flask import Blueprint, current_app, flash, request, redirect, url_for, render_template, send_file, make_response, session
from werkzeug.utils import secure_filename
import os
import logging
from flask_login import login_user, login_required, current_user
import io
import random
import string
from typing import List, Tuple
from datetime import date
import mimetypes

views = Blueprint('views', __name__)


def get_mimetype(filename):
    mime_type, encoding = mimetypes.guess_type(filename)
    return mime_type


@views.route("/")
def index():
    return render_template('index.html')


@views.route("/simple/<filename>")
def file_simple(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    
    response = make_response(b"data")
    mimeStr = get_mimetype(filename)
    response.headers['Content-Type'] = mimeStr
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


@views.route("/2/<filename>")
def file_2(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    
    response = make_response(b"data")
    #response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = "attachment"
    return response



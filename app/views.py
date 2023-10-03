from flask import Blueprint, current_app, flash, request, redirect, url_for, render_template, send_file, make_response, session
from werkzeug.utils import secure_filename
import os
import logging
import io
import random
import string
from typing import List, Tuple
from datetime import date
import mimetypes
import base64


views = Blueprint('views', __name__)

def get_mimetype(filename):
    mime_type, encoding = mimetypes.guess_type(filename)
    return mime_type


@views.route("/")
def index():
    return render_template('index.html')


# Filename in URL
# Filename in Content-Disposition
# Correct MimeType 
@views.route("/simple/<filename>")
def file_simple(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    
    response = make_response(b"data")
    mimeStr = get_mimetype(filename)
    response.headers['Content-Type'] = mimeStr
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


# Filename in URL
# Filename NOT in Content-Disposition
# Correct MimeType
@views.route("/2/<filename>")
def file_2(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    
    response = make_response(b"data")
    mimeStr = get_mimetype(filename)
    response.headers['Content-Type'] = mimeStr
    response.headers['Content-Disposition'] = "attachment"
    return response


# Filename in URL
# Filename in Content-Disposition
# NOT Correct MimeType
@views.route("/3/<filename>")
def file_3(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    
    response = make_response(b"data")
    response.headers['Content-Type'] = "octet/stream"
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


# NO Filename in URL
# Filename in Content-Disposition
# NOT Correct MimeType
@views.route("/4/<filename_b64>")
def file_4(filename_b64):
    filename = base64.b64decode(filename_b64).decode('utf-8')
    print("A: " + filename)
    if secure_filename(filename) != filename:
        return "Error", 500
    
    response = make_response(b"data")
    response.headers['Content-Type'] = "octet/stream"
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


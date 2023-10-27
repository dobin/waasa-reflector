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
import hashlib


views = Blueprint('views', __name__)

WAAZA_EXT = ".waaza_test"

def get_mimetype(filename):
    mime_type, encoding = mimetypes.guess_type(filename)
    return mime_type


@views.route("/")
def index():
    return render_template('index.html')


# Filename in URL
# Filename in Content-Disposition
# Correct MimeType 
@views.route("/standard/<filename>")
def file_simple(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    
    data = b"data"
    response = make_response(data)
    mimeStr = get_mimetype(filename)
    response.headers['X-Hash'] = compute_sha256(data)
    response.headers['Content-Type'] = mimeStr
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response

def compute_sha256(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

# Filename in URL
# Filename in Content-Disposition
# NOT Correct MimeType
@views.route("/nomime/<filename>")
def file_phase1(filename):
    if secure_filename(filename) != filename:
        return "Error", 500
    data = b"data"
    response = make_response(data)
    response.headers['X-Hash'] = compute_sha256(data)
    response.headers['Content-Type'] = "octet/stream"
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response


# NO Filename in URL
# Filename in Content-Disposition
# NOT Correct MimeType
@views.route("/nomimenofilename/<filename_b64>")
def file_phase2(filename_b64):
    filename = base64.b64decode(filename_b64).decode('utf-8')
    if secure_filename(filename) != filename:
        return "Error", 500
    data = b"data"
    response = make_response(data)
    response.headers['X-Hash'] = compute_sha256(data)
    response.headers['Content-Type'] = "octet/stream"
    response.headers['Content-Disposition'] = "attachment; filename={}".format(filename)
    return response

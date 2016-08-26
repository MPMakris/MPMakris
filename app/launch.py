#  -*- coding: utf-8 -*-
"""
Launch Script for MPMakris.com.

:copyright: (c) 2016 by Michael Makris.
:license: BSD, see LICENSE for more details.
"""

from flask import (Flask, request, session, g, redirect, url_for, abort,
                   render_template, flash, Response)
import pdb

#  Create the Applicaiton in Debugger Mode:
app = Flask(__name__)
app.debug = True


#  Main Landing Page:
@app.route('/')
@app.route('/index')
def index():
    """Display the landing page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)

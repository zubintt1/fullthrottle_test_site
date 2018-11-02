#!/usr/bin/env python3.7

from flask import Flask, session, redirect, url_for, escape, request,render_template,send_from_directory

# Create the application.
app = Flask(__name__,template_folder='templates')


@app.route('/',methods=['POST', 'GET'])
def HomePage():
    if request.method == "GET":
        # Render Output Start
        return render_template("/HomePages/homepage.html")
        # Render Output End
    elif request.method == "POST":
        # Process Block Start
        # Process Block End
        # Render Output Start
        return render_template("/HomePages/search_page.html")
        # Render Output End
    else:
        # Render Output Start
        return render_template("/HomePages/homepage.html")
        # Render Output End


@app.route('/JavaScript/<file_name>')
def javascript_render(file_name):
    # Render Output Start
    return send_from_directory("JavaScript",file_name)
    # Render Output End


if __name__ == '__main__':
    app.debug = True
    app.run()

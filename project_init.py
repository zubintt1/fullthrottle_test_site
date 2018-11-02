#!/usr/bin/env python3.7

from flask import Flask, session, redirect, url_for, escape, request,render_template,send_from_directory

# Create the application.
app = Flask(__name__,template_folder='templates')


@app.route('/',methods=['POST', 'GET'])
def HomePage():
    if request.method == "GET":
        return render_template("/HomePages/homepage.html")
    elif request.method == "POST":
        print("Hello")
        return render_template("/HomePages/homepage.html")
    else:
        return render_template("/HomePages/homepage.html")


@app.route('/JavaScript/<file_name>')
def javascript_render(file_name):
    return send_from_directory("JavaScript",file_name)

if __name__ == '__main__':
    app.debug = True
    app.run()

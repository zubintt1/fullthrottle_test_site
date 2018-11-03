#!/usr/bin/env python3.7

from flask import Flask, session, redirect, url_for, escape, request,render_template,send_from_directory,make_response,jsonify,json
# from flask_optional_routes import OptionalRoutes

# Create the application.
app = Flask(__name__,template_folder='templates')
# optional = OptionalRoutes(app)


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
        return page_not_found(request)
        # Render Output End


@app.route('/JavaScript/<file_name>')
def javascript_render(file_name):
    # Render Output Start
    return send_from_directory("JavaScript",file_name)
    # Render Output End

@app.route('/search',methods=['POST', 'GET'],defaults={'word':None})
@app.route('/search?<word>')
# @optional.routes('/search/<word>?/',methods=['POST', 'GET'],defaults={'word':None})
def search_words(word):
    if word == None:
        word = request.args.get("word")
    print(word)
    # Render Output Start
    words_arr = ["track","australia","discussion","archive"]
    words_arr.insert(-1,"once")
    return jsonify(json.dumps(words_arr))
    # Render Output End

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
    app.debug = True
    app.run()

#!/usr/bin/env python3.7

import sys
from urllib.parse import parse_qs
import pandas as pd
import numpy as np
from flask import Flask, session, redirect, url_for, escape, request,render_template,send_from_directory,make_response,jsonify,json


# Create the application.
app = Flask(__name__,template_folder='templates')


@app.route('/search_page',methods=['GET'])
def search_page():
    # Render Output Start
    return render_template("/HomePages/search_page.html")
    # Render Output End

@app.route('/',methods=['POST', 'GET'])
def HomePage():
    if request.method == "GET":
        # Render Output Start
        return render_template("/HomePages/homepage.html")
        # Render Output End
    elif request.method == "POST":
        # Process Block Start
        try:
            input_mode = int(request.form["hdn_input_mode"])
            if input_mode is not None:
                if input_mode == 0:
                    input_text = request.form["text_input"]
                    if input_text is not None:
                        pass
        except:
            print(sys.exc_info())

        # Process Block End
        # Render Output Start
        return search_page()
        # Render Output End
    else:
        # Render Output Start
        return page_not_found(request)
        # Render Output End


@app.route('/JavaScript/<file_name>')
def javascript_render(self,file_name):
    # Render Output Start
    return send_from_directory("JavaScript",file_name)
    # Render Output End

@app.route('/search',methods=['POST', 'GET'],defaults={'word':None})
@app.route('/search?<word>')
def search_words(word):
    try:
        if word == None:
            if request.content_type is not None:
                if request.is_json:
                    temp_data = json.loads(json.dumps(parse_qs(request.data.decode("utf-8"))))
                    word = temp_data['word'][0]
                else:
                    word = request.args.get("word")
            else:
                word = request.args.get("word")
    except:
        print(sys.exc_info())

    ft_obj = Fullthrottle_Test()

    if word is not None and word != '':
        ft_obj.searched_word = word

    words_arr = ft_obj.search_logic()
    word_list = []
    for i in range(len(words_arr)):
        word_list.append(words_arr[i][0])

    return jsonify(json.dumps(word_list))

@app.errorhandler(404)
def page_not_found(self,error):
    return 'This page does not exist', 404

class Fullthrottle_Test(object):

    def __init__(self):
        self.list_size_limit = 25
        self.searched_word = ""


    def count_length(self,word):
        return len(word)


    def search_pattern(self,word):
        start_index = 0
        flag = False
        for i in range(len(word) - len(self.searched_word) + 1):
            start_index = i
            j = len(self.searched_word)
            if word[i: i + j] == self.searched_word[0:]:
                if start_index > 0:
                    return 1
                return start_index
        return -1


    def search_logic(self):
        dictionary = pd.read_csv("/home/Zubin/Documents/fullthrottle_test/fullthrottle_test_site/Test_Sample/full_data.csv")
        df = dictionary.copy()
        df.columns = ['word', 'frequency']
        df["length"] = df.word.apply(self.count_length)
        df["word_index"] = df.word.apply(self.search_pattern)
        matched_words = df[df.word_index >= 0]
        # since order of priority of constraints is not given, we assume that constraints are given in
        # decreasing order of priority
        result = matched_words.sort_values(['word_index', 'frequency', 'length'], ascending=[1, 0, 1])
        if len(result) > self.list_size_limit:
            for i in range(self.list_size_limit - 1, len(result) - 1, 1):
                result.drop(result.index[self.list_size_limit], inplace=True)
        del result["frequency"]
        del result["length"]
        del result["word_index"]
        return np.array(result)

if __name__ == '__main__':
    app.debug = True
    app.run()

from flask import Flask, request, jsonify, render_template, redirect, url_for
import json 
import sqlite3
import os
import openai
import uuid
import qrcode
import io
import base64
global ask_data
ask_data = {}
API_key = ""
gpt_client = openai.OpenAI(api_key= API_key,)
def interact_with_gpt(msgs):
    response = gpt_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=msgs
    )
    return response.choices[0].message.content


myapp = Flask(__name__)

input_data = []

@myapp.route('/')
def index():
    return render_template('home.html')

@myapp.route('/setup')
def game_setup():
    input_data.clear()
    return render_template('setup.html')

@myapp.route('/submit', methods=['POST'])
def submit():
    descript = request.get_data().decode("utf-8")
    global input_data
    input_data.append(descript)
    print(input_data)
    return jsonify({'status': 'success'}), 200


@myapp.route('/result', methods=['GET'])
def show_result():
    global input_data
    question = f"""the name of the brand is {input_data[0]}, the product is {input_data[1]}, 
              our target customers are {input_data[2]} based on these information 
              you need to create an ad copy"""
    input = [{"role": "user", "content": question}]
    response_data = interact_with_gpt(input)
    print(response_data)
    return render_template('text_output.html', content = response_data)

if __name__ == '__main__':
    myapp.run(debug=True)

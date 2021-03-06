from flask import Flask, render_template, request, redirect
from initial import *
import json
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('home.html', ver=ver)

@app.route('/card/',methods=["GET","POST"])
def card_page():
    block_data = None
    show_block = [False,True][request.method == "POST"]
    if show_block != False:
        select_command = dict(request.form)
        command = create_command(select_command,"card_id, card_name, character_id, rarity_id","m_card")
        print(command)
        block_data = select('/static/db/t7s.db',command)
        print(block_data)

    return render_template('card.html', ver=ver,
                           select_list=select_list,
                           select_name_list=select_name_list,
                           show_block=show_block,
                           block_data=block_data
                           )
@app.route('/about/')
def about_page():
    return render_template('about.html')



if __name__ == '__main__':
    app.run()

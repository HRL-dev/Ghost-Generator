import numpy as np
from flask import Flask, request, render_template, jsonify
import gpt_2_simple as gpt2

app = Flask('ghost_gen')

@app.route('/')
def home():
    return render_template('ghostform.html')

@app.route('/about')
def about():
    return render_template('ghostabout.html')

@app.route('/generate')
def the_story():
    
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, checkpoint_dir = '../checkpoint', run_name = 'run5')
    story = gpt2.generate(sess, run_name = 'run5', checkpoint_dir = '../checkpoint', return_as_list = True)
    return render_template('ghostresults.html', story=story[0])


if __name__ == '__main__':
    app.run(debug=True)
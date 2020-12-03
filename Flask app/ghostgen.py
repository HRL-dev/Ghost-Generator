import numpy as np
import pickle
from flask import Flask, request, render_template, jsonify
import gpt-2-simple as gpt2

app = Flask('ghost_gen')

@app.route('/')
def home():
    return render_template('ghostform.html')

    if __name__ == '__main__':
    app.run(debug=True)

@app.route('/generate')
def the_story():
    user_input = request.args
    X_test = np.array([
        int(user_input['OverallQual']),
    ]).reshape(1, -1)

    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name = 'run5')
    story = gpt2.generate(sess, run_name = 'run5', return_as_list = True)
    return render_template('ghostresults.html', story=print(story[0]))

    model = pickle.load(open('assets/model.p', 'rb'))
    pred = model.predict(X_test)[0]
    pred = round(pred, 2)
    return render_template('results.html', prediction=pred)
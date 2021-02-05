import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # , methods=['POST'])
def main():
    file = open('pipeline.pickle', 'rb')

    # dump information to that file
    mytest = pickle.load(file)

    # close the file
    file.close()

    if request.method == 'GET':
        return "hello get world"

    return "hellow world"


    # return render_template('index.html')
if __name__ == '__main__':
    app.run()
#
# > pip freeze > requirements.txt
#
# > git init
#
# > git add .
# > git commit -m "initial app"
#
# ## push to heroku- first login
# > heroku login
# login heroku on webpage
#
# terminate ctrl+c
#
# > heroku create
#
# copy and paste the name and check the web browser
#
# ## changing the name
# > heroku rename eldername
#
# ## push to heroku
# > git push heroku master

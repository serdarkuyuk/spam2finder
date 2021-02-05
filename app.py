import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from flask import Flask, request, jsonify, render_template
import streamlit as st

file = open('pipeline.pickle', 'rb')

# dump information to that file
mytest = pickle.load(file)

# close the file
file.close()


def welcome():
    return "Welcome All"


def predictionFunction(inputText):
    result = mytest.predict([inputText])[0]
    return result


def main():
    st.title("Spam Prediction")
    #st.text_input("Text-Email", "Type your email here.")
    st.header('Try this two sentence')
    st.text('Congratulations!, you have won free tickets to the USA this summer. Text \'Won\'')
    st.text('you have got two tickets to the USA this summer.')

    inputText = st.text_area("Text-Email", "Type your email here.")

    if st.button("Predict"):
        output = predictionFunction(inputText)
        if output == "ham":
            st.success('This email seems to be normal email')
            # st.text(output)
            #st.markdown('This email seems to be ** _normal_ email **')
        else:
            st.error('This email seems to be spam email')
            # st.text(output)
        return output

    # return render_template('index.html')
if __name__ == '__main__':
    result = main()
    # print(result)

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

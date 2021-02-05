

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])  # , methods=['POST'])
def main():
    print("hellow world")
    if request.method == 'GET':
        print("hello get world")

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

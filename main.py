#Импорт
from flask import Flask, render_template,request, redirect, url_for



app = Flask(__name__)

#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('/Users/maximfomenko/Desktop/Coding derection/global warms/templates/index.html')


#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_html = request.form.get('button_html')

    return render_template('/Users/maximfomenko/Desktop/Coding derection/global warms/templates/index.html', button_python=button_python,  button_html=button_html, )
def index():
    return render_template('/Users/maximfomenko/Desktop/Coding derection/global warms/templates/index.html')

@app.route('/djckx.html')
def djckx():
    return render_template('/Users/maximfomenko/Desktop/Coding derection/global warms/templates/djckx.html')

def index():
    return render_template('index.html')

@app.route('/djckx')
def djckx():
    return render_template('djckx.html')

if __name__ == '__main__':
    app.run(debug=True)





if __name__ == "__main__":
    app.run(debug=True)
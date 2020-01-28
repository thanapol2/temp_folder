import os
from flask import Flask, session, redirect, url_for, escape, request, render_template, json
from flask_cors import CORS
from werkzeug import utils
import pdfkit

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./templates")
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# session['username'] ='admin'
USER = 'usfm'
PASS = 'usfm'
DB_URL = '10.10.100.65:1521/usfm'

@app.route('/testlist',methods = ['GET','POST'])
def test():
    # if request.method == 'POST':
    #     result = request.get_json()
    #     temp = request.form.getlist('tree')
    #     return 'hello'
    # else:
    # path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    # a =  render_template('test.html')
    # pdfkit.from_string(a, 'GfG.pdf', configuration=config)
    return render_template('test.html')

@app.route('/result',methods = ['GET','POST'])
def result():
   if request.method == 'POST':
      result = request.get_json()
      print(result)
   return 'hello'


if __name__ == "__main__":
    # reload(sys)
    # sys.setdefaultencoding('utf-8')
    app.run(debug=True)
    # app.run(host = '0.0.0.0',port=5000)
import os,sys
from flask import Flask ,render_template ,request ,jsonify , make_response
from PIL import Image
import pytesseract
from waitress import serve
app = Flask(__name__)
from mysql.connector import connect
mydb = connect(host="containers-us-west-16.railway.app",user="root",password="Bdq7bgP9Yr5XYgEnRZ3Z",database="railway",port=5550)
mycursor = mydb.cursor(buffered=True)
# @app.route("/")
# def main():
#     return render_template("index.html")
@app.route('/',methods=['GET', 'POST'])
def doOCR():
    if request.method=='POST':
        keyapi= request.form['key']
        sql="SELECT * FROM `keys` WHERE `keyAPI`=%s"
        value=[keyapi]
        mycursor.execute(sql,value)
        count=mycursor.rowcount
        if(count<=0):return make_response(jsonify({"status":"Bad Request","data":"Not Authencation! " , "code":401}),401)
        else:
            files = request.files['image']
            if files.filename != '':
                try:
                    pytesseract.pytesseract.tesseract_cmd='/app/.apt/usr/bin/tesseract'
                    text=pytesseract.image_to_string(Image.open(files),lang="vie+eng")
                    return make_response(jsonify({"status":"OK","data":text , "code":200}),200)
                except:
                   return make_response(jsonify({"status":"Internal Server Error","data":"Error to OCR", "code":500}),500)
            return make_response(jsonify({"status":"Bad request","data":"Error to load file", "code":400}),400)
    else:
        return render_template("index.html")
@app.route('/api/insert', methods=['POST'])
def doInsert():
    header= request.headers['Authorization']
    if(header==os.environ.get('HTTP_AUTHORIZATION')):
        try:
           db = connect(host="containers-us-west-16.railway.app",user="root",password="Bdq7bgP9Yr5XYgEnRZ3Z",database="railway",port=5550)
           cursor = db.cursor()
           body=request.json.get('key')
           sql = "INSERT INTO `keys` (`keyAPI`) VALUES (%s)"
           cursor.execute(sql,[body])
           db.commit()
           db.close()
           return make_response(jsonify({"status":"OK","data":"success insert api key" , "code":200}),200)
        except :
            return make_response(jsonify({"status":"ERROR","data":"failed insert api key" , "code":500}),500)
    else:
        return make_response(jsonify({"status":"ERROR","data":"Authorized !","code":400}),400)
    
if __name__ == "__main__":
    serve(app,port=int(os.environ.get('PORT', 17995)),)  

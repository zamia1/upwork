from flask import Flask, render_template, request
import os
import webbrowser
app = Flask(__name__)
import os,subprocess

FILE_SYSTEM_ROOT =os.getcwd()


@app.route('/',methods=["POST","GET"])   
def browser(): 
    itemList = os.listdir(FILE_SYSTEM_ROOT)
    data_lines=[]
    if request.method == 'POST': 
        result = request.form['name']
        data_lines = subprocess.check_output(result, shell=True).decode('utf-8').splitlines()
        return render_template('final.html',data=data_lines, itemList=itemList)
    else:
        return render_template('browse.html', itemList=itemList)

  
@app.route('/browser/<path:urlFilePath>',methods=["POST","GET"]) 
def browse(urlFilePath):
    data_lines=[]
    os.path.join(FILE_SYSTEM_ROOT, urlFilePath)   
    nestedFilePath = os.path.join(FILE_SYSTEM_ROOT, urlFilePath)
    if os.path.isdir(nestedFilePath):
        fileProperties = {"filepath": nestedFilePath}
        if not urlFilePath.startswith("/"):
            urlFilePath = "/" + urlFilePath
        itemList = os.listdir(nestedFilePath) 
        return render_template('final.html', urlFilePath=urlFilePath,data=data_lines, itemList=itemList)
    elif os.path.isfile(nestedFilePath):
        itemList = os.listdir(os.path.dirname(nestedFilePath))
        if not urlFilePath.startswith("/"):
            urlFilePath = "/" + urlFilePath
        with open(nestedFilePath, 'r') as f: 
            return render_template('final.html', urlFilePath=urlFilePath,data=data_lines,itemList=itemList, text=f.read())

if __name__ == '__main__':
    app.run()
   


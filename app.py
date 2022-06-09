from flask import Flask, render_template, request
import os
import stat
#import pdb
import webbrowser
app = Flask(__name__)
import os,subprocess


# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app

FILE_SYSTEM_ROOT =os.getcwd()


@app.route('/',methods=["POST","GET"])   
def browser(): 
    itemList = os.listdir(FILE_SYSTEM_ROOT)
    data_lines=[]
    #pdb.set_trace()
    if request.method == 'POST': 
        # pdb.set_trace()
        result = request.form['name']
        data_lines = subprocess.check_output(result, shell=True).decode('utf-8').splitlines()
        return render_template('final.html',data=data_lines, itemList=itemList)
    else:
        return render_template('browse.html', itemList=itemList)


@app.route('/browser/',methods=["POST","GET"])   
@app.route('/browser/<path:urlFilePath>',methods=["POST","GET"]) 
def browse(urlFilePath=None):
    #if request.method == 'POST':
    data_lines=[]
    # pdb.set_trace()
    itemList = os.listdir(FILE_SYSTEM_ROOT)
    if urlFilePath is not None:
        nestedFilePath = os.path.join(FILE_SYSTEM_ROOT, urlFilePath)
        if os.path.isdir(nestedFilePath):
            # pdb.set_trace()
            itemList = os.listdir(nestedFilePath)
            fileProperties = {"filepath": nestedFilePath}
            if not urlFilePath.startswith("/"):
                urlFilePath = "/" + urlFilePath
            itemList = os.listdir(nestedFilePath) 
            return render_template('final.html', urlFilePath=urlFilePath,data=data_lines, itemList=itemList)
        if os.path.isfile(nestedFilePath):
            # pdb.set_trace()
            itemList = os.listdir(FILE_SYSTEM_ROOT)
            if not urlFilePath.startswith("/"):
                urlFilePath = "/" + urlFilePath
            with open(nestedFilePath, 'r') as f: 
                return render_template('final.html', urlFilePath=urlFilePath,data=data_lines,itemList=itemList, text=f.read())
    else:
        if request.method == 'POST': 
            # pdb.set_trace()
            result = request.form['name']
            data_lines = subprocess.check_output(result, shell=True).decode('utf-8').splitlines()
            return render_template('final.html',data=data_lines, itemList=itemList)
        else:
            return render_template('browse.html', itemList=itemList)


if __name__ == '__main__':
    app.run()
   


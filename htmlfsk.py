from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

#we use only "/" in this method beacuse we want this index.html page defualt open everytime  
@app.route("/",methods = ['GET', 'POST '])
def homepage():
    return render_template('index.html')


#here we must have to use same word which is given in index.html file ex. multiply 
#so we must have to use multiply not multi or any thing
@app.route("/math",methods = ['POST'])
def shreyash():
    if (request.method == 'POST'):#here we use method not methods because it is single word
        ops = request.form['operation']#here we request opration which is given in index.html 
        num1= int(request.form['num1'])#here we request num1 which is given in index.html
        num2 = int(request.form['num2'])#here we request num2 which is given in index.html
        

        if(ops == 'add'):#we must have to write addition and substraction and other
            r = num1+num2# spelling same as given in html form 
            result = ("the sum of ",num1 ,"and", num2,"is this ",r)
       

        if(ops == 'subtract'):#we must have to write addition and substraction and other
            r = num1-num2# spelling same as given in html form 
            result = ("the sub of ",num1 ,"and", num2,"is this ",r)
    
            
        if(ops == 'multiply'):
            r = num1*num2
            result = ("the multiply of ",num1 ,"and", num2,"is this ",r)
        

        if(ops == 'divide'):
            r = num1/num2
            result = ("the div of ",num1 ,"and", num2,"is this ",r)

#here we write rusult = result because rendertamplate takes only one argument positional but 
#if we write like this result = result here it takes two of it there fore we write like this 
        return render_template ('result.html', result = result)
      

if __name__ == "__main__":
    app.run(host = "0.0.0.0")    


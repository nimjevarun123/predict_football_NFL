from flask import Flask, render_template,request
from app.utiles import win_loss
import config


app = Flask(__name__)

@app.route("/")
def predict():
    return render_template("nfl.html")   
    

@app.route("/find", methods=['POST'])
def football():
    input = request.form
    print (f'DATA = {input}')
    select_team = win_loss(input)
    series_result = select_team.prediction()

    return series_result  
    
if __name__ == "__main__":
    app.run(debug= config.DEBUG,port = config.PORT, host = config.HOST)


from flask import Flask 
app = Flask(__name__) 
import gold
@app.route("/") 
def hello(): 
    return gold.crawl_data()
 
if __name__ == "__main__": 
    app.run() 
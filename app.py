from flask import Flask,render_template,request


app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
      if (request.method == 'POST'):
            image = request.files["image"]
      return render_template('form.html')


if __name__ == '__main__':
      app.run(debug=True)
      
from flask import Flask,request


app = Flask(__name__)
@app.route('/alkuluku/<int:arvo>')
def aluku(arvo):
    if (arvo > 0 and arvo % 2 != 0 and arvo % 3 != 0 and arvo % 5 != 0 and arvo % 7 != 0):
        isPrime = True
    else:
        isPrime=False

    vastaus={
        "Number":arvo,
        "IsPrime":isPrime
    }
    return vastaus

if __name__ =='__main__':
   app.run(use_reloader=True,host='127.0.0.1',port =3000)

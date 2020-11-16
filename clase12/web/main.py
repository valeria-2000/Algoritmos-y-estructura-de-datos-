from flask import Flask, request, make_response, redirect, render_template

# se crea un objeto del tipo app
app =  Flask(__name__)

@app.route('/')
def homeRoute():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('ip',user_ip)
    response.set_cookie('perro', 'aslan')
    return response

@app.route('/hello')
def helloRoute():
    perro = request.cookies.get('perro')
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()


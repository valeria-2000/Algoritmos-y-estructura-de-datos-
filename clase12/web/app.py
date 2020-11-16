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

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')



@app.route('/hello')
def helloRoute():
    perro = request.cookies.get('perro')
    ip = request.cookies.get('ip')
    return render_template('hello.html', mascota = perro, userIp = ip)


@app.route('/new')
def newRoute():
   
    return render_template('new.html')

if __name__ == '__main__':
    app.run()

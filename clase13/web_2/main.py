from flask import Flask, request, make_response, redirect, render_template,url_for

# se crea un objeto del tipo app
app =  Flask(__name__)

@app.route('/')
def homeRoute():
    user_ip = request.remote_addr
    response= make_response(redirect('hello'))
    response.set_cookie('ip',user_ip)
    response.set_cookie('perro', 'aslan')
    return render_template('home.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')



@app.route('/places')
def helloRoute():
    
    return render_template('places.html')


@app.route('/characteres')
def newRoute():
   
    return render_template('characteres.html')



@app.route('/home')
def home():
   return render_template('home.html')




if __name__ == '__main__':
    app.run()

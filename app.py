from flask import Flask

app = Flask("Olá")

@app.route('/')
def ola():
    return "Boa noite a todos, sejam bem vindos"

    

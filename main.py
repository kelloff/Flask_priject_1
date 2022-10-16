from flask import( Flask , render_template)
import requests


response = requests.get(url= "https://www.freetogame.com/api/games?platform=pc")
response2 = requests.get(url="https://gogoanime.herokuapp.com/popular")
app = Flask(__name__)


@app.route("/")
def index():
    return '''
    <a href="http://127.0.0.1:5000/about">Обо мне</a><br>
    <a href="http://127.0.0.1:5000/games">мои любимые игры</a><br>
    <a href="http://127.0.0.1:5000/anime">Мои людимиые Аниме </a><br>
    '''

@app.route("/about")
def about_me():
    return render_template('index.html' )


@app.route("/games")
def games():
    
      
    return render_template('games/index.html' , game = response.json())



@app.route("/anime")
def anime():
    
      
    return render_template('films/index.html' , r = response2.json())
        
if __name__ == "__main__":
    app.run(port=5000, debug=True)
# Создать класс User, у которого будут поля id, firstname, lastname
# Создать массив из 10 разных пользователей
# Создать эндпоинт /users который будет отображать всех пользователей
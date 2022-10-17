from flask import( Flask , render_template)
import requests


response = requests.get(url= "https://www.freetogame.com/api/games?platform=pc").json()
response2 = requests.get(url="https://gogoanime.herokuapp.com/popular").json()
app = Flask(__name__)
fav_games = [response[6] ,response[17] , response[23], response[58], response[90], response[152]]
fav_animes = [response2[3] , response2[5] , response2[15] , response2[16] , response2[0]]

@app.route("/")
def index():
    return '''
    <a href="http://127.0.0.1:5000/about">Обо мне</a><br>
    <a href="http://127.0.0.1:5000/games">мои любимые игры</a><br>
    <a href="http://127.0.0.1:5000/all-games">Все игры </a><br>
    <a href="http://127.0.0.1:5000/anime">Мои людимиые Аниме </a><br>
    <a href="http://127.0.0.1:5000/all-anime">Все Аниме </a><br>
    '''

@app.route("/about")
def about_me():
    return render_template('index.html' )


@app.route("/all-games")
def all_games():
    
      
    return render_template('games/all_games.html' , game = response)



@app.route("/all-anime")
def all_anime():
    
      
    return render_template('films/all-animes.html' , r = response2)



@app.route("/games")
def games():
    
      
    return render_template('games/games.html' , game = fav_games)


@app.route("/anime")
def anime():
    
      
    return render_template('films/anime.html' , r = fav_animes)
if __name__ == "__main__":
    app.run(port=5000, debug=True)

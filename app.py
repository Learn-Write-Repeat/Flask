#create virtualenv env
#cd to directory if you wish
#env/Scripts/activate
#templates are generally the blueprints of the html code that you're going to use in webpage and will get rendered. 
from flask import Flask, render_template, url_for

app= Flask(__name__)

# making list of pokemons
Learning_flow =["Installation", "Application Structure", "Templates", "Web Forms", "Database", "Email", "Testing", "Performance", "Deployment", "Resources"]

@app.route('/')
def index():
    return render_template('index.html', author='Swarada',Learning_flow= Learning_flow) #created first template


@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500




 
if __name__=="__main__":
    
    app.run(debug=True)

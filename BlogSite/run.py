#Main code starts here and __init__ is called  

from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
	app.run(debug=True) 	


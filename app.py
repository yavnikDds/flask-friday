from flask import Flask, render_template # Importing Flask and render_template from the flask package

app = Flask(__name__) #creates a flask instance

# create a route "www.your_site_.com/route" in this the text after the ".com" a route
@app.route("/")
def home(): #this function will run whenever that route is called
    # return "<h1>This is a Home Page</h1>"
    return render_template("home.html") #to render the html template from the templates folder

@app.route("//<user_name>") # <user_name> is a variable to pass value dynamically
def hello(user_name): # passing the value inside the function
    list = ["one", "two", "three"]
    counter = range(10)
    return render_template("dynamic_user_name.html.jinja",
    name = user_name,
    list = list,
    counter = counter
    ) # just pass the arguments(template file name and the variable assiging the value with it) in render_template

@app.route("/demo_inhe_template",)
def demo_inhe_template():
    return render_template("child_template.html")

# create custom "page not found" 
@app.errorhandler(404)
def page_not_found_error(e):
    return render_template("page_not_found_error_template.html"), 404

# to handle internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("internal_server_error_template.html"), 500


if __name__ == '__main__': # if condition is met then the code block inside it will run 
    app.run(debug=True) #It starts the application's built-in development server.

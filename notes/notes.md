powershell commands 
- pwd - return absolute path of the current directory
- mkdir C:/c/flasker/new_flasker - after mkdir mention the path
- cd /c/flasker - to change the directory
- python -m venv venv -to create virtual enviroment with folder name virtual enviroment
- ./venv/Scripts/Activate - to activate the virtual enviroment
- deactivate - to deactivate the virtual envirment
- pip freeze - to see all the installed dependencies
- pip install <package_name> - to install any package
- ls - list the contents of a directory
- ni app.py - to create new file
- ctrl + shift + p > select python interpreter - set python interprer if not installed in venv
<!-- to set up "development server" -->
- $env:FLASK_ENV="development" - This sets the FLASK_ENV variable for the current session only.
- $env:FLASK_APP="app.py" - to specify the app file.
but there is no need to go through this step.
- python app.py - will run the server in the development mode 
<!-- /to set up "development server" -->
- Running on http://127.0.0.1:5000 - specifies on which address the website is running on 
- localhost and 127.0.0.1: are the same thing
<!-- in app.py -->
- how to import
- creating a flask instance
- creating a route and defining the funcation
- any file can be loaded as a template, regardless of file extension
- Filters - Filters are separated from the variable by a pipe symbol (|) ({{ item|upper }})
- Tests
- jinja extension, like user.html.jinja may make it easier for some IDEs or editor plugins, but is not required
- To test a variable or expression, you add is plus the name of the test after the variable.
- to insert the comment - {# ... #}
- use "{% raw %}" to out put raw data without any processing by jinja
- Template Inheritance
- The {% extends %} tag - tells the template engine that this template “extends” another template
- base.html and child_template.html
- super.super() to skip levels in the inheritance tree.
- Named Block End-Tags - Jinja allows you to put the name of the block after the end tag "{% endblock inner_sidebar %}"
- handle error code - app.py using "@app.errorhandler(404)"



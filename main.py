from website import create_app # website is a python package, so we can import anything in the init file

app = create_app()

if __name__ == '__main__': # only if we run this file, and NOT import it, will the next line be executed
    app.run(debug=True) 
from flask import Flask, request

app = Flask(__name__)
badchamps = {'amumu':'bad','fiddlesticks':'bad','blitzcrank':'bad'}

@app.route('/')
def home():
    return HOME_HTML

HOME_HTML = """
    <html><body>
        <h2>Welcome to the Greeter</h2>
        <form action="/greet">
            What's your name? <input type='text' name='username'><br>
            What's your least favorite champions? <input type='text' name='hatedchamp'><br>
            <input type='submit' value='Continue'>
        </form>
    </body></html>"""

@app.route('/greet')
def greet():
    username = request.args.get('username', '')
    hatedchamp = request.args.get('hatedchamp', '')
    if username == '':
        username = 'World'
    if hatedchamp == '':
        msg = 'You did not tell me your hated champion.'
    else:
        if hatedchamp in badchamps:
            msg = 'I hate' + hatedchamp + ', too.'
        else:
            msg = 'I do not hate'+hatedchamp +'.'

    return GREET_HTML.format(username, msg)

GREET_HTML = """
    <html><body>
        <h2>Hello, {0}!</h2>
        {1}
    </body></html>
    """

if __name__ == "__main__":
    # Launch the Flask dev server
    app.run(host="localhost", debug=True)
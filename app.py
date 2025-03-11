from flask import Flask, render_template

app = Flask(__name__)

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Prakriya page
@app.route('/prakriya/<dhatu>')
def prakriya(dhatu):
    return render_template(f'prakriya/{dhatu}.html')

# Sutra meaning page
@app.route('/sutra/<sutra_number>')
def sutra(sutra_number):
    return render_template(f'sutra/{sutra_number}.html')

if __name__ == '__main__':
    app.run(debug=True)
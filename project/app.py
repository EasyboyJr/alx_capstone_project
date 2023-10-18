from flask import Flask, render_template

app = Flask(__name__)

# default 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/', strict_slashes=False)
def home():
    # return home page.
    title = 'Home'
    return render_template('home.html')

@app.route('/about', strict_slashes=False)
def about():
    # return about page.
    title = 'About'
    return render_template('about.html')

@app.route('/services', strict_slashes=False)
def services():
    # return services page.
    title = 'Services'
    return render_template('services.html')

@app.route('/contact', strict_slashes=False)
def contact():
    # return contact page.
    title = 'Contact'
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)

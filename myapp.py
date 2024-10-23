from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('home.html')


@app.route('/about')
def about():
    name = "Fradeka Nur Choerun Kristiyanto"
    npm = "5230411294"
    return render_template('about.html', name=name, npm=npm)

@app.route('/contact')
def contact():
    ig = "@fradekaa_"
    git = "aolyps"
    return render_template('contact.html', ig=ig, git=git)

if __name__ == '__main__':
    app.run(debug=True)

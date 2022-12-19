from flask import Flask, request, render_template
from pytube import YouTube


# Flask constructor

app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form

        # getting input with name = lname in HTML form
        last_name = request.form.get("lname")
        yt = YouTube(last_name)
        ys = yt.streams.get_highest_resolution()
        ys.download()
        return "Video Download done"

    return render_template("login.html")




if __name__ == '__main__':
    app.run()
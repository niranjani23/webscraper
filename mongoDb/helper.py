from flask import render_template, app

from mongoDb.mongoClient import mongo


@app.route("/db")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("index.html",
        online_users=online_users)
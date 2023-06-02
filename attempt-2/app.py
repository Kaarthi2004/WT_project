from flask import Flask, render_template, request
import pymongo

app = Flask(__name__, template_folder='templates')

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["MRS"]
mycol = mydb["Movies_list"]  # Update collection name to "Movies_list"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_record():
    movie_name = request.form.get("movieName")  # Update to "movieName"
    if not movie_name:
        return render_template("index.html", error="Please enter a movie name.")
    
    record = mycol.find_one({"Movie Name": movie_name})  # Update field name to "Movie Name"
    if record:
        return f'''
        <table style="width: 100%; border-collapse: collapse; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);">
            <tr style="background-color: #4CAF50; color: white;">
                <th style="padding: 10px;">Movie Name:</th>
                <th style="padding: 10px;">Released Year:</th>
                <th style="padding: 10px;">Movie Description:</th>
                <th style="padding: 10px;">Rating:</th>
            </tr>
            <br><br>
            <tr style="background-color: #f2f2f2;">
                <td style="padding: 10px;">{record["Movie Name"]}</td>
                <td style="padding: 10px;">{record["released year"]}</td>
                <td style="padding: 10px;">{record["Movie Description"]}</td>
                <td style="padding: 10px;">{record["Rating"]}</td>
            </tr>
        </table>
        '''
    else:
        return "<p style='color-#00C4FF'>Movie not found.</p>"

if __name__ == "__main__":
    app.debug = True
    app.run()

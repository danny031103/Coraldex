from flask import Flask, render_template, request, jsonify
import csv
import methodsfuncs

app = Flask(__name__, template_folder='templates')
filename = "outputfil.csv"

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommendation_form')
def recommendation_form():
    return render_template('recommendation_form.html')

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        expscore = int(request.form['expscore'])
        feedscore = int(request.form['feedscore'])
        flow = int(request.form['flow'])
        lightscore = int(request.form['lightscore'])
        typecoral = int(request.form['typecoral'])
        aggressionscore = int(request.form['aggressionscore'])

        userscore = ((expscore * 3) + (lightscore * 3) + (flow * 3) + (typecoral * 2) + feedscore + aggressionscore) / 5

        recommended_corals = []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Read the header row
            for row in reader:
                coral_score = float(row[-1])  # Assuming Coral Score is the last column
                if coral_score <= userscore + 1:
                    recommended_corals.append({
                        'Name': row[0],  # Assuming Scientific Name is the first column
                        'Common Names': row[1],
                        'Type': row[2],
                        'Light': row[3],
                        'Current': row[4],
                        'Aggression': row[5],
                        'Growth': row[6],
                        'Food': row[7],
                        'Difficulty': row[8],
                        'Notes': row[9],
                        'Coral Score': row[10]
                    })

        return render_template('recommendation.html', recommended_corals=recommended_corals)
    else:
        return render_template('recommendation_form.html')

@app.route('/coral_info')
def coral_info():
    return render_template('coral_info.html')

def findcoral(filename, coralname):
    results = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if coralname.lower() in row[0].lower() or coralname.lower() in row[1].lower():
                results.append(row)
    return results

@app.route('/find_coral', methods=['POST'])
def find_coral():
    coralname = request.json.get('coralName', '')
    results = findcoral(filename, coralname)
    return jsonify(results)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        userchoice = request.form['userchoice']
        if userchoice == "1":
            return methodsfuncs.recommendspec()
        elif userchoice == "2":
            return methodsfuncs.recommendgenbeginner()
        elif userchoice == "3":
            return methodsfuncs.recommendgenintermediate()
        elif userchoice == "4":
            return methodsfuncs.recommendgenadvanced()
        elif userchoice == "5":
            return methodsfuncs.findcoral()
        elif userchoice == "6":
            return methodsfuncs.addcoral()
        elif userchoice == "7":
            return methodsfuncs.nonphotosynthetics()
        elif userchoice == "8":
            return methodsfuncs.softies()
        elif userchoice == "9":
            return methodsfuncs.lps()
        elif userchoice == "10":
            return methodsfuncs.sps()
        elif userchoice == "11":
            return methodsfuncs.randomcoralgen(filename)
        elif userchoice == "12":
            return "Goodbye!"
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
from flask import Flask, render_template, request, jsonify
import random
import csv
import methodsfuncs

app = Flask(__name__, template_folder='templates')
filename="outputfil.csv"

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommendation_form')
def recommendation_form():
    return render_template('recommendation_form.html')

@app.route('/recommendation', methods=['GET', 'POST'])
def recommendation():
    if request.method == 'POST':
        expscore = int(request.form['expscore'])
        feedscore = int(request.form['feedscore'])
        flow = int(request.form['flow'])
        lightscore = int(request.form['lightscore'])
        typecoral = int(request.form['typecoral'])
        aggressionscore = int(request.form['aggressionscore'])

        userscore = ((expscore * 3) + (lightscore * 3) + (flow * 3) + (typecoral * 2) + feedscore + aggressionscore) / 5

        recommended_corals = []

        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Read the header row
            for row in reader:
                coral_score = float(row[-1])  # Assuming Coral Score is the last column
                if coral_score <= userscore+1:
                    recommended_corals.append({
                        'Name': row[0],  # Assuming Scientific Name is the first column
                        'Common Names': row[1],
                        'Type': row[2],
                        'Light': row[3],
                        'Current': row[4],
                        'Aggression': row[5],
                        'Growth': row[6],
                        'Food': row[7],
                        'Difficulty': row[8],
                        'Notes': row[9],
                        'Coral Score': row[10]
                    })

        return render_template('recommendation.html', recommended_corals=recommended_corals)
    else:
        return render_template('recommendation_form.html')
####
@app.route('/coral_info', methods=['GET'])
def coral_info():
    return render_template('coral_info.html')

def findcoral(filename, coralname):
    results = []
    with open(filename, "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if coralname.lower() in row[0].lower() or coralname.lower() in row[1].lower():
                results.append(row)
    return results

@app.route('/find_coral', methods=['POST'])
def find_coral():
    coralname = request.json.get('coralName', '')
    results = findcoral('outputfil.csv', coralname)
    return jsonify(results)

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for handling the main functionality
@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        userchoice = request.form['userchoice']
        if userchoice == "1":
            return methodsfuncs.recommendspec()
        elif userchoice == "2":
            return methodsfuncs.recommendgenbeginner()
        elif userchoice == "3":
            return methodsfuncs.recommendgenintermediate()
        elif userchoice == "4":
            return methodsfuncs.recommendgenadvanced()
        elif userchoice == "5":
            return methodsfuncs.findcoral()
        elif userchoice == "6":
            return methodsfuncs.addcoral()
        elif userchoice == "7":
            return methodsfuncs.nonphotosynthetics()
        elif userchoice == "8":
            return methodsfuncs.softies()
        elif userchoice == "9":
            return methodsfuncs.lps()
        elif userchoice == "10":
            return methodsfuncs.sps()
        elif userchoice == "11":
            return methodsfuncs.randomcoralgen(filename)
        elif userchoice == "12":
            return "Goodbye!"
    return render_template('main.html')

# Add more routes as needed

if __name__ == '__main__':
    app.run(debug=True)
'''
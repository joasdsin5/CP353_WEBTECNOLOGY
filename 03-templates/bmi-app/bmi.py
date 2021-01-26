from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])     #defaul = GET
def bmi_calc():
    bmi = ''
    recomend = ""
    if request.method == 'POST':
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
        if bmi < 15:
            recomend = "Very severely underweight"
        elif bmi <= 16:
            recomend = "Severely underweight"
        elif bmi <= 18.5:
            recomend = "Underweight"
        elif bmi <= 25:
            recomend = "Normal (healthy weight)"
        elif bmi <= 30:
            recomend = "overweight"
        elif bmi <= 35:
            recomend = "Moderately obese"
        elif bmi <= 40:
            recomend = "Severely obese"
        elif bmi > 40:
            recomend = "overweight"
        else:
            recomend = "Invalid"
    #ทำแน่นอน
    return render_template("bmi.html",
	                        bmi=bmi, recomend=recomend)

def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)
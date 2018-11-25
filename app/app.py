from flask import Flask
from flask import render_template
from flask import request
from sklearn import tree
from sklearn.externals import joblib

app = Flask(__name__, template_folder=".")
classifier = joblib.load('heart-disease-model.joblib')

def diagnose(data):
	for value in data:
		if value == None:
			return None
	result = classifier.predict([data])
	
	if result == 0:
		return "Absense"
	else:
		return "Presence"

@app.route('/')
def index():
	age = request.args.get('age', default=None, type=int)
	gender = request.args.get('gender', default=None, type=int)
	cpt = request.args.get('cpt', default=None, type=int)
	rbp = request.args.get('rbp', default=None, type=int)
	sc = request.args.get('sc', default=None, type=int)
	hfbs = request.args.get('hfbs', default=None, type=int)
	recg = request.args.get('recg', default=None, type=int)
	mhra = request.args.get('mhra', default=None, type=int)
	eia = request.args.get('eia', default=None, type=int)
	std = request.args.get('std', default=None, type=int)
	pests = request.args.get('pests', default=None, type=int)
	nomv = request.args.get('nomv', default=None, type=int)
	thal = request.args.get('thal', default=None, type=int)

	# Column 12 -> nomv dibuang
	# Column 13 -> thal dibuang
	instance = [age, gender, cpt, rbp, sc, hfbs, recg, mhra, eia, std, pests]
	
	return render_template('index.html', 
		age=age, gender=gender, cpt=cpt, rbp=rbp, sc=sc, hfbs=hfbs, 
		recg=recg, mhra=mhra, eia=eia, std=std, pests=pests, nomv=nomv, thal=thal, diagnose=diagnose(instance))

if __name__ == "__main__":
    app.run(debug=True)
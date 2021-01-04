from flask import Flask, request
from flask_cors import CORS, cross_origin
import config as config
from datetime import datetime
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

print("--Running API--")
@app.route('/auth', methods = ['POST'])
def authentication():
	payload = request.json
	username = payload['username']
	basedir = './storage/users/'+username
	if not os.path.exists('./storage/users/'+username):
		os.makedirs('./storage/users/'+username)
		UserData = pd.DataFrame()
		QuestionBank = pd.read_csv('./storage/Question Data.csv')
		UserData['ID'] = QuestionBank['ID'].to_list()
		UserData['Status'] = ['Not Attempted']*len(QuestionBank)
		UserData['Result'] = ['']*len(QuestionBank)
		UserData['Your Time'] = ['']*len(QuestionBank)
		UserData.to_csv(basedir+'/User Data.csv', index=False)
	else:
		UserData = pd.read_csv(basedir+'/User Data.csv')

	response = {
		'Attempted' : len(UserData[UserData['Status'] == 'Attempted']),
		'Not Attempted' : len(UserData[UserData['Status'] != 'Attempted']),
		'Correct' : len(UserData[UserData['Result'] == 'Correct']),
		'InCorrect' : len(UserData[UserData['Result'] == 'InCorrect'])
	}

	return response

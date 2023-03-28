import os
import logging

from datetime import datetime
from typing import Any, Dict

from werkzeug.datastructures import ImmutableMultiDict

from flask import Flask, abort, redirect, request, send_file
from flask_cors import CORS
#from flask_socketio import SocketIO

from dotenv import load_dotenv
from pymongo import MongoClient

from .questions import questions, freelance
#from .session import session
from .excel import write_to_excel

from bson.json_util import loads, dumps

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

app = Flask('Questionnaire API', )
cors = CORS(app)
app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app, cors_allowed_origins='*')

GLOBAL = {}

load_dotenv()

mongo = MongoClient(os.environ['ME_CONFIG_MONGODB_URL'])
database = mongo[os.environ['MONGO_DB_NAME']]
#sessions = {}

@app.after_request
def add_cors_headers(response):
    #r = request.referrer[:-1]
    #if r in white:
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Headers', 'Cache-Control')
    response.headers.add('Access-Control-Allow-Headers', 'X-Requested-With')
    response.headers.add('Access-Control-Allow-Headers', 'Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, DELETE')
    return response
"""
@app.route('/client')
def client_open():
    return init_session('client', questions())

@app.route('/freelance')
def freelance_open():
    return init_session('freelance', freelance(questions()))
"""
@app.route('/client_data/<contract_id>')
def get_client_data(contract_id):
    print(contract_id)
    #get template questions data for client
    return questions()

@app.route('/freelancer_data/<contract_id>')
def get_freelance_data(contract_id):
    print(contract_id)
    #get template questions data for freelancer
    return freelance(questions())

@app.route('/legal_expert_template_data/<contract_id>')
def get_legal_expert_template_data(contract_id):
    print(contract_id)
    #get template questions data for legal expert
    return questions()
    
@app.route('/legal_expert_data/<contract_id>')
def get_legal_expert_data(contract_id):
    print(contract_id)
    #answers = get_contract_from_mongo('legal_expert', contract_id)
    #get stored mongodb data from freelancer and client based on contract_id
    answers = get_contract_from_mongo(contract_id)
    if not answers:
        return questions()
    else: 
        print(answers)
        return answers

@app.post("/submit")
def submit():
    print('submit (contract route) called')
    #return store_contract_to_mongo(flat_map(request.form), collection='answer')
    return store_contract_to_mongo(request.get_json(), collection='answer')
    #return store_contract_to_mongo(request.args, collection='answer')
    #return store_contract_to_mongo(request.data, collection='answer')

@app.post("/save_additional_question")
def save_additional_question():
    print('save_additional_question called')
    return store_additional_questions_to_mongo(request.get_json(), collection='questions')

@app.route('/check_for_additional_question_answers/<contract_id>')
def get_check_for_additional_question_answers(contract_id):
    print(contract_id)
    print('check_for_additional_question_answers')
    questions = get_additional_questions_from_mongo(contract_id, 'answer')
    print(questions)
    return questions

@app.route('/check_for_additional_questions/<contract_id>')
def get_check_for_additional_questions(contract_id):
    print(contract_id)
    print('check_for_additional_questions')
    questions = get_additional_questions_from_mongo(contract_id, 'query')
    print(questions)
    return questions
    

"""
def init_session(category, questions):
    obj = session(category, questions)
    sessions[obj['id']] = obj
    return obj

@socketio.on('session')
def handle_session(data):
    if 'id' in data:
        print("Received session update for " + data['id'])
        if data['id'] in sessions:
            print("Found the session in the local cache")
        else:
            print("Could not find the session in the local cache")

@socketio.on('update')
def handle_update(data):
    print(data)
    socketio.emit('update', data)
    if 'sessionId' in data and data['sessionId'] in sessions:
        sessions[data['sessionId']][data['field']] = data['value']
        print(sessions[data['sessionId']])
"""
@app.route("/results")
def get_results():
    answers = list(database['answer'].find())
    survey = list(database['survey'].find())
    file_name = write_to_excel(answers=answers, survey=survey)
    return send_file(file_name)

def flat_map(form_data: ImmutableMultiDict) -> Dict[str, Any]:
    """ Turns a MultiDict into a regular dict with lists for duplicate keys """
    return { row[0]: row[1][0] if len(row[1]) == 1 else row[1] for row in form_data.lists() }

def store_contract_to_mongo(answers: Dict[str, Any], collection: str):
    log.info(f'Submitting {answers} to Mongo {collection}')
    answers['time'] = str(datetime.now().replace(microsecond=0))
    database[collection].insert_one(answers)
    return "contract saved"

def store_additional_questions_to_mongo(questions: Dict[str, Any], collection: str):
    log.info(f'Submitting {questions} to Mongo {collection}')
    questions['time'] = str(datetime.now().replace(microsecond=0))
    database[collection].insert_one(questions)
    return "additional question saved"

#def get_contract_from_mongo(contractID: str, type: str):
def get_contract_from_mongo(contractID: str):
    #log.info(f'Getting {contractID} of type {type} from Mongo')
    log.info(f'Getting data about contract with {contractID} from Mongo')
    print(f'Getting data about contract with {contractID} from Mongo')
    #filter = {"_id": 1}
    #if (type): 
    #   return list(database['answer'].find({"type": type, "contractID": contractID}, filter))
    #else:
    #return list(database['answer'].find({"contractID": contractID}, filter))
    #cursor_list = list(database['answer'].find_one({"contractID": contractID}))
    cursor_list = database['answer'].find({"contractID": contractID})
    print(cursor_list)
    json = dumps(cursor_list, indent = 2)
    print(json)
    return json

def get_additional_questions_from_mongo(contractID: str, type: str):
    log.info(f'Getting additional questiosn for contract with ID {contractID} from Mongo')
    print(f'Getting additional questiosn for contract with ID {contractID} from Mongo')
    cursor_list = database['questions'].find({"contractID": contractID, "type": type})
    print(cursor_list)
    json = dumps(cursor_list, indent = 2)
    print(json)
    return json

def run():
    app.run("0.0.0.0", 8082)
#    socketio.run(app, host='0.0.0.0', port=8082, allow_unsafe_werkzeug=True)

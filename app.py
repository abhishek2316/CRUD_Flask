from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

Client = MongoClient('mongodb://localhost:27017/')
db = Client['crudFlask']
collection = db['test']

def format_employee(employee):
    employee['_id'] = str(employee['_id'])
    return employee

@app.route('/')
@app.route('/form')
def fill_form():
    return render_template('form/index.html')

#GET Method

@app.route('/api/employee', methods = ['GET'])
def get_employees():
    empid = request.args.get('empid')
    if empid:
        employee = collection.find_one({'empid' : int(empid)})
        if employee:
            return jsonify(format_employee(employee)), 200
        else:
            return jsonify({'error' : "No employee found"})
    else:
        employees = list(collection.find())
        return jsonify([format_employee(emp) for emp in employees]), 200
    
#POST Method
    
@app.route('/api/employee', methods = ['POST'])
def add_employees():
    data = request.json
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)
    return jsonify({'message' : 'Employee details are inserted'})

#PUT Method

@app.route('/api/employee', methods = ['PUT'])
def update_employees():
    empid = request.args.get('empid')
    data = request.json

    if empid:
        result = collection.update_one({'empid' : int(empid)}, { '$set' : data})
        if result.matched_count:
            return jsonify({'message' : 'Employee details updated'}), 200
        return jsonify({'error' : 'Employee not found'}),400
    return jsonify({'error': 'Provide an employee ID to update details'}),400


#Delete Method

@app.route('/api/employee', methods = ["DELETE"])
def delete_employees():
    empid = request.args.get('empid')
    if empid:
        result = collection.delete_one({'empid' :  int(empid)})
        if result.deleted_count:
            return jsonify({'message' : 'Employee deleted'}), 200
        return jsonify({'error' : 'Employee not found'}), 404
    return jsonify({'error' : 'Provide an employee detail'}), 404

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask,jsonify,request,session
from models import db, Student

app = Flask(__name__)

#    DATABASE  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# <            ___   __  __ ___            /\    __         >
# <           |___| |_  |__  |  _ _ _ _   /--\  |__| |      > 
# <           |  \  |__  __| |           /    \ |    |      >

# we have to make file to json format -- JSONify. in django we can use serialzer to send json  front end

# < ---  GET API REQUEST --->

@app.route('/students', methods = ['GET'])

def get_students():

    students = Student.query.all()

    # return jsonify([x.to_dict() for x in students]) 

    data = []

    for student in students:
        data.append({
            "id":student.id,
            "name":student.name,
            "roll_no":student.roll_no,
            "class_no":student.class_no,
            "address":student.address
        })

    
    return jsonify({
        'message':'Successfully fetched data',
        "data":data
    })



# <------------  POST API REQUEST ---------->

@app.route('/add_students', methods= ['POST'])
def create_students():

# this is request for data
    data = request.get_json()

    student = Student(
        id = data['id'],
        name = data['name'],
        roll_no = data['roll_no'],
        class_no = data['class_no'],
        address = data['address']
    )

    db.session.add(student)
    db.session.commit()

    return jsonify({
        'message':'The students details has created',
        "student":{
            "id":student.id,
            "name":student.name,
            "roll_no":student.roll_no,
            "class_no":student.class_no,
            "address":student.address
        }
    })

#<--------   DELETE STUDENT    ------>


@app.route('/remove_sy=tudent', methods = ['DELETE'])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({'message': f'The student id {id} doesnot exist'})

    
    db.session.delete(student)
    db.session.commit()

    return jsonify({'message':f'The student id {id} has succesfullly deleted'})


#< ---------------   UPDATE DATA   --------------->

@app.route('/update_student/<int:id>', methods=['PUT'])
def alter_data(id):

    student = Student.query.get(id)
    if not student:
        return jsonify({'message':f'The student id {id} doesnot exist'})

    data = request.get_json()

   
    student.name = data['name'],
    student.roll_no = data['roll_no'],
    student.class_no = data['class_no'],
    student.address = data['address']

    
    db.session.commit()
    return jsonify({
        'message':f'Successfully updated',
    })



# students = [
#     {
#         "id":2,
#         "name":Sreehari,
#         "roll_no":97,
#         "class_no":2,
#         "address":Mezhathur
#     },
#     {
#             "id":3,
#             "name":Niranjan,
#             "roll_no":64,
#             "class_no":2,
#             "address":Amala
#         }
# ]





if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
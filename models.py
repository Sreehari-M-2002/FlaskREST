from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):

    name = db.Column(db.String(20), nullable=False)
    roll_no = db.Column(db.Integer, nullable= False)
    class_no =db.Column(db.Integer, nullable=False)
    address=db.Column(db.String(50),nullable=False)
    id=db.Column(db.Integer, primary_key=True)

#< ---- Easy way ---->
    # def to_dict(self):
    #     return {
    #         "id":self.id,
    #         "name":student.name,
    #         "roll_no":self.roll_no,
    #         "class_no":self.class_no,
    #         "address":self.address
    #     }
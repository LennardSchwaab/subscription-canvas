from project import db
from project.models import Test1, User
from project.quick_check.forms import CheckForm

checkform = CheckForm

def read_user(user_id=None):
     if user_id is None:
         users = User.query.all()
     else:
         users = User.query.filter_by(id=user_id).all()
     return(users)

def test1():
    output = Test1.query.all()
    return(output)

def test1_add(value1, value2):
    db_wert = Test1(test1=checkform.frage1.data,
                    test2=checkform.frage2.data)
    db.session.add(db_wert)
    db.session.commit()

#test1_add(1,2)
print(test1())

def test1_add2(value1, value2):
    for items in Test1.query.all():
        delete_item = Test1.query.get(items.report_test1_id())
        db.session.delete(delete_item)
        db.session.commit()
    test1 = value1
    test2 = value2
    db_wert = Test1(test1,
                    test2)
    db.session.add(db_wert)
    db.session.commit()

test1_add2(1,1)

print(test1())

from flask import*
from database import*
from public import*
from admin import*
from hospital import*
from doctor import*
from user import*





app=Flask(__name__)
app.secret_key='sdfghj'
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(hospital)
app.register_blueprint(doctor)
app.register_blueprint(user)






app.run(debug=True,port=5007)
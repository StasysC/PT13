from app import db, Message

all_message = Message.query.all()
print(all_message)

message_petras = Message.query.get(2)
message_petras.email = 'ksakdsakdasdk@gmail.com'
db.session.add(message_petras)
db.session.commit()


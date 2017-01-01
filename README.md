# protospacedoor

raspberry pi based access control for futurespace(formerly protospace)

```
sudo pip3 install < requirements.txt
```

add this to .bashrc

```
sandman2ctl sqlite+pysqlite:///futurespace.db &

python3 door.py
```

access admin via localhost:5000/admin


Notes about how stuff works:
```
db = dataset.connect('sqlite:///futurespace.db')

db.query('DROP TABLE "users";')

db.query("""CREATE TABLE "users" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "keyfob" TEXT NOT NULL,
    "enabled" TEXT NOT NULL
)""")

# create users
u = db['users']

t1 = {'name':'eli', 'keyfob':'12345', 'enabled':'TRUE'}
t2 = {'name':'john', 'keyfob':'23456', 'enabled':'FALSE'}

u.insert(t1)
u.insert(t2)

# create an entry into the building
entries = db['log']
utc = arrow=utcnow()
local = utc.to('US/Central')

temp = {'time':local.timestamp(), 'user':user}

entries.insert(temp)

# listing users 
all_users = db['users'].all()
all_entries = db['log'].all()
```

# TODO:
* add offsite logging via firebase
* allow remote entry via firebase
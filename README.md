# protospacedoor

use gui to admin 
```#sandman2ctl sqlite+pysqlite:///futurespace.db```
access it via localhost:5000/admin

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

temp = {'time':local.humanize(), 'user':user}

entries.insert(temp)

# listing users 
all_users = db['users'].all()
all_entries = db['log'].all()
```
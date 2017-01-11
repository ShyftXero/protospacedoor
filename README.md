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

Use an NFC tag reading app to get the serial number in aa:bb:cc:dd:ee:ff format

always read the last 4 bytes in reverse order.

tag id 04:4d:cd:92:6d:40:80
```
python3 -c "s = '04:4d:cd:92:6d:40:80'.split(':')[0:4];print(int('0x'+''.join(s[::-1]), 16))"
```

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

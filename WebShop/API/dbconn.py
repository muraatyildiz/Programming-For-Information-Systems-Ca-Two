from sshtunnel import SSHTunnelForwarder
import mysql.connector
try:
    server = SSHTunnelForwarder(('20.218.157.149',22),
                                ssh_username='murat',
                                ssh_password="M2001695720016957.z",
                                ssh_proxy_enabled= True,
                                remote_bind_address=('127.0.0.1', 3306)
                                )
    server.start()
    print("Server started")
    mysql = mysql.connector.connect(user='web', password='webPass',
                                    host='127.0.0.1',
                                    database='student',
                                    port=server.local_bind_port,
                                    
                                    )
    if mysql!=None:
        print("connect",mysql)
    else:
        print("error", mysql)          
except BaseException as e:
    print('Problem with', e)
finally:
    if server:
        server.close   
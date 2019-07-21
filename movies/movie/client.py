import connection
client = connection.Connection('root', 'root', 'localhost', 6542)
# print(client.create_database('zzz'))
# print(client.create_user('ali', 'ali'))
print(client.get_databases())
# client.use_database('hamed_keyspace')
# client.delete_database('hamed_keyspace')
client.delete_database('zzz')

# client.create_table('info', {'id': 'int', 'info': 'map<text, text>'}, ['id'])

# table = client.table('info')

# table.delete()

# table.put_item({'id': 1, 'info': {'fist_name': 'ali', 'last_name': 'safari'}})
# table.put_item({'id': 1, 'name': 'uuu'})

# table.update_item({'name': 'qqq'}, {'id': 4})

# table.delete_item({'id': 6})

# table.get_item()

# tables = client.get_tables()
# for table in tables:
#     print(table.name)

client.close_connection()

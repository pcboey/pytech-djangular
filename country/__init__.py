# sqlite3 foreign key support is not on by default
# this sets it on if sqllite3 is used
from django.db.backends.signals import connection_created

def activate_foreign_keys(sender, connection, **kwargs):
    """Enable integrity constraint with sqlite."""
    if connection.vendor == 'sqlite':
        cursor = connection.cursor()
        cursor.execute('PRAGMA foreign_keys = ON;')

connection_created.connect(activate_foreign_keys)
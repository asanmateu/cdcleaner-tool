from constants import getpass

# Set up tunnel connection to prod with querying functions...
CONNECTION_SETTINGS = {
    'read_only_prod': {
        'ssh_host': 'bastion.jooraccess.com',
        'ssh_port': 22,
        'remote_ip': 'localhost',
        'remote_port': 7432,
        'db_default': 'prodrds'},
    'reporting': {
        'ssh_host': 'www-reporting.joordev.com',
        'ssh_port': 227,
        'remote_ip': 'localhost',
        'remote_port': 5432,
        'db_default': 'joor_dev'},
    'user': {
        'name': getpass.getuser(),
        'ssh_username': None,
        'ssh_password': None,
        'db_username': None,
        'db_password': None,
        'credentials_set': False}
}

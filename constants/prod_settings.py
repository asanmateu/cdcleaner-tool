from library import getpass


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
        'ssh_username': '',
        'ssh_password': '',
        'db_username': '',
        'db_password': '',
        'credentials_set': False}
}
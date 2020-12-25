from library import getpass, os


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
        'ssh_username': os.environ.get('SSH_USERNAME'),
        'ssh_password': os.environ.get('SSH_PASSWORD'),
        'db_username': os.environ.get('PROD_USERNAME'),
        'db_password': os.environ.get('PROD_PASSWORD'),
        'credentials_set': False}
}

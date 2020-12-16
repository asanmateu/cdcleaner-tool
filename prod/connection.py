import pandas as pd
import getpass
from sqlalchemy import create_engine, exc
from sshtunnel import SSHTunnelForwarder, BaseSSHTunnelForwarderError

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
        'ssh_username': 'asanmateu',
        'ssh_password': '',
        'db_username': 'human_ro_asanmateu',
        'db_password': 'wyUhzpUw3ZCyoEkDEdtv',
        'credentials_set': False}
}


def get_credentials():
    if CONNECTION_SETTINGS['user']['ssh_username'] is None:
        CONNECTION_SETTINGS['user']['ssh_username'] = input('SSH Username: ')

    if CONNECTION_SETTINGS['user']['ssh_password'] is None:
        CONNECTION_SETTINGS['user']['ssh_password'] = getpass.getpass(prompt='SSH Password: ')

    if CONNECTION_SETTINGS['user']['db_username'] is None:
        CONNECTION_SETTINGS['user']['db_username'] = input('DB Username: ')

    if CONNECTION_SETTINGS['user']['db_password'] is None:
        CONNECTION_SETTINGS['user']['db_password'] = getpass.getpass(prompt='DB Password: ')

    CONNECTION_SETTINGS['user']['credentials_set'] = True


def clear_credentials():
    CONNECTION_SETTINGS['user']['ssh_username'] = None
    CONNECTION_SETTINGS['user']['ssh_password'] = None
    CONNECTION_SETTINGS['user']['db_username'] = None
    CONNECTION_SETTINGS['user']['db_password'] = None
    CONNECTION_SETTINGS['user']['credentials_set'] = False


def query_read_only_prod(query_string):
    if not CONNECTION_SETTINGS['user']['credentials_set']:
        get_credentials()
    ssh_username = CONNECTION_SETTINGS['user']['ssh_username']
    ssh_password = CONNECTION_SETTINGS['user']['ssh_password']
    db_username = CONNECTION_SETTINGS['user']['db_username']
    db_password = CONNECTION_SETTINGS['user']['db_password']
    name = CONNECTION_SETTINGS['user']['name']
    settings = CONNECTION_SETTINGS['read_only_prod']
    remote_ip = settings['remote_ip']
    remote_port = settings['remote_port']
    db_default = settings['db_default']
    ssh_host = settings['ssh_host']
    ssh_port = settings['ssh_port']
    ssh_pkey_path = '/Users/' + name + '/.ssh/id_rsa'
    try:
        with SSHTunnelForwarder(
                ssh_address_or_host=(ssh_host, ssh_port),
                ssh_username=ssh_username,
                ssh_pkey=ssh_pkey_path,
                remote_bind_address=(remote_ip, remote_port),
                ssh_password=ssh_password
        ) as server:
            server.start()
            local_port = str(server.local_bind_port)
            address = 'postgresql://{db_username}:{db_password}@{remote_ip}:{local_port}/{db_default}'
            engine_address = address.format(db_username=db_username,
                                            db_password=db_password,
                                            remote_ip=remote_ip,
                                            local_port=local_port,
                                            db_default=db_default)
            engine = create_engine(engine_address)
            connection = engine.connect()
            query_df = pd.read_sql_query(query_string, con=engine)
            connection.close()
            engine.dispose()
            return query_df
    except ValueError as e:
        print('ValueError', e, 'check your key path')
        clear_credentials()
    except BaseSSHTunnelForwarderError as e:
        print('BaseSSHTunnelForwarderError:', e, '\nCheck that you entered the correct credentials from 1Password')
        clear_credentials()
    except exc.SQLAlchemyError as e:
        print('SQLAlchemyError:', e)
        clear_credentials()
import os

from hvac import Client
from hvac.exceptions import Unauthorized
from app.logger import logger

credentials = {}


def get_credentials(path, env=None):
    if not credentials.get(path):
        if not env:
            env = os.getenv('ENV')
        token = os.getenv('VAULT_TOKEN')

        error = []
        if not env: error.append('ENV')
        if not token: error.append('VAULT_TOKEN')

        if error:
            logger.error(message='environment variables not declared', data=error, status_code=500)
            raise EnvironmentError('environment variablesnot declared')

        logger.info(message=f'Consultando path "{path}" no Vault. Ambiente "{env}"')
        vault_host = os.getenv('VAULT_HOST')
        client = Client(vault_host, token)

        if not client.is_authenticated():
            logger.error(message='Não autenticado no Vault', status_code=401)
            raise Unauthorized('Não autenticado no Vault')

        key_dict = client.secrets.kv.v2.read_secret(mount_point=env, path=path, )['data']['data']
        credentials.update({path: key_dict})

    return credentials.get(path)

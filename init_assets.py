import random
import logging

import bigchaindb
import bigchaindb.config_utils

import apps_config
from server.lib.models.accounts import retrieve_accounts
from server.lib.models.assets import create_asset
from server.config_bigchaindb import get_bigchain

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APPS = apps_config.APPS


def get_accounts_by_name(accounts):
    # returns a dict with key = 'name-<ledger_id>' value = account
    return {'{}-{}'.format(account['name'], account['ledger']['id']): account for account in accounts}


def main():
    for app in APPS:
        app_name = '{}'.format(app['name'])
        if 'num_accounts' in app:
            ledger_name = 'bigchaindb_examples_{}'.format(app['ledger'])
            bigchain = get_bigchain(ledger_id=app['ledger'])
            accounts = retrieve_accounts(bigchain, app_name)
            assets = []
            for i in range(app['num_assets']):
                asset = create_asset(bigchain=bigchain,
                                     to=accounts[random.randint(0, app['num_accounts'] - 1)]['vk'],
                                     payload=app['payload_func'](i))
                assets.append(asset)
            logging.info('{} assets initialized for app {} on ledger {}'.format(len(assets),
                                                                                app_name,
                                                                                ledger_name))
        elif app_name == 'different_users':
            bigchain = bigchaindb.Bigchain()
            accounts_by_name = get_accounts_by_name(retrieve_accounts(bigchain, app['name']))
            admin_account = app['accounts'][0]
            [user_assets, account_assets] = admin_account['ledgers']
            bigchain = bigchaindb.Bigchain(dbname='bigchaindb_examples_0')
            assets = []

            for user_asset_ind in range(user_assets['num_assets']):
                payload = {
                    'app': 'different_users',
                    'content':
                        {
                            'asset_name': 'user{}'.format(user_asset_ind),
                        },
                }
                user_asset = create_asset(bigchain=bigchain,
                                          to=accounts_by_name['admin-0']['vk'],
                                          payload=payload)
                assets.append(user_asset)

            user_0_asset_id = assets[0]['id']
            user_1_asset_id = assets[1]['id']

            for account_asset_ind in range(account_assets['num_assets']):
                account = app['accounts'][account_asset_ind + 1]
                ledger = account['ledgers'][0]
                account_name = '{}-{}'.format(account['name'], ledger['id'])
                authorized = {}
                if account_asset_ind < 3:
                    authorized[str(len(authorized))] = user_0_asset_id
                if account_asset_ind > 1:
                    authorized[str(len(authorized))] = user_1_asset_id
                payload = {
                    'app': 'different_users',
                    'content':
                        {
                            'asset_name': accounts_by_name[account_name]['vk'],
                            'authorized': authorized,
                        },
                }
                account_asset = create_asset(bigchain=bigchain,
                                            to=accounts_by_name['admin-0']['vk'],
                                            payload=payload)
                assets.append(account_asset)

            account_ind = 0
            for account in app['accounts']:
                account_ind += 10
                if account['name'] != 'admin':
                    for ledger in account['ledgers']:
                        ledger_name = 'bigchaindb_examples_{}'.format(ledger['id'])
                        account_name = '{}-{}'.format(account['name'], ledger['id'])
                        bigchain = bigchaindb.Bigchain(dbname=ledger_name)
                        for i in range(ledger['num_assets']):
                            asset = create_asset(bigchain=bigchain,
                                                 to=accounts_by_name[account_name]['vk'],
                                                 payload=app['payload_func'](i + account_ind))
                            assets.append(asset)

            logging.info('{} assets initialized in app {}'.format(len(assets), app_name))
        elif 'accounts' in app:
            bigchain = bigchaindb.Bigchain()
            accounts_by_name = get_accounts_by_name(retrieve_accounts(bigchain, app['name']))
            for account in app['accounts']:
                for ledger in account['ledgers']:
                    ledger_name = 'bigchaindb_examples_{}'.format(ledger['id'])
                    account_name = '{}-{}'.format(account['name'], ledger['id'])
                    bigchain = bigchaindb.Bigchain(dbname=ledger_name)
                    assets = []
                    for i in range(ledger['num_assets']):
                        asset = create_asset(bigchain=bigchain,
                                             to=accounts_by_name[account_name]['vk'],
                                             payload=app['payload_func'](i))
                        assets.append(asset)
                    logging.info('{} assets initialized for account {} in app {} on ledger {}'
                                 .format(len(assets), account['name'], app_name, ledger_name))


if __name__ == '__main__':
    main()

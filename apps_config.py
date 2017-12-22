APPS = [
    {
        'name': 'ontherecord',
        'num_accounts': 3,
        'num_assets': 0,
        'ledger': 0,
        'payload_func': (
            lambda x: {
                'app': 'ontherecord',
                'content': x
            }
        )
    },
    {
        'name': 'sharetrader',
        'num_accounts': 5,
        'num_assets': 64,
        'ledger': 0,
        'payload_func': (
            lambda i: {
                'app': 'sharetrader',
                'content': {
                    'x': int(i / 8),
                    'y': int(i % 8)
                }
            }
        )
    },
    {
        'name': 'interledger',
        'accounts': [
            {
                'name': 'alice',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 3
                    }
                ]
            },
            {
                'name': 'bob',
                'ledgers': [
                    {
                        'id': 1,
                        'num_assets': 3
                    }
                ]
            },
            {
                'name': 'chloe',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 3
                    },
                    {
                        'id': 1,
                        'num_assets': 3
                    }
                ]
            }
        ],
        'payload_func': (
            lambda x: {
                'app': 'interledger',
                'content': x
            }
        )
    },
    {
        'name': 'different_users',
        'accounts': [
            {
                'name': 'admin',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 2
                    },
                    {
                        'id': 0,
                        'num_assets': 4
                    }
                ]
            },
            {
                'name': 'account1',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 1
                    }
                ]
            },
            {
                'name': 'account2',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 2
                    },
                ]
            },
            {
                'name': 'account3',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 3
                    },
                ]
            },
            {
                'name': 'account4',
                'ledgers': [
                    {
                        'id': 0,
                        'num_assets': 4
                    },
                ]
            }
        ],
        'payload_func': (
            lambda x: {
                'app': 'different_users',
                'content': x,
            }
        )
    },
]

__author__ = 'ob3'

class template:

    subscriber_detail = {
        'edo': {
            'url': 'http://localhost/',
            'method': 'post'
        }
    }

    pattern_subscriber = {
        '*POST*': ['edo', 'edi'],
        '*STATUS_CHANGED*': ['sow', 'bb']
    }

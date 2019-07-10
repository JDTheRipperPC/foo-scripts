#!/usr/bin/env python

import shodan
from shodan.cli.helpers import get_api_key

FACETS = [
    ('org', 5),
    ('domain', 5),
    ('port', 5),
    ('asn', 5),
    ('country', 5)
]

FACETS_TITLES = {
    'org': 'Top 5 Organizations',
    'domain': 'Top 5 Domains',
    'port': 'Top 5 Ports',
    'asn': 'Top 5 Autonomous Systems',
    'country': 'Top 5 Countries'
}

def simple_facet():
    try:
        ShodanAPI = shodan.Shodan(get_api_key())
        results = ShodanAPI.count("nginx", facets=FACETS)
        print('Total results: {}\n'.format(results.get('total')))
        for facet in facets:
            print('\n', FACETS_TITLES[facet], '\n')
            for item in facets[facet]:
                print('{value}: {key}'.format(value=item.get('value'), key=item.get('count')))
    except shodan.APIError as err:
        print('Error: {}'.format(err))


if __name__ == '__main__':
    pass

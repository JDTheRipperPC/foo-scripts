#!/usr/bin/env python

import shodan
from shodan.cli.helpers import get_api_key


def simple_search():
    try:
        ShodanAPI = shodan.Shodan(get_api_key())
        results = ShodanAPI.host('188.84.42.162')
        for result in results.get('matches'):
            print(result)
    except shodan.APIError as err:
        print('Error: {}'.format(err))


if __name__ == '__main__':
    simple_search()

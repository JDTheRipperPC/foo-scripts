#!/usr/bin/env python

import shodan
from shodan.cli.helpers import get_api_key


def simple_search():
    try:
        ShodanAPI = shodan.Shodan(get_api_key())
        results = ShodanAPI.ports()
        print('Total ports that Shodan crawls:', len(results))
        for result in results:
            print('Port: ', result)
    except shodan.APIError as err:
        print('Error: {}'.format(err))


if __name__ == '__main__':
    simple_search()

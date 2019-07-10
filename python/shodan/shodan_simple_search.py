#!/usr/bin/env python

import shodan
from shodan.cli.helpers import get_api_key


def simple_search():
    try:
        ShodanAPI = shodan.Shodan(get_api_key())
        results = ShodanAPI.search('apache')
        for result in results.get('matches'):
            print('IP: {ip}\nData: {data}\n'.format(
                ip=result.get('ip_str'),
                data=result.get('data')
            ))
    except shodan.APIError as err:
        print('Error: {}'.format(err))


if __name__ == '__main__':
    simple_search()

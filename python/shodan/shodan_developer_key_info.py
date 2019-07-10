#!/usr/bin/env python

import shodan
from shodan.cli.helpers import get_api_key


def show_info(apikey):
    try:
        ShodanAPI = shodan.Shodan(apikey)
        info = ShodanAPI.info()
        for inf in info:
            print('{key}: {value}'.format(key=inf, value=info[inf]))
    except shodan.APIError as err:
        print('Error: {}'.format(err))


if __name__ == '__main__':
    show_info(get_api_key())

#!/usr/bin/env python3
# coding=utf-8

# This parser returns Kuwait's electricity system load (assumed to be equal to electricity production)
# Source: Ministry of Electricity and Water / State of Kuwait
# URL: https://www.mew.gov.kw/
# Shares of Electricity production in 2016: 64% gas, 36% oil (source: IEA; https://www.iea.org/statistics/?country=KUWAIT&indicator=ElecGenByFuel)


import arrow
import requests

def fetch_production(zone_key='KW', session=None, logger=None):
    r = session or requests.session()
    url = 'https://www.mew.gov.kw/getTempLiveRead.aspx'
    response = r.get(url)
    html = response.text
    total_production = html.split('\r\n', 1)[0]
   
    datapoint = {
      'zoneKey': zone_key,
      'datetime': arrow.now('Asia/Kuwait').datetime,
      'unknown': total_production,
      'source': 'mew.gov.kw'
    }

    return datapoint

if __name__ == '__main__':
    """Main method, never used by the Electricity Map backend, but handy for testing."""
    
    print('fetch_production() ->')
    print(fetch_production())

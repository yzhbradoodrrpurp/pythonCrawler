# -*- coding = utf-8 -*-
# @Time: 2024/10/5 13:12
# @Author: Zhihang Yi
# @File: 008flightradar.py
# @Software: PyCharm

import urllib.request
import json
import sqlite3
import random


def main():
    url1 = 'https://www.flightradar24.com/flights/most-tracked'

    content_id = get_id(url1)

    if content_id is not None:
        IDs = parse_id(content_id)
    else:
        print("You failed to obtain the flight IDs.")
        return

    basic_url = ' https://data-live.flightradar24.com/clickhandler/?version=1.5&flight='
    flight_list = []

    for ID in IDs:
        url = basic_url + str(ID)
        content_flight = get_info(url, ID)
        flight_info = parse_info(content_flight)

        if flight_info is not None:
            flight_list.append(flight_info)

        print()

    store_data(flight_list)

def get_id(url):
    headers = {
        'Cookie':
            'mac_overlay_count=190; _dd_s=rum=0&expire=1728117579627; OptanonConsent=isGpcEnabled=0'
            '&datestamp=Sat+Oct+05+2024+16%3A23%3A39+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%'
            '86%E6%97%B6%E9%97%B4)&version=202409.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&con'
            'sentId=18a3fbdd-e489-4130-a63f-2e54e5cfc53b&interactionCount=1&isAnonUser=1&landingPat'
            'h=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intT'
            'ype=1&geolocation=US%3BCA&AwaitingReconsent=false; _ga=GA1.1.1004982678.1726987624; _g'
            'a_38V2BZ2HMF=GS1.1.1728116619.14.1.1728116619.60.0.0; mp_942a098c72ecbdd6c0d9c00fe8308'
            '319_mixpanel=%7B%22distinct_id%22%3A%20%22%24device%3A192187bde801a8b-0c52fc87e76446-3'
            'e62654b-1ce26a-192187bde801a8b%22%2C%22%24device_id%22%3A%20%22192187bde801a8b-0c52fc87'
            'e76446-3e62654b-1ce26a-192187bde801a8b%22%2C%22%24initial_referrer%22%3A%20%22%24direct'
            '%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%'
            '2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_re'
            'ferring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%'
            '20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%'
            '5D%7D; subFeature=Timeout%20overlay%20upgrade%20CTA; _frpk=_v64R3PHIMSr4ef3W4mvNw; _l'
            'r_env_src_ats=false; _pbjs_userid_consent_data=3524755945110770; csuuidSekindo=66fe2b7'
            '78bf39; _cc_id=16e4c66af0153c7eaa43c2aaad6aff6a; pbjs-unifiedid=%7B%22TDID%22%3A%2286c'
            '12190-139e-4975-8354-226140df85db%22%2C%22TDID_LOOKUP%22%3A%22FALSE%22%2C%22TDID_CREA'
            'TED_AT%22%3A%222024-10-03T05%3A28%3A30%22%7D; pbjs-unifiedid_last=Thu%2C%2003%20Oct%2'
            '02024%2005%3A28%3A30%20GMT; cw-test-20240912-prebid-ts-test-25-75=control; cw-test-sta'
            'nd-alone-floors-facade-hardFloor-0-95-0-5=fallb; cw-test-stand-alone-floors-facade-mul'
            'tiplier-80-20-0-0=multa; 33acrossIdTp=L%2BylhEpDeV7tbT7tGCUFfN5PGnxz3vOMuAhgPzBrmDQ%3D;'
            ' OptanonAlertBoxClosed=2024-09-22T06:47:31.570Z; cw-test-stand-alone-floors-comparison'
            '-multiplier-0-100=control; cw-test-20240912-prebid-ts-test-10-90=control; cw-test-stan'
            'd-alone-floors-facade-hardFloor-0-40-40-20=fallc; cw-test-stand-alone-floors-facade-m'
            'ultiplier-20-40-40-0=multb',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15'
    }

    req = urllib.request.Request(url=url, headers=headers)

    # proxies = proxy_pool()

    # handler = urllib.request.ProxyHandler(proxies=proxies)
    # opener = urllib.request.build_opener(handler)

    try:
        # response = opener.open(req, timeout=4)
        response = urllib.request.urlopen(req, timeout=4)
    except Exception as e:
        print("There's an error occurred.")
        print(e)

        return None
    else:
        print("You've successfully got the IDs of several flights.\n")

        return response.read().decode('utf-8')


def parse_id(content_id):
    content = json.loads(content_id)

    flights = content['data']
    IDs = []

    for flight in flights:
        IDs.append(flight['flight_id'])

    return IDs


def get_info(url, ID):
    headers = {
        'Cookie':
            'mac_overlay_count=109; _frpk=_v64R3PHIMSr4ef3W4mvNw; '
            'OptanonConsent=isGpcEnabled=0&datestamp=Sat+Oct+05+2024+12%3A48%3A32+GMT%2B0800+'
            '(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202409.1.0&'
            'browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=18a3fbdd-e489-4130-a63f-2e54e5cfc53b&'
            'interactionCount=1&isAnonUser=1&landingPath=NotLandingPage&'
            'groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&intType=1&'
            'geolocation=US%3BCA&AwaitingReconsent=false; _ga=GA1.1.1004982678.1726987624; '
            '_ga_38V2BZ2HMF=GS1.1.1728103454.10.1.1728103712.60.0.0; '
            'mp_942a098c72ecbdd6c0d9c00fe8308319_mixpanel=%7B%22distinct_'
            'id%22%3A%20%22%24device%3A192187bde801a8b-0c52fc87e76446-3e62654b-1ce26a-19'
            '2187bde801a8b%22%2C%22%24device_id%22%3A%20%22192187bde801a8b-0c52fc87e76446-3e'
            '62654b-1ce26a-192187bde801a8b%22%2C%22%24initial_referrer%22%3A%20%22%24direct'
            '%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%'
            '20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%2'
            '2%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3'
            'A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3'
            'A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D; _cc_id=16e4c66af0153c7eaa43c2aaad6aff6a; '
            '33acrossIdTp=L%2BylhEpDeV7tbT7tGCUFfN5PGnxz3vOMuAhgPzBrmDQ%3D; '
            'OptanonAlertBoxClosed=2024-09-22T06:47:31.570Z',
        'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
            'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Safari/605.1.15'
    }

    req = urllib.request.Request(url=url, headers=headers)

    # proxy = proxy_pool()

    # handler = urllib.request.ProxyHandler(proxy)
    # opener = urllib.request.build_opener(handler)

    try:
        # response = opener.open(req, timeout=4)
        response = urllib.request.urlopen(req)
    except Exception as e:
        print("There's an error occurred.")
        print(e)
        return None
    else:
        print(f"You've successfully got the flight information of '{ID}'.")
        return response.read().decode('utf-8')


def parse_info(content):
    try:
        content = json.loads(content)
    except Exception as e:
        print("The API didn't return a JSON file.")
        print(e)

        return None
    else:
        ID = content['identification']['id']

        callsign = content['identification']['callsign']
        if callsign is None:
            callsign = ' '
        if callsign == 'Blocked':
            print(f"The information of {content['identification']['id']} is blocked.")
            return None

        try:
            icao = content['airline']['code']['icao']
        except Exception as e:
            icao = ' '
            print(f"For {content['identification']['id']}, the ICAO is unknown.")

        try:
            origin = content['airport']['origin']['name']
        except Exception as e:
            origin = ' '
            print(f"For {content['identification']['id']}, the origin is unknown.")

        try:
            destination = content['airport']['destination']['name']
        except Exception as e:
            destination = ' '
            print(f"For {content['identification']['id']}, the destination is unknown.")

        trail = content['trail']

        return [ID, callsign, icao, origin, destination, trail]


def store_data(flight_list):
    conn = sqlite3.connect('/Users/yzhbradoodrrpurp/Desktop/flights.db')
    c = conn.cursor()

    sql = '''
    create table if not exists flights(
    ID text primary key,
    Callsign text not null,
    ICAO text not null,
    Origin text not null,
    Destination text not null
    );'''

    c.execute(sql)

    for flight in flight_list:
        # or ignore的作用是，如果primary key有重复，就会跳过这个数据的插入。
        sql = '''
        insert or ignore into flights(ID, Callsign, ICAO, Origin, Destination)
        values(?, ?, ?, ?, ?);
        '''

        c.execute(sql, (flight[0], flight[1], flight[2], flight[3], flight[4]))

    conn.commit()
    conn.close()

    print("The information is successfully stored in database.")


def proxy_pool():
    proxy_pool = [
        {'http': '52.91.132.109', 'https': '52.91.132.109'},
    ]

    num = random.randint(0, len(proxy_pool) - 1)

    return proxy_pool[num]


if __name__ == '__main__':
    main()

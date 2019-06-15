import os
import requests


def output_the_number_of_clicks_on_the_link(token, link_address):
    link_address = link_address.split('//')
    headers = {}
    headers["Authorization"] = "Bearer %s" % (token)
    url = 'https://api-ssl.bitly.com/v4/bitlinks/%s/clicks/summary' % (
        link_address[1])
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def creating_a_shortened_link(token, link_address):
    checking_the_link = requests.get(link_address)
    payload = {}
    payload["long_url"] = link_address
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {}
    headers["Authorization"] = "Bearer %s" % (token)
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    short__link = response.json()
    return short__link['link']


def checking_the_link(link_address):
    return link_address.startswith(
        'http://bit.ly/') or link_address.startswith('https://bit.ly/')


def main():
    token = os.getenv("TOKEN")
    link_address = input("Введите вашу ссылку ")
    check = checking_the_link(link_address)
    if check:
        amount_of_link_clicks = output_the_number_of_clicks_on_the_link(
            token, link_address)
        print(amount_of_link_clicks)
    else:
        short_link = creating_a_shortened_link(token, link_address)
        print(short_link)


if __name__ == '__main__':
    main()

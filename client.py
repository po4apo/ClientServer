# -*- coding: utf-8 -*-
import requests

def get(request):
    response = requests.get(
        f'http://127.0.0.1:40000/{request}',
        headers={'Accept': 'application/vnd.github.v3.text-match+json'})

    return (response.text)


if __name__ == '__main__':
    while True:
        print('\nДля выхода введите: exit')
        request = input('Введите ваше выражение:')
        if request == 'exit':
            break

        print(get(request))
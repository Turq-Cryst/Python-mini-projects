# requires pip installation of "requests" package

import requests
from requests import Response

def normalise_url(url: str) -> str:
    return url if url.startswith(('http://', 'https://')) else f'https://{url}'

def check_status(url: str, timeout: int = 10) -> Response | None:
    url = normalise_url(url)

    try:
        response: Response = requests.get(url, timeout=timeout)
    except Exception as e:
        print(f'ERROR: {e}')
        return

    return response

def display_status(response: Response) -> None:
    status_code: int = response.status_code
    elapsed_time: float = response.elapsed.total_seconds()
    reason: str = response.reason
    content_type: str = response.headers.get('Content-Type', '')
    encoding: str|None = response.encoding
    headers: dict[str, str] = dict(response.headers)

    print(f'Status code  : {status_code} ({reason})')
    print(f'Elapsed time : {elapsed_time*1000}ms')
    print(f'Content-Type : {content_type}')
    print(f'Encoding     : {encoding or 'n/a'}')
    print('Headers      :')
    for key, value in headers.items():
        print(f'  • {key}: {value}')

if __name__ == '__main__':
    response = check_status("www.amazon.com")
    if response is not None:
        display_status(response)
    else:
        print('Something went wrong...')


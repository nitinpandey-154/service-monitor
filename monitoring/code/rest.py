import requests


def monitor_rest(**kwargs):
    end_point = kwargs['end-point']
    return_code = kwargs['return-code']
    method = kwargs['method']
    if method == 'get':
        response = requests.get(end_point)
    elif method == 'post':
        response = requests.post(end_point)
    else:
        return False

    status_code = response.status_code
    if status_code == return_code:
        return True
    else:
        return False

from requests import post

def get_result(token) -> bool:
    """
    Check recaptcha result
    :param token: Check token
    :return: Token check result
    """
    u = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': '6LePxpUbAAAAAJFqpr2fVDLLPUdhgRbTYZQw0xGn',
        'response': token,
    }
    try:
        return post(u, data=data).json()['success']
    except Exception as e:
        return False

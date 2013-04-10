from pyadmitad import client, transport


def get_authorizing_client(access_token, user_agent=None):
    """
    Creates a client using an access token.
    """
    http_transport = transport.HttpTransport(
        access_token, user_agent=user_agent)
    return client.Client(http_transport)


def get_oauth_password_client(client_id, client_secret,
                              username, password, scopes, user_agent=None):
    auth = transport.oauth_password_authorization({
        'client_id': client_id,
        'client_secret': client_secret,
        'username': username,
        'password': password,
        'scopes': scopes
    })
    return get_authorizing_client(auth['access_token'], user_agent=user_agent)


def get_oauth_client_client(client_id, client_secret, scopes, user_agent=None):
    auth = transport.oauth_client_authorization({
        'client_id': client_id,
        'client_secret': client_secret,
        'scopes': scopes
    })
    return get_authorizing_client(auth['access_token'], user_agent=user_agent)


def get_oauth_client(access_token):
    return get_authorizing_client(access_token, user_agent=None)



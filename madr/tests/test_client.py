from http import HTTPStatus


def test_create_account(client):
    response = client.post(
        '/conta/',
        json={
            'username': 'joao',
            'email': 'email@email.com',
            'password': 'password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'joao',
        'email': 'email@email.com',
    }


def test_update(client):
    response = client.put(
        'conta/1',
        json={
            'username': 'joao',
            'email': 'joao@email.com',
            'password': 'palavrapassedojoao',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'joao',
        'email': 'joao@email.com',
    }

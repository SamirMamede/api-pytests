import requests

ENDPOINT = 'https://todo.pixegami.io/'

def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_task():
    payload = {
        "content": "test api",
        "user_id": "teste-user-id",
        "is_done": False
    }
    create_task_response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert create_task_response.status_code == 200

    data = create_task_response.json()
    print(data)

    task_id = data['task']['task_id']
    get_task_id_response = requests.get(ENDPOINT + f"/get-task/{task_id}")
    assert get_task_id_response.status_code == 200

    data_get_task_id_response = get_task_id_response.json()
    print(data_get_task_id_response)
    assert data_get_task_id_response['content'] == payload['content']
    assert data_get_task_id_response['user_id'] == payload['user_id']

def test_update_task():
    # crete a task
    # update the task
    # get and validate the changes
    pass
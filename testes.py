import pytest
import requests

BASE_URL = "http://localhost:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "nova tarefa",
        "description": "Descricao de uma nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0].id
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert "id" in response_json
        assert "title" in response_json

def test_update_task():
    if tasks:
        task_id = tasks[0].id
        updated_task_data = {
            "title": "tarefa atualizada",
            "description": "Descricao atualizada",
            "completed": True
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=updated_task_data)
        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json
        #validação de valores atualizados
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == updated_task_data["title"]
        assert response_json["description"] == updated_task_data["description"]
        assert response_json["completed"] == updated_task_data["completed"]

def test_delete_task():
    if tasks:
        task_id = tasks[0].id   
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404


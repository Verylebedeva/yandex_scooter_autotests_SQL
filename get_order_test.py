# Вера Лебедева, 6-й поток — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data
import configuration

# функция для получения трэк-номера заказа
def get_order_track_number():
    response = sender_stand_request.post_new_order(data.order_body)
    return response.json()["track"]

# эта функция меняет значение в параметре t
def change_track_param(t):
    current_body = data.track_number.copy()
    current_body["t"] = t
    return current_body

def test_get_order_by_number_success_response():
    parpar = get_order_track_number()
    print (parpar)

    params = change_track_param(parpar)
    get_order_response = sender_stand_request.get_order_by_track_number(params)

    assert get_order_response.status_code == 200

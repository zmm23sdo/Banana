from API import change_order_status


order_no = "1220419424240000001"
headers = {'Authorization': '4211278B73B3424AB9B6701C83B558F5', 'X-Tenant-Type':'client'}
def test_change_order_status():
    order_status = change_order_status.ipay88Complete(
        payment_number = order_no,
        headers=headers
    )
    # print(f'test_change_order_status:{order_status.status_code}')
    assert str(order_status.status_code) == "200"
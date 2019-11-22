async def test_simple(guillotina):
    resp, status, headers = await guillotina.make_request("GET", "@double/2")
    assert status == 200
    assert resp["value"] == 4

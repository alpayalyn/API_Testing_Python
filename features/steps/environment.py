import requests

def after_scenario(context, scenario):
    response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

        "ID": context.bookId
    }, headers={"Content-Type": "application/json"},
                                        )
    assert response_deleteBook.status_code == 200
    context.res_json = response_deleteBook.json()

    print(res_json["msg"])
    assert res_json["msg"] == "book is successfully deleted."
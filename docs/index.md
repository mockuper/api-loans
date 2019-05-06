# loans online

- EN = Loans Online
- ID = Pinjaman Online

## app bundle

com.loans.online.android

## app process

<!---
participant mobile as m
participant server as s

opt registration
    m->>+s: POST /form
    s->>-m: token
end
opt data update
    m->>+s: GET /loans
    s->>-m: data[loan]
end
-->

![sheme](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=cGFydGljaXBhbnQgbW9iaWxlIGFzIG0KAAwMc2VydmVyIGFzIHMKCm9wdCByZWdpc3RyYXRpb24KICAgIG0tPj4rczogUE9TVCAvZm9ybQASBXMtPj4tbTogdG9rZW4KZW5kADkFZGF0YSB1cGRhdGUAMA1HRVQgL2xvYW5zADANZGF0YVtsb2FuXQplbmQ&s=magazine)

## model user

> POST /form
>
> - X-Country-Code: id
> - X-Security-Token: 67753e82-975f-49ca-af64-65e0e774c119
> - X-Device-Id: 65e0e774c119

```json
{
  "name": "Text",
  "phone": "Text",
  "email": "Text",
  "utm": {
    "utm_source": "Text",
    "utm_medium": "Text"
  }
}
```

=>200

```json
{
  "token": "67753e82-975f-49ca-af64-65e0e774c119"
}
```

=>404

```json
{
  "code": 39203,
  "message": "Text"
}
```

## model loan

> GET /loans
>
> - X-Country-Code: id
> - X-Security-Token: 654b370b-6219-44c7-9c23-38bf3e820927
> - X-Device-Id: 65e0e774c119
> - X-Auth-Token: 67753e82-975f-49ca-af64-65e0e774c119

=>200

```json
{
  "data": [
    {
      "name": "Text",
      "icon_url": "http://",
      "amount": {
        "currency": "USD",
        "min": 1,
        "max": 9999
      },
      "term": {
        "min": 1,
        "max": 99,
        "type": "d"
      },
      "discount": true,
      "description": "Text",
      "stars": 4.2,
      "action_url": "http://"
    }
  ]
}
```

=>401

```json
{
  "code": 39203,
  "message": "Text"
}
```

=>404

```json
{
  "code": 39203,
  "message": "Text"
}
```

| key                | value   | description                                               |
| ------------------ | ------- | --------------------------------------------------------- |
| data[x].term.type  | {d,m,y} | тип кредита для отображения d - дни, m - месяцы, y - годы |
| data[x].action_url | url     | урл на открытие webView                                   |

Ошибка 401 предусматривает релогин принудительный, в частности может понадобится для попытки юзера повторить логин через некоторое время для обновления информации в базе и при маркетинговой рассылке с проверкой гипотиз

!!! нужно будет реализовать схему с [.well-known/assetlinks.json](https://developer.android.com/training/app-links/verify-site-associations) на лэндинге кэшвагона или встроить в сайты кэшвагона

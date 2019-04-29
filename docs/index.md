# loans online

- EN = Loans Online
- ID = Pinjaman Online

## app bundle

com.loans.online.android

## model user

> POST /user
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
      "amout": {
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

| key       | value type | description                                               |
| --------- | ---------- | --------------------------------------------------------- |
| term.type | {d,m,y}    | тип кредита для отображения d - дни, m - месяцы, y - годы |

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

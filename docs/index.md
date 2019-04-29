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
    m->>+s: GET /form
    s->>-m: data[field]
    m->>+s: POST /form
    s->>-m: token
end
opt data update
    m->>+s: GET /loans
    s->>-m: data[loan]
end
-->

![sheme](https://www.websequencediagrams.com/cgi-bin/cdraw?lz=cGFydGljaXBhbnQgbW9iaWxlIGFzIG0KAAwMc2VydmVyIGFzIHMKCm9wdCByZWdpc3RyYXRpb24KICAgIG0tPj4rczogR0VUIC9mb3JtABEFABYFcy0-Pi1tOiBkYXRhW2ZpZWxkXQAmDVBPUwAoDAAnCHRva2VuCmVuZABsBWRhdGEgdXBkYXRlAF4SbG9hbnMAWhJsb2FuXQplbmQ&s=magazine)

## model user

> GET /form
>
> - X-Country-Code: id
> - X-Security-Token: 67753e82-975f-49ca-af64-65e0e774c119
> - X-Device-Id: 65e0e774c119

```json
{
  "data": [
    {
      "type": "name",
      "label": "Your name",
      "mask": "[A…]",
      "regexp": "^[\\w .'-]+$"
    }
  ]
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

| key            | value type           | description                                                   |
| -------------- | -------------------- | ------------------------------------------------------------- |
| data[x].type   | {name, phone, email} | тип поля для управление интерфейсом                           |
| data[x].mask   | string               | [RMR Mask](https://github.com/RedMadRobot/input-mask-android) |
| data[x].regexp | string               | вторичная валидация после маски на вменяемость                |

В интерфейсе валидность отображается иконочкой, если пройдена валидация по mask и regexp то зеленая галочка, иначе красная. Если поле станет необязательным к заполнению, то это можно решить через комбинацию полей mask и regexp

---

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

| key               | value type | description                                               |
| ----------------- | ---------- | --------------------------------------------------------- |
| data[x].term.type | {d,m,y}    | тип кредита для отображения d - дни, m - месяцы, y - годы |

Ошибка 401 предусматривает релогин принудительный, в частности может понадобится для попытки юзера повторить логин через некоторое время для обновления информации в базе и при маркетинговой рассылке с проверкой гипотиз
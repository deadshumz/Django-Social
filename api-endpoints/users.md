---
description: User endpoints
---

# Users

{% swagger method="get" path="/users/" baseUrl="https://127.0.0.1" summary="Get users" %}
{% swagger-description %}
**Returns all users**

Returns user by id if id specified
{% endswagger-description %}

{% swagger-parameter in="path" name="id" type="Integer" required="false" %}
User Id
{% endswagger-parameter %}

{% swagger-response status="200: OK" description="Response Example" %}
```javascript
{
        "id": 1,
        "username": "username",
        "first_name": "John",
        "last_name": "Smith",
        "email": "mail@domain.com",
        "is_active": true,
        "date_joined": "2022-01-01T00:00:0Z"
}
```
{% endswagger-response %}

{% swagger-response status="404: Not Found" description="If user not found ( Id incorrect )" %}
```javascript
{
    "detail": "Not found."
}
```
{% endswagger-response %}
{% endswagger %}

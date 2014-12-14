### Django test Client

Since we're likely testing a web application, we're likely a lot of the time going to need to make requests to the app. Easy!

    from django.test import Client
    client = Client()
    response = client.get('/')
    response = client.post('/posts/edit/1/', {"text": "Text content"})

The response from client provides everything you need to check what happened, including status code, rendered HTML, context, request, templates used, etc.

Note! Client is not browser emulation. You cannot do UI tests with it.

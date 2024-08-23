from django.http import HttpRequest, HttpResponse

def home(request: HttpRequest) -> HttpResponse:
    body = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Server Mama Cas</title>
</head>
<body>
<p>Les urls dispos sont celles du projet <a href="https://github.com/jbittel/django-mama-cas">Django Mama CAS</a> : </p>
<ul>
    <li>/cas/login</li>
    <li>/cas/logout</li>
    <li>/cas/validate</li>
    <li>/cas/serviceValidate</li>
    <li>/cas/proxyValidate</li>
    <li>/cas/proxy</li>
    <li>/cas/p3/serviceValidate</li>
    <li>/cas/p3/proxyValidate</li>
    <li>/cas/warn</li>
    <li>/cas/samlValidate</li>
</ul>

<p> Pour comprendre le role de ces urls, voir <a href="https://apereo.github.io/cas/7.0.x/protocol/CAS-Protocol-Specification.html">Description protocole CAS</a></p>

</body>
</html>
        """
    return HttpResponse(body)

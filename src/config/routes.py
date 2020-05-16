users = {
    'prefix': '/users',
    'index': '',
    'create': '',
    'show': '/<int:user_id>',
    'destroy': '/<int:user_id>',
    'update': '/<int:user_id>',
}

authentication = {
    'prefix': '',
    'login': '/login',
}

assessments = {
    'prefix': '/users/<int:user_id>/assessments',
    'index': ''
}

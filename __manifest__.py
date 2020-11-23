{
'name': 'Library Members',
'description': 'Miembros para la librería.',
'author': 'Francisco Valdes',
'data': [
    'views/book_view.xml',
    'security/ir.model.access.csv',
    'security/library_security.xml',
    'views/member_view.xml',
    'views/library_menu.xml',
    'views/book_list_template.xml',
],
'depends': [
    'library_app',
    'mail',
],
'application': False,
}


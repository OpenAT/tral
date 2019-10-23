# -*- coding: utf-8 -*-

{
    'name': 'tral_config',
    'summary': '''FS-Online tral instance configuration''',
    'description': '''
FS-Online Instance Configuration
================================

Customer configuration for the instance tral

- Default settings
- View modifications
- CSS
- Translations
    ''',
    'author': 'Michael Karrer (michael.karrer@datadialog.net), DataDialog',
    'version': '1.0',
    'website': 'https://www.datadialog.net',
    'installable': True,
    'depends': [
        'fsonline',
    ],
    'data': [
        'views/snippet_options.xml',
        'views/templates.xml',
    ],
}

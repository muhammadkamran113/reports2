# -*- coding: utf-8 -*-
{
    'name': "Commercial Invoice for V4",

    'summary': "Commercial Invoice for V4",

    'description': "Commercial Invoice for V4",

    'author': "Muhammmad Kamran",
    'website': "http://www.bcube.com",

    # any module necessary for this one to work correctly
    'depends': ['base', 'report', 'account'],
    # always loaded
    'data': [
        'template.xml',
        'views/module_report.xml',
    ],
    'css': ['static/src/css/report.css'],
}
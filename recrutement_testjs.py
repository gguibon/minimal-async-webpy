#!/usr/bin/env python

"""
This a simple python API dedicated to the engineer interview process at Inria Nancy for the Arborator-Grew project.
Instructions are located in the README file.

This program does not require any argument but requires the following packages :
pip3 install lorem web.py
"""

__author__  = "Gaël Guibon"


import web, lorem, json

bdd = {"projects":
    {"superproj": {"id": "superproj", "title": "super😍 proj", "description": lorem.text(), "author": "Bob"},
    "wonderfulproj": {"id":"wonderfulproj", "title": "wonderful🤩 proj", "description": lorem.text(), "author": "Babs"},
    "coolproj": {"id":"coolproj", "title": "cool😎 proj", "description": lorem.text(), "author": "Grewy"},
    "chillproj": {"id":"chillproj", "title": "chill😙 proj", "description": lorem.text(), "author": "Arbo"}
    },
    "authors": {"bob": {"name": "Bob", "role": "admin"}, 
        "babs": {"name": "Babs", "role": "user"}, 
        "grewy": {"name": "Grewy", "role": "user"}, 
        "arbo": {"name": "Arbo", "role": "user"}}
}

urls = ("/projectlist", "projectlist", 
        "/project/(.*)", "project", "/projectadd", "projectadd" )

class projectlist:
    def GET(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Content-Type', 'application/json')
        return json.dumps(list(bdd["projects"].values()))

class project:
    def GET(self, name):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Content-Type', 'application/json')
        print('name', name)
        return json.dumps(bdd["projects"][name])

class projectadd:
    def POST(self):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Content-Type', 'application/json')
        data = json.loads(web.data())
        print("data", data)
        bdd["projects"][data['pname']].setdefault(data['pdata'], {"title":"", "description": "", "author": ""})
        return json.dumps(bdd["projects"][data["pname"]])

if __name__ == "__main__":
    app = web.application(urls, globals(), autoreload=False)
    app.run()
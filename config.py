from .optimizeimages import optipng

worlds["janus"] = "../world"

def SettlementFilter(poi):
    if poi['id'] == 'Settlement':
        return poi['name']

renders["janusday"] = {
    "world": "janus",
    "title": "Day",
    "rendermode": smooth_lighting,
    "dimension": "overworld",
    "northdirection" : "lower-right",
    "showspawn" : False,
    "optimizeimg" : [optipng(olevel=3)],
    "defaultzoom" : 10,
    "center" : [328, 64, 95],
    'manualpois':[
               {'id':'Settlement',
                'x':282,
                'y':64,
                'z':102,
                'name':'Janus City'},
               {'id':'Settlement',
                'x':3617,
                'y':64,
                'z':159,
                'name':'Blattebyn'}],
               {'id':'Settlement',
                'x':376,
                'y':64,
                'z':-1416,
                'name':'Kyrkstaden'}],
                {'id':'Settlement',
                'x':380,
                'y':64,
                'z':1996,
                'name':'Penisbyn'}],
                {'id':'Settlement',
                'x':940,
                'y':64,
                'z':23,
                'name':'Jonny City'}],
                {'id':'Settlement',
                'x':3740,
                'y':64,
                'z':1251,
                'name':'Mahjong City'}],
    'markers': [dict(name="Settlements", filterFunction=SettlementFilter, icon="icons/marker_janustown.png")],
}

renders["janusnight"] = {
    "world": "janus",
    "title": "Night",
    "rendermode": smooth_night,
    "dimension": "overworld",
    "northdirection" : "lower-right",
    "showspawn" : False,
    "optimizeimg" : [optipng(olevel=3)],
    "defaultzoom" : 10,
    "center" : [328, 64, 95],
    'markers': [dict(name="Settlements", filterFunction=SettlementFilter, icon="icons/marker_janustown.png")],
}

outputdir = "../maps"
texturepath = "../textures_1.15"

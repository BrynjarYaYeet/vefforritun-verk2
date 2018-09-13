from sys import argv

import bottle
from bottle import *

@route("/")
def index():
    return """
    <h2> Verkefni 2. </h2>
    <p><a href="/a"> Liður A </a></p>
    <p><a href="/b"> Liður B </a></p>
    """

@route("/a")
def a():
    return """
        <h2> Verkefni 2.A </h2>
        <a href="/sidaA/1"> Síða 1. </a> -
        <a href="/sidaA/2"> Síða 2. </a> -
        <a href="/sidaA/3"> Síða 3. </a> -
    """

@route("/b")
def b():
    return """
        <h2> Verkefni 2.B </h2>
        <a href="/sidaB/1"> Síða 1. </a> -
        <a href="/sidaB/2"> Síða 2. </a> -
        <a href="/sidaB/3"> Síða 3. </a> -
    """


@route("/myndir/<skra>")
def static_skra(skra):
    return static_file(skra, root="./myndir")


@route("/sidaA/<id>")
def page(id):
    if id == "1":
        return """
        Þetta er síða 1.A<br><a href="/a"> Til baka </a>
        """
    if id == "2":
        return """
        Þetta er síða 2.A<br><a href="/a"> Til baka </a>
        """
    if id == "3":
        return """
        Þetta er síða 3.A<br><a href="/a"> Til baka </a>
        """
@route("/b")
def b():
    return """
    <h2>Verkefni 2 - B</h2>
    <h4> Veldu mynd</h4>
    <a href ="/sida2?bokstafur=a"><img src="myndir/a.jpg"></a>
    <a href ="/sida2?bokstafur=b"><img src="myndir/b.jpg"></a>
    <a href ="/sida2?bokstafur=c"><img src="myndir/c.jpg"></a>
    <a href ="/sida2?bokstafur=d"><img src="myndir/d.jpg"></a>
    """

@route("/sida2")
def page():
    l=request.query.bokstafur
    if l == "a":
        return """<h3>Hér er karlin: </h3> <img src="myndir/a.jpg">"""
    if l == "b":
        return """<h3>Hér er kerlan: </h3> <img src="myndir/b.jpg">"""
    if l == "c":
        return """<h3>Hér er karlin: </h3> <img src="myndir/c.jpg">"""
    if l == "d":
        return """<h3>Hér er karlin: </h3> <img src="myndir/d.jpg">"""





@error(404)
def villa(error):
    return """
        <h2 style='color:red'>Þessi síða finnst ekki </h2>
    """

#run(host="localhost", port=8020)

run(host='0.0.0.0', port=argv[1])

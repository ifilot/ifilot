from jinja2 import Environment, FileSystemLoader
import os
import requests
import sys

def main():
    # Jinja2 template folder
    env = Environment(loader=FileSystemLoader(os.path.join(
        os.path.dirname(__file__), 
        'templates')
    ))

    # Load the template
    template = env.get_template('index.tpl')

    # show languages / tools
    language_icons = [
        'https://img.shields.io/badge/-C-blue?logo=c&logoColor=white',
        'https://img.shields.io/badge/-C++-blue?logo=cplusplus',
        'https://img.shields.io/badge/assembly-6502-e32dbf.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjAiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiI+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjA2LjAyLDk1Ljg1Yy0wLjEsMS42OC0wLjE3LDIuMzMtMC4xNywyLjk4Yy0wLjAxLDM3LjMzLDAuMDIsNzQuNjUtMC4wOCwxMTEuOTgKCQljLTAuMDEsMy4wNiwwLjk3LDQuNjksMy42NSw2LjIyYzMxLjc3LDE4LjIxLDYzLjQ1LDM2LjU2LDk1LjE2LDU0Ljg2YzEuMzQsMC43NywyLjc2LDEuNCw0LjM0LDIuMTljMC4yNS0xLjE5LDAuNDMtMS42NiwwLjQzLTIuMTQKCQljMC4wMS0zNy42Ni0wLjA1LTc1LjMyLDAuMDgtMTEyLjk3YzAuMDEtMy4zOC0xLjc2LTQuNTktNC4xNi01Ljk4Yy0yNy42OS0xNS45NS01NS4zNC0zMS45Ni04My4wMS00Ny45NAoJCUMyMTcuMTIsMTAyLjA5LDIxMS45Myw5OS4xOSwyMDYuMDIsOTUuODV6IE0zMDkuMzgsMzAxLjQzYy0xLjY3LDAuODMtMi40MywxLjE2LTMuMTQsMS41OGMtMzIuMTQsMTguNTMtNjQuMjUsMzcuMTEtOTYuNDUsNTUuNTQKCQljLTMuMDEsMS43Mi00LjAzLDMuNjEtNC4wMSw3LjA1YzAuMTMsMzYuNjQsMC4wOCw3My4yOSwwLjA4LDEwOS45M2MwLDEuMjMsMCwyLjQ2LDAsNC4yNGMxLjc0LTAuODIsMi44LTEuMjIsMy43Ny0xLjc4CgkJYzMyLjE1LTE4LjUyLDY0LjI2LTM3LjA5LDk2LjQ2LTU1LjUyYzIuOC0xLjYsMy4zNC0zLjUyLDMuMzMtNi40NWMtMC4wOC0zNi40OC0wLjA0LTcyLjk2LTAuMDMtMTA5LjQzCgkJQzMwOS4zOCwzMDUuMTQsMzA5LjM4LDMwMy42OSwzMDkuMzgsMzAxLjQzeiBNMjEzLjQxLDgyLjUxYzEuMzcsMC42NCwxLjg0LDAuODIsMi4yNywxLjA2YzMyLjg0LDE4Ljk3LDY1LjY1LDM3Ljk5LDk4LjU5LDU2Ljc4CgkJYzEuNTEsMC44Niw0LjUyLDAuNDMsNi4yLTAuNTNjMzEuOTItMTguMjQsNjMuNzQtMzYuNjUsOTUuNTctNTUuMDRjMS4xOS0wLjY5LDIuMjctMS41NSwzLjU1LTIuNDJjLTAuNzMtMC41Ny0wLjk3LTAuODEtMS4yNS0wLjk4CgkJYy0zMi45Ny0xOS4wNy02NS45My0zOC4xNy05OS01Ny4wOGMtMS4zOS0wLjgtNC4xNC0wLjQyLTUuNjgsMC40NGMtMTIuMiw2LjgxLTI0LjI2LDEzLjg3LTM2LjM3LDIwLjg2CgkJQzI1Ni40MSw1Ny42NiwyMzUuNTQsNjkuNzMsMjEzLjQxLDgyLjUxeiBNMzAxLjI4LDI4OC4wNmMtMS42OC0xLjExLTIuNi0xLjgtMy41OS0yLjM3Yy0zMS44NC0xOC40LTYzLjczLTM2LjctOTUuNDctNTUuMjgKCQljLTMuNjUtMi4xNC02LjAxLTEuMDYtOC45OSwwLjY3Yy0yNy45MywxNi4xOS01NS45LDMyLjMtODMuODUsNDguNDVjLTQuNTgsMi42NS05LjEyLDUuMzctMTMuOTYsOC4yMmMwLjksMC43MywxLjM0LDEuMiwxLjg4LDEuNTEKCQljMzIuNzEsMTguODksNjUuNDQsMzcuNzMsOTguMDksNTYuNzJjMi41MywxLjQ3LDQuMTgsMC44NCw2LjI4LTAuMzljMTUuNTQtOS4wMiwzMS4xMi0xNy45OCw0Ni42OC0yNi45NgoJCUMyNjUuNzcsMzA4LjU4LDI4My4xOSwyOTguNTEsMzAxLjI4LDI4OC4wNnogTTE5MC40LDQ4MGMwLjEyLTEuNzcsMC4yMS0yLjQzLDAuMjEtMy4wOWMwLjAxLTM3LjQ2LTAuMDUtNzQuOTMsMC4xLTExMi4zOQoJCWMwLjAxLTMuMzgtMS42NC00LjYxLTQuMDYtNmMtMjAuMzQtMTEuNjgtNDAuNjMtMjMuNDMtNjAuOTQtMzUuMTVjLTEyLjQ4LTcuMi0yNC45OC0xNC4zNy0zNy45Mi0yMS44MQoJCWMtMC4xNywxLjU4LTAuMzcsMi41MS0wLjM3LDMuNDVjLTAuMDEsMzcuMywwLjA0LDc0LjU5LTAuMDgsMTExLjg5Yy0wLjAxLDMuMDIsMS4yMSw0LjM5LDMuNiw1Ljc2CgkJYzI0LjIzLDEzLjksNDguNCwyNy45LDcyLjU5LDQxLjg3QzE3Mi4yNyw0NjkuNTgsMTgxLjAyLDQ3NC42LDE5MC40LDQ4MHogTTMyNC42NSwyNzQuMDRjMS40My0wLjU4LDIuMzYtMC44NSwzLjE3LTEuMzIKCQljMzIuMjgtMTguNjEsNjQuNTMtMzcuMjgsOTYuODctNTUuOGMyLjYyLTEuNSwzLjE3LTMuMjcsMy4xNi01Ljk4Yy0wLjA3LTM2Ljk4LTAuMDUtNzMuOTctMC4wNy0xMTAuOTVjMC0xLjA4LTAuMTktMi4xNi0wLjMzLTMuNzYKCQljLTEuNjUsMC44Mi0yLjgyLDEuMzQtMy45MywxLjk3Yy0zMS41NiwxOC4yMS02My4wOSwzNi40OC05NC43MSw1NC41OGMtMy4xNywxLjgxLTQuMjYsMy43OS00LjI0LDcuNDIKCQljMC4xNCwzNS45OCwwLjA5LDcxLjk3LDAuMDksMTA3Ljk1QzMyNC42NSwyNjkuOTUsMzI0LjY1LDI3MS43NCwzMjQuNjUsMjc0LjA0eiBNNDI3LjM4LDIzMy40MWMtMS41OCwwLjY5LTIuODEsMS4xLTMuOTEsMS43MwoJCWMtMzEuOTksMTguNDctNjQsMzYuOTItOTUuODcsNTUuNTljLTEuNjUsMC45Ny0zLjA2LDMuODctMy4wNyw1Ljg4Yy0wLjE4LDM3LjE1LTAuMTMsNzQuMy0wLjExLDExMS40NmMwLDAuOSwwLjIxLDEuOCwwLjM3LDMuMDIKCQljMS4wMi0wLjQzLDEuNjQtMC42MSwyLjE5LTAuOTNjMzIuNDMtMTguNyw2NC44NC0zNy40NCw5Ny4zMS01Ni4wNmMyLjczLTEuNTYsMy4zOS0zLjQ0LDMuMzktNi40MQoJCWMtMC4xLTM2LjQ5LTAuMDYtNzIuOTctMC4wOC0xMDkuNDZDNDI3LjYsMjM2Ljc5LDQyNy40NywyMzUuMzUsNDI3LjM4LDIzMy40MXoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0yMDYuMDIsOTUuODVjNS45MSwzLjM1LDExLjEsNi4yNCwxNi4yNSw5LjIxYzI3LjY3LDE1Ljk4LDU1LjMyLDMxLjk5LDgzLjAxLDQ3Ljk0CgkJYzIuNCwxLjM4LDQuMTcsMi42LDQuMTYsNS45OGMtMC4xMywzNy42Ni0wLjA4LDc1LjMxLTAuMDgsMTEyLjk3YzAsMC40OC0wLjE5LDAuOTYtMC40MywyLjE0Yy0xLjU5LTAuOC0zLjAxLTEuNDItNC4zNC0yLjE5CgkJYy0zMS43MS0xOC4zLTYzLjM5LTM2LjY2LTk1LjE2LTU0Ljg2Yy0yLjY4LTEuNTMtMy42NS0zLjE2LTMuNjUtNi4yMmMwLjExLTM3LjMyLDAuMDctNzQuNjUsMC4wOC0xMTEuOTgKCQlDMjA1Ljg2LDk4LjE4LDIwNS45Myw5Ny41MiwyMDYuMDIsOTUuODV6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMzA5LjM4LDMwMS40M2MwLDIuMjUsMCwzLjcsMCw1LjE1Yy0wLjAxLDM2LjQ4LTAuMDUsNzIuOTYsMC4wMywxMDkuNDNjMC4wMSwyLjkzLTAuNTMsNC44NS0zLjMzLDYuNDUKCQljLTMyLjIsMTguNDMtNjQuMzEsMzctOTYuNDYsNTUuNTJjLTAuOTcsMC41Ni0yLjAzLDAuOTYtMy43NywxLjc4YzAtMS43OCwwLTMuMDEsMC00LjI0YzAtMzYuNjQsMC4wNS03My4yOS0wLjA4LTEwOS45MwoJCWMtMC4wMS0zLjQzLDEuMDEtNS4zMyw0LjAxLTcuMDVjMzIuMi0xOC40Myw2NC4zMS0zNy4wMSw5Ni40NS01NS41NEMzMDYuOTUsMzAyLjYsMzA3LjcxLDMwMi4yNywzMDkuMzgsMzAxLjQzeiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTIxMy40MSw4Mi41MWMyMi4xMi0xMi43OCw0My0yNC44NCw2My44Ny0zNi45YzEyLjEtNi45OSwyNC4xNy0xNC4wNSwzNi4zNy0yMC44NgoJCWMxLjU0LTAuODYsNC4yOS0xLjI0LDUuNjgtMC40NGMzMy4wNywxOC45MSw2Ni4wMiwzOC4wMSw5OSw1Ny4wOGMwLjI4LDAuMTYsMC41MiwwLjQsMS4yNSwwLjk4Yy0xLjI4LDAuODgtMi4zNiwxLjc0LTMuNTUsMi40MgoJCWMtMzEuODMsMTguMzktNjMuNjUsMzYuOC05NS41Nyw1NS4wNGMtMS42NywwLjk2LTQuNjksMS4zOS02LjIsMC41M2MtMzIuOTQtMTguOC02NS43NS0zNy44MS05OC41OS01Ni43OAoJCUMyMTUuMjUsODMuMzIsMjE0Ljc4LDgzLjE1LDIxMy40MSw4Mi41MXoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMDEuMjgsMjg4LjA2Yy0xOC4wOSwxMC40NS0zNS41MSwyMC41Mi01Mi45NCwzMC41OGMtMTUuNTYsOC45OC0zMS4xNCwxNy45NC00Ni42OCwyNi45NgoJCWMtMi4xLDEuMjItMy43NiwxLjg2LTYuMjgsMC4zOUMxNjIuNzQsMzI3LDEzMCwzMDguMTYsOTcuMywyODkuMjdjLTAuNTQtMC4zMS0wLjk4LTAuNzgtMS44OC0xLjUxYzQuODQtMi44NSw5LjM4LTUuNTgsMTMuOTYtOC4yMgoJCWMyNy45NS0xNi4xNSw1NS45Mi0zMi4yNiw4My44NS00OC40NWMyLjk5LTEuNzMsNS4zNC0yLjgxLDguOTktMC42N2MzMS43MywxOC41OCw2My42MywzNi44OCw5NS40Nyw1NS4yOAoJCUMyOTguNjgsMjg2LjI2LDI5OS42LDI4Ni45NSwzMDEuMjgsMjg4LjA2eiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTE5MC40LDQ4MGMtOS4zOS01LjQtMTguMTMtMTAuNDItMjYuODctMTUuNDZjLTI0LjE5LTEzLjk3LTQ4LjM2LTI3Ljk3LTcyLjU5LTQxLjg3CgkJYy0yLjM5LTEuMzctMy42MS0yLjc0LTMuNi01Ljc2YzAuMTItMzcuMywwLjA3LTc0LjU5LDAuMDgtMTExLjg5YzAtMC45NCwwLjE5LTEuODcsMC4zNy0zLjQ1YzEyLjk0LDcuNDQsMjUuNDMsMTQuNjEsMzcuOTIsMjEuODEKCQljMjAuMzEsMTEuNzIsNDAuNjEsMjMuNDcsNjAuOTQsMzUuMTVjMi40MiwxLjM5LDQuMDgsMi42Miw0LjA2LDZjLTAuMTYsMzcuNDYtMC4xLDc0LjkzLTAuMSwxMTIuMzkKCQlDMTkwLjYyLDQ3Ny41NywxOTAuNTMsNDc4LjIzLDE5MC40LDQ4MHoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMjQuNjUsMjc0LjA0YzAtMi4zMSwwLTQuMDksMC01Ljg4YzAtMzUuOTgsMC4wNi03MS45Ny0wLjA5LTEwNy45NWMtMC4wMS0zLjYzLDEuMDctNS42MSw0LjI0LTcuNDIKCQljMzEuNjMtMTguMSw2My4xNS0zNi4zNyw5NC43MS01NC41OGMxLjEtMC42NCwyLjI4LTEuMTUsMy45My0xLjk3YzAuMTUsMS42LDAuMzMsMi42OCwwLjMzLDMuNzZjMC4wMiwzNi45OCwwLDczLjk3LDAuMDcsMTEwLjk1CgkJYzAuMDEsMi43MS0wLjU0LDQuNDgtMy4xNiw1Ljk4Yy0zMi4zMywxOC41Mi02NC41OSwzNy4xOS05Ni44Nyw1NS44QzMyNywyNzMuMiwzMjYuMDcsMjczLjQ2LDMyNC42NSwyNzQuMDR6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNNDI3LjM4LDIzMy40MWMwLjA5LDEuOTUsMC4yMiwzLjM4LDAuMjIsNC44MmMwLjAxLDM2LjQ5LTAuMDIsNzIuOTcsMC4wOCwxMDkuNDYKCQljMC4wMSwyLjk2LTAuNjYsNC44NC0zLjM5LDYuNDFjLTMyLjQ3LDE4LjYyLTY0Ljg4LDM3LjM2LTk3LjMxLDU2LjA2Yy0wLjU1LDAuMzItMS4xNywwLjUtMi4xOSwwLjkzCgkJYy0wLjE1LTEuMjItMC4zNy0yLjEyLTAuMzctMy4wMmMtMC4wMi0zNy4xNS0wLjA3LTc0LjMsMC4xMS0xMTEuNDZjMC4wMS0yLjAxLDEuNDItNC45MSwzLjA3LTUuODgKCQljMzEuODctMTguNjcsNjMuODgtMzcuMTIsOTUuODctNTUuNTlDNDI0LjU3LDIzNC41LDQyNS44LDIzNC4xLDQyNy4zOCwyMzMuNDF6Ii8+Cjwvc3ZnPg==',
        'https://img.shields.io/badge/assembly-z80-e32dbf.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjAiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiI+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjA2LjAyLDk1Ljg1Yy0wLjEsMS42OC0wLjE3LDIuMzMtMC4xNywyLjk4Yy0wLjAxLDM3LjMzLDAuMDIsNzQuNjUtMC4wOCwxMTEuOTgKCQljLTAuMDEsMy4wNiwwLjk3LDQuNjksMy42NSw2LjIyYzMxLjc3LDE4LjIxLDYzLjQ1LDM2LjU2LDk1LjE2LDU0Ljg2YzEuMzQsMC43NywyLjc2LDEuNCw0LjM0LDIuMTljMC4yNS0xLjE5LDAuNDMtMS42NiwwLjQzLTIuMTQKCQljMC4wMS0zNy42Ni0wLjA1LTc1LjMyLDAuMDgtMTEyLjk3YzAuMDEtMy4zOC0xLjc2LTQuNTktNC4xNi01Ljk4Yy0yNy42OS0xNS45NS01NS4zNC0zMS45Ni04My4wMS00Ny45NAoJCUMyMTcuMTIsMTAyLjA5LDIxMS45Myw5OS4xOSwyMDYuMDIsOTUuODV6IE0zMDkuMzgsMzAxLjQzYy0xLjY3LDAuODMtMi40MywxLjE2LTMuMTQsMS41OGMtMzIuMTQsMTguNTMtNjQuMjUsMzcuMTEtOTYuNDUsNTUuNTQKCQljLTMuMDEsMS43Mi00LjAzLDMuNjEtNC4wMSw3LjA1YzAuMTMsMzYuNjQsMC4wOCw3My4yOSwwLjA4LDEwOS45M2MwLDEuMjMsMCwyLjQ2LDAsNC4yNGMxLjc0LTAuODIsMi44LTEuMjIsMy43Ny0xLjc4CgkJYzMyLjE1LTE4LjUyLDY0LjI2LTM3LjA5LDk2LjQ2LTU1LjUyYzIuOC0xLjYsMy4zNC0zLjUyLDMuMzMtNi40NWMtMC4wOC0zNi40OC0wLjA0LTcyLjk2LTAuMDMtMTA5LjQzCgkJQzMwOS4zOCwzMDUuMTQsMzA5LjM4LDMwMy42OSwzMDkuMzgsMzAxLjQzeiBNMjEzLjQxLDgyLjUxYzEuMzcsMC42NCwxLjg0LDAuODIsMi4yNywxLjA2YzMyLjg0LDE4Ljk3LDY1LjY1LDM3Ljk5LDk4LjU5LDU2Ljc4CgkJYzEuNTEsMC44Niw0LjUyLDAuNDMsNi4yLTAuNTNjMzEuOTItMTguMjQsNjMuNzQtMzYuNjUsOTUuNTctNTUuMDRjMS4xOS0wLjY5LDIuMjctMS41NSwzLjU1LTIuNDJjLTAuNzMtMC41Ny0wLjk3LTAuODEtMS4yNS0wLjk4CgkJYy0zMi45Ny0xOS4wNy02NS45My0zOC4xNy05OS01Ny4wOGMtMS4zOS0wLjgtNC4xNC0wLjQyLTUuNjgsMC40NGMtMTIuMiw2LjgxLTI0LjI2LDEzLjg3LTM2LjM3LDIwLjg2CgkJQzI1Ni40MSw1Ny42NiwyMzUuNTQsNjkuNzMsMjEzLjQxLDgyLjUxeiBNMzAxLjI4LDI4OC4wNmMtMS42OC0xLjExLTIuNi0xLjgtMy41OS0yLjM3Yy0zMS44NC0xOC40LTYzLjczLTM2LjctOTUuNDctNTUuMjgKCQljLTMuNjUtMi4xNC02LjAxLTEuMDYtOC45OSwwLjY3Yy0yNy45MywxNi4xOS01NS45LDMyLjMtODMuODUsNDguNDVjLTQuNTgsMi42NS05LjEyLDUuMzctMTMuOTYsOC4yMmMwLjksMC43MywxLjM0LDEuMiwxLjg4LDEuNTEKCQljMzIuNzEsMTguODksNjUuNDQsMzcuNzMsOTguMDksNTYuNzJjMi41MywxLjQ3LDQuMTgsMC44NCw2LjI4LTAuMzljMTUuNTQtOS4wMiwzMS4xMi0xNy45OCw0Ni42OC0yNi45NgoJCUMyNjUuNzcsMzA4LjU4LDI4My4xOSwyOTguNTEsMzAxLjI4LDI4OC4wNnogTTE5MC40LDQ4MGMwLjEyLTEuNzcsMC4yMS0yLjQzLDAuMjEtMy4wOWMwLjAxLTM3LjQ2LTAuMDUtNzQuOTMsMC4xLTExMi4zOQoJCWMwLjAxLTMuMzgtMS42NC00LjYxLTQuMDYtNmMtMjAuMzQtMTEuNjgtNDAuNjMtMjMuNDMtNjAuOTQtMzUuMTVjLTEyLjQ4LTcuMi0yNC45OC0xNC4zNy0zNy45Mi0yMS44MQoJCWMtMC4xNywxLjU4LTAuMzcsMi41MS0wLjM3LDMuNDVjLTAuMDEsMzcuMywwLjA0LDc0LjU5LTAuMDgsMTExLjg5Yy0wLjAxLDMuMDIsMS4yMSw0LjM5LDMuNiw1Ljc2CgkJYzI0LjIzLDEzLjksNDguNCwyNy45LDcyLjU5LDQxLjg3QzE3Mi4yNyw0NjkuNTgsMTgxLjAyLDQ3NC42LDE5MC40LDQ4MHogTTMyNC42NSwyNzQuMDRjMS40My0wLjU4LDIuMzYtMC44NSwzLjE3LTEuMzIKCQljMzIuMjgtMTguNjEsNjQuNTMtMzcuMjgsOTYuODctNTUuOGMyLjYyLTEuNSwzLjE3LTMuMjcsMy4xNi01Ljk4Yy0wLjA3LTM2Ljk4LTAuMDUtNzMuOTctMC4wNy0xMTAuOTVjMC0xLjA4LTAuMTktMi4xNi0wLjMzLTMuNzYKCQljLTEuNjUsMC44Mi0yLjgyLDEuMzQtMy45MywxLjk3Yy0zMS41NiwxOC4yMS02My4wOSwzNi40OC05NC43MSw1NC41OGMtMy4xNywxLjgxLTQuMjYsMy43OS00LjI0LDcuNDIKCQljMC4xNCwzNS45OCwwLjA5LDcxLjk3LDAuMDksMTA3Ljk1QzMyNC42NSwyNjkuOTUsMzI0LjY1LDI3MS43NCwzMjQuNjUsMjc0LjA0eiBNNDI3LjM4LDIzMy40MWMtMS41OCwwLjY5LTIuODEsMS4xLTMuOTEsMS43MwoJCWMtMzEuOTksMTguNDctNjQsMzYuOTItOTUuODcsNTUuNTljLTEuNjUsMC45Ny0zLjA2LDMuODctMy4wNyw1Ljg4Yy0wLjE4LDM3LjE1LTAuMTMsNzQuMy0wLjExLDExMS40NmMwLDAuOSwwLjIxLDEuOCwwLjM3LDMuMDIKCQljMS4wMi0wLjQzLDEuNjQtMC42MSwyLjE5LTAuOTNjMzIuNDMtMTguNyw2NC44NC0zNy40NCw5Ny4zMS01Ni4wNmMyLjczLTEuNTYsMy4zOS0zLjQ0LDMuMzktNi40MQoJCWMtMC4xLTM2LjQ5LTAuMDYtNzIuOTctMC4wOC0xMDkuNDZDNDI3LjYsMjM2Ljc5LDQyNy40NywyMzUuMzUsNDI3LjM4LDIzMy40MXoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0yMDYuMDIsOTUuODVjNS45MSwzLjM1LDExLjEsNi4yNCwxNi4yNSw5LjIxYzI3LjY3LDE1Ljk4LDU1LjMyLDMxLjk5LDgzLjAxLDQ3Ljk0CgkJYzIuNCwxLjM4LDQuMTcsMi42LDQuMTYsNS45OGMtMC4xMywzNy42Ni0wLjA4LDc1LjMxLTAuMDgsMTEyLjk3YzAsMC40OC0wLjE5LDAuOTYtMC40MywyLjE0Yy0xLjU5LTAuOC0zLjAxLTEuNDItNC4zNC0yLjE5CgkJYy0zMS43MS0xOC4zLTYzLjM5LTM2LjY2LTk1LjE2LTU0Ljg2Yy0yLjY4LTEuNTMtMy42NS0zLjE2LTMuNjUtNi4yMmMwLjExLTM3LjMyLDAuMDctNzQuNjUsMC4wOC0xMTEuOTgKCQlDMjA1Ljg2LDk4LjE4LDIwNS45Myw5Ny41MiwyMDYuMDIsOTUuODV6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMzA5LjM4LDMwMS40M2MwLDIuMjUsMCwzLjcsMCw1LjE1Yy0wLjAxLDM2LjQ4LTAuMDUsNzIuOTYsMC4wMywxMDkuNDNjMC4wMSwyLjkzLTAuNTMsNC44NS0zLjMzLDYuNDUKCQljLTMyLjIsMTguNDMtNjQuMzEsMzctOTYuNDYsNTUuNTJjLTAuOTcsMC41Ni0yLjAzLDAuOTYtMy43NywxLjc4YzAtMS43OCwwLTMuMDEsMC00LjI0YzAtMzYuNjQsMC4wNS03My4yOS0wLjA4LTEwOS45MwoJCWMtMC4wMS0zLjQzLDEuMDEtNS4zMyw0LjAxLTcuMDVjMzIuMi0xOC40Myw2NC4zMS0zNy4wMSw5Ni40NS01NS41NEMzMDYuOTUsMzAyLjYsMzA3LjcxLDMwMi4yNywzMDkuMzgsMzAxLjQzeiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTIxMy40MSw4Mi41MWMyMi4xMi0xMi43OCw0My0yNC44NCw2My44Ny0zNi45YzEyLjEtNi45OSwyNC4xNy0xNC4wNSwzNi4zNy0yMC44NgoJCWMxLjU0LTAuODYsNC4yOS0xLjI0LDUuNjgtMC40NGMzMy4wNywxOC45MSw2Ni4wMiwzOC4wMSw5OSw1Ny4wOGMwLjI4LDAuMTYsMC41MiwwLjQsMS4yNSwwLjk4Yy0xLjI4LDAuODgtMi4zNiwxLjc0LTMuNTUsMi40MgoJCWMtMzEuODMsMTguMzktNjMuNjUsMzYuOC05NS41Nyw1NS4wNGMtMS42NywwLjk2LTQuNjksMS4zOS02LjIsMC41M2MtMzIuOTQtMTguOC02NS43NS0zNy44MS05OC41OS01Ni43OAoJCUMyMTUuMjUsODMuMzIsMjE0Ljc4LDgzLjE1LDIxMy40MSw4Mi41MXoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMDEuMjgsMjg4LjA2Yy0xOC4wOSwxMC40NS0zNS41MSwyMC41Mi01Mi45NCwzMC41OGMtMTUuNTYsOC45OC0zMS4xNCwxNy45NC00Ni42OCwyNi45NgoJCWMtMi4xLDEuMjItMy43NiwxLjg2LTYuMjgsMC4zOUMxNjIuNzQsMzI3LDEzMCwzMDguMTYsOTcuMywyODkuMjdjLTAuNTQtMC4zMS0wLjk4LTAuNzgtMS44OC0xLjUxYzQuODQtMi44NSw5LjM4LTUuNTgsMTMuOTYtOC4yMgoJCWMyNy45NS0xNi4xNSw1NS45Mi0zMi4yNiw4My44NS00OC40NWMyLjk5LTEuNzMsNS4zNC0yLjgxLDguOTktMC42N2MzMS43MywxOC41OCw2My42MywzNi44OCw5NS40Nyw1NS4yOAoJCUMyOTguNjgsMjg2LjI2LDI5OS42LDI4Ni45NSwzMDEuMjgsMjg4LjA2eiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTE5MC40LDQ4MGMtOS4zOS01LjQtMTguMTMtMTAuNDItMjYuODctMTUuNDZjLTI0LjE5LTEzLjk3LTQ4LjM2LTI3Ljk3LTcyLjU5LTQxLjg3CgkJYy0yLjM5LTEuMzctMy42MS0yLjc0LTMuNi01Ljc2YzAuMTItMzcuMywwLjA3LTc0LjU5LDAuMDgtMTExLjg5YzAtMC45NCwwLjE5LTEuODcsMC4zNy0zLjQ1YzEyLjk0LDcuNDQsMjUuNDMsMTQuNjEsMzcuOTIsMjEuODEKCQljMjAuMzEsMTEuNzIsNDAuNjEsMjMuNDcsNjAuOTQsMzUuMTVjMi40MiwxLjM5LDQuMDgsMi42Miw0LjA2LDZjLTAuMTYsMzcuNDYtMC4xLDc0LjkzLTAuMSwxMTIuMzkKCQlDMTkwLjYyLDQ3Ny41NywxOTAuNTMsNDc4LjIzLDE5MC40LDQ4MHoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMjQuNjUsMjc0LjA0YzAtMi4zMSwwLTQuMDksMC01Ljg4YzAtMzUuOTgsMC4wNi03MS45Ny0wLjA5LTEwNy45NWMtMC4wMS0zLjYzLDEuMDctNS42MSw0LjI0LTcuNDIKCQljMzEuNjMtMTguMSw2My4xNS0zNi4zNyw5NC43MS01NC41OGMxLjEtMC42NCwyLjI4LTEuMTUsMy45My0xLjk3YzAuMTUsMS42LDAuMzMsMi42OCwwLjMzLDMuNzZjMC4wMiwzNi45OCwwLDczLjk3LDAuMDcsMTEwLjk1CgkJYzAuMDEsMi43MS0wLjU0LDQuNDgtMy4xNiw1Ljk4Yy0zMi4zMywxOC41Mi02NC41OSwzNy4xOS05Ni44Nyw1NS44QzMyNywyNzMuMiwzMjYuMDcsMjczLjQ2LDMyNC42NSwyNzQuMDR6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNNDI3LjM4LDIzMy40MWMwLjA5LDEuOTUsMC4yMiwzLjM4LDAuMjIsNC44MmMwLjAxLDM2LjQ5LTAuMDIsNzIuOTcsMC4wOCwxMDkuNDYKCQljMC4wMSwyLjk2LTAuNjYsNC44NC0zLjM5LDYuNDFjLTMyLjQ3LDE4LjYyLTY0Ljg4LDM3LjM2LTk3LjMxLDU2LjA2Yy0wLjU1LDAuMzItMS4xNywwLjUtMi4xOSwwLjkzCgkJYy0wLjE1LTEuMjItMC4zNy0yLjEyLTAuMzctMy4wMmMtMC4wMi0zNy4xNS0wLjA3LTc0LjMsMC4xMS0xMTEuNDZjMC4wMS0yLjAxLDEuNDItNC45MSwzLjA3LTUuODgKCQljMzEuODctMTguNjcsNjMuODgtMzcuMTIsOTUuODctNTUuNTlDNDI0LjU3LDIzNC41LDQyNS44LDIzNC4xLDQyNy4zOCwyMzMuNDF6Ii8+Cjwvc3ZnPg==',
        'https://img.shields.io/badge/assembly-8086/8088-e32dbf.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjAiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB3aWR0aD0iNTEyIiBoZWlnaHQ9IjUxMiI+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjA2LjAyLDk1Ljg1Yy0wLjEsMS42OC0wLjE3LDIuMzMtMC4xNywyLjk4Yy0wLjAxLDM3LjMzLDAuMDIsNzQuNjUtMC4wOCwxMTEuOTgKCQljLTAuMDEsMy4wNiwwLjk3LDQuNjksMy42NSw2LjIyYzMxLjc3LDE4LjIxLDYzLjQ1LDM2LjU2LDk1LjE2LDU0Ljg2YzEuMzQsMC43NywyLjc2LDEuNCw0LjM0LDIuMTljMC4yNS0xLjE5LDAuNDMtMS42NiwwLjQzLTIuMTQKCQljMC4wMS0zNy42Ni0wLjA1LTc1LjMyLDAuMDgtMTEyLjk3YzAuMDEtMy4zOC0xLjc2LTQuNTktNC4xNi01Ljk4Yy0yNy42OS0xNS45NS01NS4zNC0zMS45Ni04My4wMS00Ny45NAoJCUMyMTcuMTIsMTAyLjA5LDIxMS45Myw5OS4xOSwyMDYuMDIsOTUuODV6IE0zMDkuMzgsMzAxLjQzYy0xLjY3LDAuODMtMi40MywxLjE2LTMuMTQsMS41OGMtMzIuMTQsMTguNTMtNjQuMjUsMzcuMTEtOTYuNDUsNTUuNTQKCQljLTMuMDEsMS43Mi00LjAzLDMuNjEtNC4wMSw3LjA1YzAuMTMsMzYuNjQsMC4wOCw3My4yOSwwLjA4LDEwOS45M2MwLDEuMjMsMCwyLjQ2LDAsNC4yNGMxLjc0LTAuODIsMi44LTEuMjIsMy43Ny0xLjc4CgkJYzMyLjE1LTE4LjUyLDY0LjI2LTM3LjA5LDk2LjQ2LTU1LjUyYzIuOC0xLjYsMy4zNC0zLjUyLDMuMzMtNi40NWMtMC4wOC0zNi40OC0wLjA0LTcyLjk2LTAuMDMtMTA5LjQzCgkJQzMwOS4zOCwzMDUuMTQsMzA5LjM4LDMwMy42OSwzMDkuMzgsMzAxLjQzeiBNMjEzLjQxLDgyLjUxYzEuMzcsMC42NCwxLjg0LDAuODIsMi4yNywxLjA2YzMyLjg0LDE4Ljk3LDY1LjY1LDM3Ljk5LDk4LjU5LDU2Ljc4CgkJYzEuNTEsMC44Niw0LjUyLDAuNDMsNi4yLTAuNTNjMzEuOTItMTguMjQsNjMuNzQtMzYuNjUsOTUuNTctNTUuMDRjMS4xOS0wLjY5LDIuMjctMS41NSwzLjU1LTIuNDJjLTAuNzMtMC41Ny0wLjk3LTAuODEtMS4yNS0wLjk4CgkJYy0zMi45Ny0xOS4wNy02NS45My0zOC4xNy05OS01Ny4wOGMtMS4zOS0wLjgtNC4xNC0wLjQyLTUuNjgsMC40NGMtMTIuMiw2LjgxLTI0LjI2LDEzLjg3LTM2LjM3LDIwLjg2CgkJQzI1Ni40MSw1Ny42NiwyMzUuNTQsNjkuNzMsMjEzLjQxLDgyLjUxeiBNMzAxLjI4LDI4OC4wNmMtMS42OC0xLjExLTIuNi0xLjgtMy41OS0yLjM3Yy0zMS44NC0xOC40LTYzLjczLTM2LjctOTUuNDctNTUuMjgKCQljLTMuNjUtMi4xNC02LjAxLTEuMDYtOC45OSwwLjY3Yy0yNy45MywxNi4xOS01NS45LDMyLjMtODMuODUsNDguNDVjLTQuNTgsMi42NS05LjEyLDUuMzctMTMuOTYsOC4yMmMwLjksMC43MywxLjM0LDEuMiwxLjg4LDEuNTEKCQljMzIuNzEsMTguODksNjUuNDQsMzcuNzMsOTguMDksNTYuNzJjMi41MywxLjQ3LDQuMTgsMC44NCw2LjI4LTAuMzljMTUuNTQtOS4wMiwzMS4xMi0xNy45OCw0Ni42OC0yNi45NgoJCUMyNjUuNzcsMzA4LjU4LDI4My4xOSwyOTguNTEsMzAxLjI4LDI4OC4wNnogTTE5MC40LDQ4MGMwLjEyLTEuNzcsMC4yMS0yLjQzLDAuMjEtMy4wOWMwLjAxLTM3LjQ2LTAuMDUtNzQuOTMsMC4xLTExMi4zOQoJCWMwLjAxLTMuMzgtMS42NC00LjYxLTQuMDYtNmMtMjAuMzQtMTEuNjgtNDAuNjMtMjMuNDMtNjAuOTQtMzUuMTVjLTEyLjQ4LTcuMi0yNC45OC0xNC4zNy0zNy45Mi0yMS44MQoJCWMtMC4xNywxLjU4LTAuMzcsMi41MS0wLjM3LDMuNDVjLTAuMDEsMzcuMywwLjA0LDc0LjU5LTAuMDgsMTExLjg5Yy0wLjAxLDMuMDIsMS4yMSw0LjM5LDMuNiw1Ljc2CgkJYzI0LjIzLDEzLjksNDguNCwyNy45LDcyLjU5LDQxLjg3QzE3Mi4yNyw0NjkuNTgsMTgxLjAyLDQ3NC42LDE5MC40LDQ4MHogTTMyNC42NSwyNzQuMDRjMS40My0wLjU4LDIuMzYtMC44NSwzLjE3LTEuMzIKCQljMzIuMjgtMTguNjEsNjQuNTMtMzcuMjgsOTYuODctNTUuOGMyLjYyLTEuNSwzLjE3LTMuMjcsMy4xNi01Ljk4Yy0wLjA3LTM2Ljk4LTAuMDUtNzMuOTctMC4wNy0xMTAuOTVjMC0xLjA4LTAuMTktMi4xNi0wLjMzLTMuNzYKCQljLTEuNjUsMC44Mi0yLjgyLDEuMzQtMy45MywxLjk3Yy0zMS41NiwxOC4yMS02My4wOSwzNi40OC05NC43MSw1NC41OGMtMy4xNywxLjgxLTQuMjYsMy43OS00LjI0LDcuNDIKCQljMC4xNCwzNS45OCwwLjA5LDcxLjk3LDAuMDksMTA3Ljk1QzMyNC42NSwyNjkuOTUsMzI0LjY1LDI3MS43NCwzMjQuNjUsMjc0LjA0eiBNNDI3LjM4LDIzMy40MWMtMS41OCwwLjY5LTIuODEsMS4xLTMuOTEsMS43MwoJCWMtMzEuOTksMTguNDctNjQsMzYuOTItOTUuODcsNTUuNTljLTEuNjUsMC45Ny0zLjA2LDMuODctMy4wNyw1Ljg4Yy0wLjE4LDM3LjE1LTAuMTMsNzQuMy0wLjExLDExMS40NmMwLDAuOSwwLjIxLDEuOCwwLjM3LDMuMDIKCQljMS4wMi0wLjQzLDEuNjQtMC42MSwyLjE5LTAuOTNjMzIuNDMtMTguNyw2NC44NC0zNy40NCw5Ny4zMS01Ni4wNmMyLjczLTEuNTYsMy4zOS0zLjQ0LDMuMzktNi40MQoJCWMtMC4xLTM2LjQ5LTAuMDYtNzIuOTctMC4wOC0xMDkuNDZDNDI3LjYsMjM2Ljc5LDQyNy40NywyMzUuMzUsNDI3LjM4LDIzMy40MXoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0yMDYuMDIsOTUuODVjNS45MSwzLjM1LDExLjEsNi4yNCwxNi4yNSw5LjIxYzI3LjY3LDE1Ljk4LDU1LjMyLDMxLjk5LDgzLjAxLDQ3Ljk0CgkJYzIuNCwxLjM4LDQuMTcsMi42LDQuMTYsNS45OGMtMC4xMywzNy42Ni0wLjA4LDc1LjMxLTAuMDgsMTEyLjk3YzAsMC40OC0wLjE5LDAuOTYtMC40MywyLjE0Yy0xLjU5LTAuOC0zLjAxLTEuNDItNC4zNC0yLjE5CgkJYy0zMS43MS0xOC4zLTYzLjM5LTM2LjY2LTk1LjE2LTU0Ljg2Yy0yLjY4LTEuNTMtMy42NS0zLjE2LTMuNjUtNi4yMmMwLjExLTM3LjMyLDAuMDctNzQuNjUsMC4wOC0xMTEuOTgKCQlDMjA1Ljg2LDk4LjE4LDIwNS45Myw5Ny41MiwyMDYuMDIsOTUuODV6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMzA5LjM4LDMwMS40M2MwLDIuMjUsMCwzLjcsMCw1LjE1Yy0wLjAxLDM2LjQ4LTAuMDUsNzIuOTYsMC4wMywxMDkuNDNjMC4wMSwyLjkzLTAuNTMsNC44NS0zLjMzLDYuNDUKCQljLTMyLjIsMTguNDMtNjQuMzEsMzctOTYuNDYsNTUuNTJjLTAuOTcsMC41Ni0yLjAzLDAuOTYtMy43NywxLjc4YzAtMS43OCwwLTMuMDEsMC00LjI0YzAtMzYuNjQsMC4wNS03My4yOS0wLjA4LTEwOS45MwoJCWMtMC4wMS0zLjQzLDEuMDEtNS4zMyw0LjAxLTcuMDVjMzIuMi0xOC40Myw2NC4zMS0zNy4wMSw5Ni40NS01NS41NEMzMDYuOTUsMzAyLjYsMzA3LjcxLDMwMi4yNywzMDkuMzgsMzAxLjQzeiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTIxMy40MSw4Mi41MWMyMi4xMi0xMi43OCw0My0yNC44NCw2My44Ny0zNi45YzEyLjEtNi45OSwyNC4xNy0xNC4wNSwzNi4zNy0yMC44NgoJCWMxLjU0LTAuODYsNC4yOS0xLjI0LDUuNjgtMC40NGMzMy4wNywxOC45MSw2Ni4wMiwzOC4wMSw5OSw1Ny4wOGMwLjI4LDAuMTYsMC41MiwwLjQsMS4yNSwwLjk4Yy0xLjI4LDAuODgtMi4zNiwxLjc0LTMuNTUsMi40MgoJCWMtMzEuODMsMTguMzktNjMuNjUsMzYuOC05NS41Nyw1NS4wNGMtMS42NywwLjk2LTQuNjksMS4zOS02LjIsMC41M2MtMzIuOTQtMTguOC02NS43NS0zNy44MS05OC41OS01Ni43OAoJCUMyMTUuMjUsODMuMzIsMjE0Ljc4LDgzLjE1LDIxMy40MSw4Mi41MXoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMDEuMjgsMjg4LjA2Yy0xOC4wOSwxMC40NS0zNS41MSwyMC41Mi01Mi45NCwzMC41OGMtMTUuNTYsOC45OC0zMS4xNCwxNy45NC00Ni42OCwyNi45NgoJCWMtMi4xLDEuMjItMy43NiwxLjg2LTYuMjgsMC4zOUMxNjIuNzQsMzI3LDEzMCwzMDguMTYsOTcuMywyODkuMjdjLTAuNTQtMC4zMS0wLjk4LTAuNzgtMS44OC0xLjUxYzQuODQtMi44NSw5LjM4LTUuNTgsMTMuOTYtOC4yMgoJCWMyNy45NS0xNi4xNSw1NS45Mi0zMi4yNiw4My44NS00OC40NWMyLjk5LTEuNzMsNS4zNC0yLjgxLDguOTktMC42N2MzMS43MywxOC41OCw2My42MywzNi44OCw5NS40Nyw1NS4yOAoJCUMyOTguNjgsMjg2LjI2LDI5OS42LDI4Ni45NSwzMDEuMjgsMjg4LjA2eiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTE5MC40LDQ4MGMtOS4zOS01LjQtMTguMTMtMTAuNDItMjYuODctMTUuNDZjLTI0LjE5LTEzLjk3LTQ4LjM2LTI3Ljk3LTcyLjU5LTQxLjg3CgkJYy0yLjM5LTEuMzctMy42MS0yLjc0LTMuNi01Ljc2YzAuMTItMzcuMywwLjA3LTc0LjU5LDAuMDgtMTExLjg5YzAtMC45NCwwLjE5LTEuODcsMC4zNy0zLjQ1YzEyLjk0LDcuNDQsMjUuNDMsMTQuNjEsMzcuOTIsMjEuODEKCQljMjAuMzEsMTEuNzIsNDAuNjEsMjMuNDcsNjAuOTQsMzUuMTVjMi40MiwxLjM5LDQuMDgsMi42Miw0LjA2LDZjLTAuMTYsMzcuNDYtMC4xLDc0LjkzLTAuMSwxMTIuMzkKCQlDMTkwLjYyLDQ3Ny41NywxOTAuNTMsNDc4LjIzLDE5MC40LDQ4MHoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMjQuNjUsMjc0LjA0YzAtMi4zMSwwLTQuMDksMC01Ljg4YzAtMzUuOTgsMC4wNi03MS45Ny0wLjA5LTEwNy45NWMtMC4wMS0zLjYzLDEuMDctNS42MSw0LjI0LTcuNDIKCQljMzEuNjMtMTguMSw2My4xNS0zNi4zNyw5NC43MS01NC41OGMxLjEtMC42NCwyLjI4LTEuMTUsMy45My0xLjk3YzAuMTUsMS42LDAuMzMsMi42OCwwLjMzLDMuNzZjMC4wMiwzNi45OCwwLDczLjk3LDAuMDcsMTEwLjk1CgkJYzAuMDEsMi43MS0wLjU0LDQuNDgtMy4xNiw1Ljk4Yy0zMi4zMywxOC41Mi02NC41OSwzNy4xOS05Ni44Nyw1NS44QzMyNywyNzMuMiwzMjYuMDcsMjczLjQ2LDMyNC42NSwyNzQuMDR6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNNDI3LjM4LDIzMy40MWMwLjA5LDEuOTUsMC4yMiwzLjM4LDAuMjIsNC44MmMwLjAxLDM2LjQ5LTAuMDIsNzIuOTcsMC4wOCwxMDkuNDYKCQljMC4wMSwyLjk2LTAuNjYsNC44NC0zLjM5LDYuNDFjLTMyLjQ3LDE4LjYyLTY0Ljg4LDM3LjM2LTk3LjMxLDU2LjA2Yy0wLjU1LDAuMzItMS4xNywwLjUtMi4xOSwwLjkzCgkJYy0wLjE1LTEuMjItMC4zNy0yLjEyLTAuMzctMy4wMmMtMC4wMi0zNy4xNS0wLjA3LTc0LjMsMC4xMS0xMTEuNDZjMC4wMS0yLjAxLDEuNDItNC45MSwzLjA3LTUuODgKCQljMzEuODctMTguNjcsNjMuODgtMzcuMTIsOTUuODctNTUuNTlDNDI0LjU3LDIzNC41LDQyNS44LDIzNC4xLDQyNy4zOCwyMzMuNDF6Ii8+Cjwvc3ZnPg==',
        'https://img.shields.io/badge/python-3670A0?logo=python&logoColor=ffdd54',
        'https://img.shields.io/badge/Fortran-734F96?logo=fortran&logoColor=fff',
        'https://img.shields.io/badge/cMake-064F8C?&logo=cmake&logoColor=white',
        'https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white',
        'https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=fff',
        'https://img.shields.io/badge/cakephp-red?logo=cakephp&logoColor=white',
        'https://img.shields.io/badge/Arduino-00878F?logo=arduino&logoColor=fff',
        'https://img.shields.io/badge/-LaTeX-008080?logo=latex&logoColor=white',
        'https://img.shields.io/badge/Sphinx-F7C942?logo=sphinx&logoColor=white',
        'https://img.shields.io/badge/Blender-%23F5792A.svg?logo=blender&logoColor=white',
        'https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff',
        'https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white',
        'https://img.shields.io/badge/Jupyter%20Notebook-F37626?logo=jupyter&logoColor=white',
        'https://img.shields.io/badge/Debian-A81D33?logo=debian&logoColor=fff',
        'https://img.shields.io/badge/Ubuntu-E95420?logo=ubuntu&logoColor=white',
        'https://img.shields.io/badge/CUDA-76B900?logo=nvidia&logoColor=white',
        'https://img.shields.io/badge/Sublime%20Text-%23575757.svg?logo=sublime-text&logoColor=important',
        'https://img.shields.io/badge/Vim-%2311AB00.svg?logo=vim&logoColor=white',
        'https://img.shields.io/badge/Shell-4EAA25?logo=gnu-bash&logoColor=white',
        'https://img.shields.io/badge/Notepad++-90E59A.svg?&logo=notepad%2b%2b&logoColor=white',
        'https://img.shields.io/badge/-RaspberryPi-C51A4A?logo=Raspberry-Pi',
        'https://img.shields.io/badge/Qt-green'
    ]

    ############################################################################
    # Computational Chemistry Projects
    ############################################################################
    ccp_repositories = get_repo_data([
        'pyqint',
        'pydft',
        'pypwdft',
        'pytessel',
        'hfcxx',
        'dftcxx',
        'edp',
        'den2obj',
        'sphecerix',
        'bramble',
        'wavefuse',
        'turing',
        'pylebedev',
        'atom-architect',
        'den2bin',
        'ppmil',
	'managlyph',
    ])

    ############################################################################
    # P2000T / C Chemistry Projects
    ############################################################################
    p2k_repositories = get_repo_data([
        'p2000t-sdcard',
        'p2000t-cartridges',
        'p2000t-ram-expansion-board',
        'p2000t-joystick-cartridge',
        'p2000t-cartridge-reader',
        'p2000t-z80-ide',
        'p2000t-scart-connector-pcb',
        'p2000c-bytebridge-8086',
        'P2000T-SD-kaart-handleiding',
    ])

    ############################################################################
    # Open source hardware solutions
    ############################################################################
    oshw_repositories = get_repo_data([
        'pico-sst39sf0x0-programmer',
        'pico-flasher-cli',
    ])

    ############################################################################
    # Open source education
    ############################################################################
    osed_repositories = get_repo_data([
        'opengl-cpp-course',
        'hsl-pwdft-exercises',
        'pwdft-lecture-notes',
        'hfhsl2021',
        'hfhsl',
    ])

    ############################################################################
    # Other 8-bit consoles, handhelds and computers
    ############################################################################
    dev8bit_repositories = get_repo_data([
        'gameboy-cartridge-reader',
    ])  

    ############################################################################
    # 8-bit games
    ############################################################################
    games8b_repositories = get_repo_data([
        'cx16-kakuro',
        'cx16-othello',
        'tetrix',
    ])

    ############################################################################
    # Custom computer designs
    ############################################################################
    compdes_repositories = get_repo_data([
        'sap-smd',
    ])

    # Define the data to pass to the template
    data = {
        'language_icons' : language_icons,
        'ccp_repositories' : ccp_repositories,
        'p2k_repositories' : p2k_repositories,
        'oshw_repositories' : oshw_repositories,
        'osed_repositories' : osed_repositories,
        'games8b_repositories' : games8b_repositories,
        'dev8bit_repositories' : dev8bit_repositories,
        'compdes_repositories' : compdes_repositories,
    }

    # Render the template with the data
    output = template.render(data)

    # Write the rendered HTML to a file
    with open("README.md", "w") as f:
        f.write(output)

def get_repo_data(repositories):
    """
    Grab repository information by supplying repository names
    """
    # use token
    token = sys.argv[1]

    repos = []
    for repo in repositories:
        res = fetch_github_repo_details('ifilot', repo, token)
        res['languages'] = fetch_github_languages('ifilot', repo, token)[:2]
        repos.append(res)
    return repos

def fetch_github_repo_details(owner, repo, token):
    """
    Fetch repository information like number of stars, open issues, forks,
    description and html link.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stars = data.get("stargazers_count", 0)
        issues = data.get("open_issues_count", 0)
        link = data.get("html_url", "No link available")
        forks = data.get("forks_count", 0)
        description = data.get("description", "No description available")
        return {
            "stars": stars,
            "issues": issues,
            "forks": forks,
            "description": description,
            "link": link,
            "repo": repo,
        }
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

def fetch_github_languages(owner, repo, token=None):
    """
    Fetch dominant language of repository
    """
    # Fetch languages from the GitHub API
    api_url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    headers = {"Accept": "application/vnd.github.v3+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch languages: {response.status_code}")
        return None
    
    languages = response.json()
    
    # Fetch language colors
    colors_response = requests.get("https://raw.githubusercontent.com/ozh/github-colors/master/colors.json")
    if colors_response.status_code != 200:
        print("Failed to fetch language colors.")
        return None
    
    colors = colors_response.json()
    
    # Match languages with their colors
    language_data = []
    for lang, bytes_count in languages.items():
        color = colors.get(lang, {}).get("color", "#CCCCCC")  # Default to grey if no color found
        language_data.append({
            "language": lang,
            "bytes": bytes_count,
            "color": color,
        })
    
    return language_data

if __name__ == '__main__':
    main()

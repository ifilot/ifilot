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
        'https://img.shields.io/badge/assembly-6502-e32dbf.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjAiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEyIDUxMiIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjAwLjUyLDgzLjUyYzM4LjI0LDIyLjEsNzUuMzksNDMuNTQsMTEyLjQ2LDY1LjA5YzAuOTYsMC41NiwxLjY0LDIuNDMsMS42NCwzLjY5CgkJYzAuMDgsNDIuNDIsMC4wNyw4NC44MywwLjA3LDEyOC43MmMtMzUuOTItMjAuNzQtNzEuMDUtNDAuNzEtMTA1LjcyLTYxLjQ2Yy00LjEyLTIuNDctOC4wMS05LjE1LTguMDktMTMuOTQKCQlDMjAwLjI1LDE2NS40LDIwMC41MiwxMjUuMTcsMjAwLjUyLDgzLjUyeiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTMxNC43MSwzMTAuMjJjMCw0My45OSwwLjAxLDg2LjczLTAuMDcsMTI5LjQ3YzAsMS4wNi0wLjgzLDIuNTgtMS43MywzLjEKCQljLTM3LjA5LDIxLjUtNzQuMjMsNDIuOTItMTEyLjM3LDY0LjkyYzAtNDMuOTUtMC4wMi04Ni44MiwwLjEtMTI5LjY4YzAtMS4xLDEuMzEtMi42LDIuNC0zLjI0CgkJQzIzOS44NSwzNTMuNDMsMjc2LjcsMzMyLjE3LDMxNC43MSwzMTAuMjJ6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjA5LjEsNjguOTNjMzgtMjEuOTYsNzQuODQtNDMuMjYsMTExLjc0LTY0LjQ1YzEuMTMtMC42NSwzLjI5LTAuNjMsNC40MywwLjAzCgkJQzM2Mi4xOCwyNS42OSwzOTkuMDIsNDYuOTksNDM3LDY4LjkzYy0zOC4xLDIxLjk3LTc1LjQ3LDQzLjU0LTExMi44OSw2NS4wMWMtMC43MSwwLjQxLTIuMiwwLjAyLTMuMDYtMC40NwoJCUMyODQuMDUsMTEyLjE4LDI0Ny4wOCw5MC44NCwyMDkuMSw2OC45M3oiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMDYuMTEsMjk1LjYyYy0zNy45LDIxLjg5LTc0Ljc1LDQzLjE5LTExMS42Niw2NC40Yy0xLjA1LDAuNi0yLjk2LDAuODUtMy45MiwwLjMKCQljLTM3LjIxLTIxLjMzLTc0LjM1LTQyLjc2LTExMi4zNi02NC42OWMzNy45OS0yMS45MSw3NS4xNS00My4zNSwxMTIuMzYtNjQuN2MwLjg4LTAuNSwyLjU4LTAuNDIsMy40OSwwLjEKCQlDMjMxLjA4LDI1Mi4zMiwyNjguMDksMjczLjY4LDMwNi4xMSwyOTUuNjJ6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMTgzLjc1LDUwNy43MmMtMzcuOTgtMjEuOTUtNzQuODMtNDMuMjMtMTExLjY1LTY0LjU4Yy0wLjk1LTAuNTUtMi4wOC0xLjg4LTIuMDgtMi44NQoJCWMtMC4xLTQyLjk0LTAuMDktODUuODgtMC4wOS0xMjkuODZjMzcuOTEsMjEuODcsNzQuOTEsNDMuMiwxMTEuODUsNjQuNjNjMSwwLjU4LDEuODksMi4zMywxLjg5LDMuNTMKCQlDMTgzLjc2LDQyMS4xOSwxODMuNzUsNDYzLjgsMTgzLjc1LDUwNy43MnoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMzEuNTksMjgwLjk2YzAtNDQuMDEtMC4wMS04Ni43NywwLjA3LTEyOS41MmMwLTEuMDMsMC44Ni0yLjUxLDEuNzUtMy4wMwoJCWMzNi45MS0yMS40Myw3My44Ny00Mi43OCwxMTEuOS02NC43NmMwLDQ0LjA2LDAuMDEsODYuOTUtMC4wOSwxMjkuODNjMCwwLjk2LTEuMDcsMi4yOC0yLDIuODIKCQlDNDA2LjQ0LDIzNy42NywzNjkuNjEsMjU4Ljk2LDMzMS41OSwyODAuOTZ6Ii8+PHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTQ0NS4xMywyMzQuODFjMCw0NC4wMSwwLjAyLDg2Ljc1LTAuMSwxMjkuNDhjMCwxLjE0LTEuMTYsMi43Mi0yLjIyLDMuMzMKCQljLTM2Ljc3LDIxLjM1LTczLjYsNDIuNjEtMTExLjQ0LDY0LjQ4YzAtNDQuMDktMC4wMS04Ny4xNCwwLjA2LTEzMC4yYzAtMC43MywwLjc0LTEuNzYsMS40My0yLjE2CgkJQzM2OS45NCwyNzguMjcsNDA3LjA0LDI1Ni44Myw0NDUuMTMsMjM0LjgxeiIvPgo8L3N2Zz4=',
        'https://img.shields.io/badge/assembly-z80-e32dbf.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjAiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEyIDUxMiIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjAwLjUyLDgzLjUyYzM4LjI0LDIyLjEsNzUuMzksNDMuNTQsMTEyLjQ2LDY1LjA5YzAuOTYsMC41NiwxLjY0LDIuNDMsMS42NCwzLjY5CgkJYzAuMDgsNDIuNDIsMC4wNyw4NC44MywwLjA3LDEyOC43MmMtMzUuOTItMjAuNzQtNzEuMDUtNDAuNzEtMTA1LjcyLTYxLjQ2Yy00LjEyLTIuNDctOC4wMS05LjE1LTguMDktMTMuOTQKCQlDMjAwLjI1LDE2NS40LDIwMC41MiwxMjUuMTcsMjAwLjUyLDgzLjUyeiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTMxNC43MSwzMTAuMjJjMCw0My45OSwwLjAxLDg2LjczLTAuMDcsMTI5LjQ3YzAsMS4wNi0wLjgzLDIuNTgtMS43MywzLjEKCQljLTM3LjA5LDIxLjUtNzQuMjMsNDIuOTItMTEyLjM3LDY0LjkyYzAtNDMuOTUtMC4wMi04Ni44MiwwLjEtMTI5LjY4YzAtMS4xLDEuMzEtMi42LDIuNC0zLjI0CgkJQzIzOS44NSwzNTMuNDMsMjc2LjcsMzMyLjE3LDMxNC43MSwzMTAuMjJ6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjA5LjEsNjguOTNjMzgtMjEuOTYsNzQuODQtNDMuMjYsMTExLjc0LTY0LjQ1YzEuMTMtMC42NSwzLjI5LTAuNjMsNC40MywwLjAzCgkJQzM2Mi4xOCwyNS42OSwzOTkuMDIsNDYuOTksNDM3LDY4LjkzYy0zOC4xLDIxLjk3LTc1LjQ3LDQzLjU0LTExMi44OSw2NS4wMWMtMC43MSwwLjQxLTIuMiwwLjAyLTMuMDYtMC40NwoJCUMyODQuMDUsMTEyLjE4LDI0Ny4wOCw5MC44NCwyMDkuMSw2OC45M3oiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMDYuMTEsMjk1LjYyYy0zNy45LDIxLjg5LTc0Ljc1LDQzLjE5LTExMS42Niw2NC40Yy0xLjA1LDAuNi0yLjk2LDAuODUtMy45MiwwLjMKCQljLTM3LjIxLTIxLjMzLTc0LjM1LTQyLjc2LTExMi4zNi02NC42OWMzNy45OS0yMS45MSw3NS4xNS00My4zNSwxMTIuMzYtNjQuN2MwLjg4LTAuNSwyLjU4LTAuNDIsMy40OSwwLjEKCQlDMjMxLjA4LDI1Mi4zMiwyNjguMDksMjczLjY4LDMwNi4xMSwyOTUuNjJ6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMTgzLjc1LDUwNy43MmMtMzcuOTgtMjEuOTUtNzQuODMtNDMuMjMtMTExLjY1LTY0LjU4Yy0wLjk1LTAuNTUtMi4wOC0xLjg4LTIuMDgtMi44NQoJCWMtMC4xLTQyLjk0LTAuMDktODUuODgtMC4wOS0xMjkuODZjMzcuOTEsMjEuODcsNzQuOTEsNDMuMiwxMTEuODUsNjQuNjNjMSwwLjU4LDEuODksMi4zMywxLjg5LDMuNTMKCQlDMTgzLjc2LDQyMS4xOSwxODMuNzUsNDYzLjgsMTgzLjc1LDUwNy43MnoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMzEuNTksMjgwLjk2YzAtNDQuMDEtMC4wMS04Ni43NywwLjA3LTEyOS41MmMwLTEuMDMsMC44Ni0yLjUxLDEuNzUtMy4wMwoJCWMzNi45MS0yMS40Myw3My44Ny00Mi43OCwxMTEuOS02NC43NmMwLDQ0LjA2LDAuMDEsODYuOTUtMC4wOSwxMjkuODNjMCwwLjk2LTEuMDcsMi4yOC0yLDIuODIKCQlDNDA2LjQ0LDIzNy42NywzNjkuNjEsMjU4Ljk2LDMzMS41OSwyODAuOTZ6Ii8+PHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTQ0NS4xMywyMzQuODFjMCw0NC4wMSwwLjAyLDg2Ljc1LTAuMSwxMjkuNDhjMCwxLjE0LTEuMTYsMi43Mi0yLjIyLDMuMzMKCQljLTM2Ljc3LDIxLjM1LTczLjYsNDIuNjEtMTExLjQ0LDY0LjQ4YzAtNDQuMDktMC4wMS04Ny4xNCwwLjA2LTEzMC4yYzAtMC43MywwLjc0LTEuNzYsMS40My0yLjE2CgkJQzM2OS45NCwyNzguMjcsNDA3LjA0LDI1Ni44Myw0NDUuMTMsMjM0LjgxeiIvPgo8L3N2Zz4=',
        'https://img.shields.io/badge/assembly-8086/8088-e32dbf.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB2ZXJzaW9uPSIxLjAiIGlkPSJMYXllcl8xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB4PSIwcHgiIHk9IjBweCIKCSB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgZW5hYmxlLWJhY2tncm91bmQ9Im5ldyAwIDAgNTEyIDUxMiIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjAwLjUyLDgzLjUyYzM4LjI0LDIyLjEsNzUuMzksNDMuNTQsMTEyLjQ2LDY1LjA5YzAuOTYsMC41NiwxLjY0LDIuNDMsMS42NCwzLjY5CgkJYzAuMDgsNDIuNDIsMC4wNyw4NC44MywwLjA3LDEyOC43MmMtMzUuOTItMjAuNzQtNzEuMDUtNDAuNzEtMTA1LjcyLTYxLjQ2Yy00LjEyLTIuNDctOC4wMS05LjE1LTguMDktMTMuOTQKCQlDMjAwLjI1LDE2NS40LDIwMC41MiwxMjUuMTcsMjAwLjUyLDgzLjUyeiIvPgoJPHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTMxNC43MSwzMTAuMjJjMCw0My45OSwwLjAxLDg2LjczLTAuMDcsMTI5LjQ3YzAsMS4wNi0wLjgzLDIuNTgtMS43MywzLjEKCQljLTM3LjA5LDIxLjUtNzQuMjMsNDIuOTItMTEyLjM3LDY0LjkyYzAtNDMuOTUtMC4wMi04Ni44MiwwLjEtMTI5LjY4YzAtMS4xLDEuMzEtMi42LDIuNC0zLjI0CgkJQzIzOS44NSwzNTMuNDMsMjc2LjcsMzMyLjE3LDMxNC43MSwzMTAuMjJ6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMjA5LjEsNjguOTNjMzgtMjEuOTYsNzQuODQtNDMuMjYsMTExLjc0LTY0LjQ1YzEuMTMtMC42NSwzLjI5LTAuNjMsNC40MywwLjAzCgkJQzM2Mi4xOCwyNS42OSwzOTkuMDIsNDYuOTksNDM3LDY4LjkzYy0zOC4xLDIxLjk3LTc1LjQ3LDQzLjU0LTExMi44OSw2NS4wMWMtMC43MSwwLjQxLTIuMiwwLjAyLTMuMDYtMC40NwoJCUMyODQuMDUsMTEyLjE4LDI0Ny4wOCw5MC44NCwyMDkuMSw2OC45M3oiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMDYuMTEsMjk1LjYyYy0zNy45LDIxLjg5LTc0Ljc1LDQzLjE5LTExMS42Niw2NC40Yy0xLjA1LDAuNi0yLjk2LDAuODUtMy45MiwwLjMKCQljLTM3LjIxLTIxLjMzLTc0LjM1LTQyLjc2LTExMi4zNi02NC42OWMzNy45OS0yMS45MSw3NS4xNS00My4zNSwxMTIuMzYtNjQuN2MwLjg4LTAuNSwyLjU4LTAuNDIsMy40OSwwLjEKCQlDMjMxLjA4LDI1Mi4zMiwyNjguMDksMjczLjY4LDMwNi4xMSwyOTUuNjJ6Ii8+Cgk8cGF0aCBmaWxsPSIjRkZGRkZGIiBkPSJNMTgzLjc1LDUwNy43MmMtMzcuOTgtMjEuOTUtNzQuODMtNDMuMjMtMTExLjY1LTY0LjU4Yy0wLjk1LTAuNTUtMi4wOC0xLjg4LTIuMDgtMi44NQoJCWMtMC4xLTQyLjk0LTAuMDktODUuODgtMC4wOS0xMjkuODZjMzcuOTEsMjEuODcsNzQuOTEsNDMuMiwxMTEuODUsNjQuNjNjMSwwLjU4LDEuODksMi4zMywxLjg5LDMuNTMKCQlDMTgzLjc2LDQyMS4xOSwxODMuNzUsNDYzLjgsMTgzLjc1LDUwNy43MnoiLz4KCTxwYXRoIGZpbGw9IiNGRkZGRkYiIGQ9Ik0zMzEuNTksMjgwLjk2YzAtNDQuMDEtMC4wMS04Ni43NywwLjA3LTEyOS41MmMwLTEuMDMsMC44Ni0yLjUxLDEuNzUtMy4wMwoJCWMzNi45MS0yMS40Myw3My44Ny00Mi43OCwxMTEuOS02NC43NmMwLDQ0LjA2LDAuMDEsODYuOTUtMC4wOSwxMjkuODNjMCwwLjk2LTEuMDcsMi4yOC0yLDIuODIKCQlDNDA2LjQ0LDIzNy42NywzNjkuNjEsMjU4Ljk2LDMzMS41OSwyODAuOTZ6Ii8+PHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTQ0NS4xMywyMzQuODFjMCw0NC4wMSwwLjAyLDg2Ljc1LTAuMSwxMjkuNDhjMCwxLjE0LTEuMTYsMi43Mi0yLjIyLDMuMzMKCQljLTM2Ljc3LDIxLjM1LTczLjYsNDIuNjEtMTExLjQ0LDY0LjQ4YzAtNDQuMDktMC4wMS04Ny4xNCwwLjA2LTEzMC4yYzAtMC43MywwLjc0LTEuNzYsMS40My0yLjE2CgkJQzM2OS45NCwyNzguMjcsNDA3LjA0LDI1Ni44Myw0NDUuMTMsMjM0LjgxeiIvPgo8L3N2Zz4=',
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
	'bytecradle-6502',
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

import pyfiglet
import sys
import docker

print('------------------------------')
print('|  Virtual Environment Info  |')
print('------------------------------')
print(sys.executable)
print(sys.version)

print('------------------------------')
print('|        Docker Info         |')
print('------------------------------')
try:
    client = docker.from_env()
    info = client.info()
    print("Docker Python library is installed and working!")
    print(f" - Docker version: {info.get('ServerVersion')}")
except Exception as e:
    print("An error occurred while testing the Docker library:")
    print(e)

print('------------------------------')
print('|          ASCII Art         |')
print('------------------------------')
print(pyfiglet.figlet_format("BYU Cougars"))
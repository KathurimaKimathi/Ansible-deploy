from fabric.api import *

def deploy():
    local('ansible-playbook -i hosts.yml lets-encryprt.yml')
    #local('ansible-playbook -i hosts.yml playbook.yml')
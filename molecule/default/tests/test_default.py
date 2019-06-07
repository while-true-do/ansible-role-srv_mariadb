import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mariadb_package(host):
    pkg = host.package('mariadb-server')

    assert pkg.is_installed


def test_mariadb_service(host):
    srv = host.service('mariadb')

    assert srv.is_running
    assert srv.is_enabled

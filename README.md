<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_mariadb.svg)](https://github.com/while-true-do/ansible-role-srv_mariadb/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_mariadb.svg)](https://github.com/while-true-do/ansible-role-srv_mariadb/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_mariadb.svg)](https://github.com/while-true-do/ansible-role-srv_mariadb/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_mariadb.svg)](https://github.com/while-true-do/ansible-role-srv_mariadb/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_mariadb.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_mariadb)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_mariadb%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_mariadb)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_mariadb%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_mariadb)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_mariadb%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_mariadb)

# Ansible Role: srv_mariadb

An Ansible Role to install and configure mariadb.

## Motivation

[mariadb](https://mariadb.org/) is one of the most popular database servers.
Made by the original developers of MySQL.

## Description

This role installs and configures mariadb.

-   install mariadb packages
-   configure mariadb
-   configure firewalld
-   perform mysql-secure-installation steps

## Requirements

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible File Module](https://docs.ansible.com/ansible/latest/modules/file_module.html)
-   [Ansible Firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible mysql_user Module](https://docs.ansible.com/ansible/latest/modules/mysql_user_module.html)
-   [Ansible mysql_db Module](https://docs.ansible.com/ansible/latest/modules/mysql_db_module.html)
-   [Ansible package_facts Module](https://docs.ansible.com/ansible/latest/modules/package_facts_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_mariadb)
```
ansible-galaxy install while_true_do.srv_mariadb
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_mariadb)
```
git clone https://github.com/while-true-do/ansible-role-srv_mariadb.git while_true_do.srv_mariadb
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_mariadb

# Define the source of installation
# Currently only distribution packages are supported
wtd_srv_mariadb_source: "distribution"

## Package Management
wtd_srv_mariadb_package:
  - mariadb-server
  - python3-mysql
# State can be present|latest|absent
wtd_srv_mariadb_package_state: "present"

## Configuration Management
wtd_srv_mariadb_conf_root_pass: ""

wtd_srv_mariadb_conf_my_path: "/etc/my.cnf"
wtd_srv_mariadb_conf_server_path: "/etc/my.cnf.d/mariadb-server.cnf"

wtd_srv_mariadb_conf_server:
  port: "3306"
  bind_address: "127.0.0.1"
  character_set: "utf8mb4"
  symbolic_links: "0"
  data_dir: "/var/lib/mysql"
  socket: "/var/lib/mysql/mysql.sock"

wtd_srv_mariadb_conf_innodb:
  file_per_table: "true"
  buffer_pool_size: "128M"

wtd_srv_mariadb_conf_query_cache:
  type: "1"
  limit: "256K"
  min_res_unit: "2k"
  cache_size: "64M"

## Service Management
wtd_srv_mariadb_service: "mariadb"
# State can be started|stopped
wtd_srv_mariadb_service_state: "started"
wtd_srv_mariadb_service_enabled: true

## Firewalld Management
wtd_srv_mariadb_fw_mgmt: true
wtd_srv_mariadb_fw_service: "mysql"
# State can be enabled|disabled
wtd_srv_mariadb_fw_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_mariadb_fw_zone: "public"

## Host Management
wtd_srv_mariadb_reboot_enabled: true
wtd_srv_mariadb_reboot_msg: "System is going down to ..."
wtd_srv_mariadb_reboot_timeout: 3600
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_mariadb
      wtd_srv_mariadb_conf_root_pass: "myPassword"
```

#### Allow network traffic

```
- hosts: all
  roles:
    - role: while_true_do.srv_mariadb
      wtd_srv_mariadb_conf_root_pass: "myPassword"
      wtd_srv_mariadb_conf_server:
        port: "3306"
        bind_address: "0.0.0.0"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_mariadb/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_mariadb/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>

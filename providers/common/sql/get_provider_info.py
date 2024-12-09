# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# NOTE! THIS FILE IS AUTOMATICALLY GENERATED AND WILL BE
# OVERWRITTEN WHEN PREPARING PACKAGES.
#
# IF YOU WANT TO MODIFY THIS FILE, YOU SHOULD MODIFY THE TEMPLATE
# `get_provider_info_TEMPLATE.py.jinja2` IN the `dev/breeze/src/airflow_breeze/templates` DIRECTORY


def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-common-sql",
        "name": "Common SQL",
        "description": "`Common SQL Provider <https://en.wikipedia.org/wiki/SQL>`__\n",
        "state": "ready",
        "source-date-epoch": 1730012422,
        "versions": [
            "1.20.0",
            "1.19.0",
            "1.18.0",
            "1.17.1",
            "1.17.0",
            "1.16.0",
            "1.15.0",
            "1.14.2",
            "1.14.1",
            "1.14.0",
            "1.13.0",
            "1.12.0",
            "1.11.1",
            "1.11.0",
            "1.10.1",
            "1.10.0",
            "1.9.0",
            "1.8.1",
            "1.8.0",
            "1.7.2",
            "1.7.1",
            "1.7.0",
            "1.6.2",
            "1.6.1",
            "1.6.0",
            "1.5.2",
            "1.5.1",
            "1.5.0",
            "1.4.0",
            "1.3.4",
            "1.3.3",
            "1.3.2",
            "1.3.1",
            "1.3.0",
            "1.2.0",
            "1.1.0",
            "1.0.0",
        ],
        "dependencies": ["apache-airflow>=2.8.0", "sqlparse>=0.5.1", "more-itertools>=9.0.0"],
        "additional-extras": [
            {
                "name": "pandas",
                "dependencies": [
                    'pandas>=2.1.2,<2.2;python_version>="3.9"',
                    'pandas>=1.5.3,<2.2;python_version<"3.9"',
                ],
            }
        ],
        "integrations": [
            {
                "integration-name": "Common SQL",
                "external-doc-url": "https://en.wikipedia.org/wiki/SQL",
                "how-to-guide": ["/docs/apache-airflow-providers-common-sql/operators.rst"],
                "logo": "/integration-logos/common/sql/sql.png",
                "tags": ["software"],
            }
        ],
        "operators": [
            {
                "integration-name": "Common SQL",
                "python-modules": ["airflow.providers.common.sql.operators.sql"],
            }
        ],
        "hooks": [
            {"integration-name": "Common SQL", "python-modules": ["airflow.providers.common.sql.hooks.sql"]}
        ],
        "sensors": [
            {"integration-name": "Common SQL", "python-modules": ["airflow.providers.common.sql.sensors.sql"]}
        ],
    }
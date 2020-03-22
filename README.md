# Query results to Report Automation

## Pre-requisites

- Python 3.7 or above
- Git

## Setup

Follow the steps below to complete setup.

- Create virtual environment

```shell
py -m venv venv
```

- Activate the virual environment

  This step is required each time you want to use the scripts as the python packages used would be installed in the virtual environment. You can install the dependencies globally if you do not want to repeat this step.

```shell
venv\Scripts\activate
```

- Install Python Dependencies

```shell
pip install -r requirements.txt
```

- Create the environment file

  This step will help you setup a `.env` file that can store your database connection configuration

  - Create a file `.env` in the root of the folder
  - Add the following and update as required.
  - The `TRUSTED_CONN` can be set to 1 if trusted connection is required
  - You can ignore the `DB_USERNAME` and `DB_PASSWORD` if trusted connection is selected

  ```txt
  SERVER=<Server Name>
  DATABASE=<Database Name>
  TRUSTED_CONN=0
  DB_USERNAME=<username>
  DB_PASSWORD=<password>
  ```

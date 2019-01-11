#Setting up ELink SDK
##1. Introduction
This guide describes how to install the ELink SDK for Python in preparation for developing an automatic script.
##2. Prerequisites
The ASK SDK for Python requires Python 2 (>= 2.7) or Python 3.6. Before continuing, make sure you have a supported version of Python installed. To show the version, from a command prompt run the following command:
```bash
python --version
Python 3.6.5
```
You can download python 3.6 [here](https://www.python.org/downloads/)
##3. Adding the ELink SDK for python to your project
Adding the ELink SDK for Python to Your Project
You can download and install the ELink SDK for Python from the Python Package Index (PyPI) using the command line tool pip. If you are using Python 3 version 3.6, pip should be installed with Python by default.
Many Python developers prefer to work in a virtual environment, which is an isolated Python environment that helps manage project dependencies and package versions. The easiest way to get started is to install the SDK in a virtual environment. See the section Set up the SDK in a virtual environment.
Another option is to install the ELink SDK for Python to a specific folder. This ensures that you have the required dependencies and makes it easy to locate and deploy the required files for your finished skill. See the section Set up the SDK in a specific folder.
### 3.1 Option 1: Set up the SDK in a virtual environment
This option requires you to install the virtualenv package. virtualenv is a tool to create isolated Python environments. To get started, from a command prompt, use the following command to install the package:
```bash
$ pip install virtualenv
```
Next, create a new folder for your new elink script and navigate to the folder:
```bash
$ mkdir elink_env
$ cd elink_env
```
Next, create a virtual environment called elink_env by issuing the following command:
```bash
$ virtualenv elink_env
```
Next, activate your virtual environment and install the sdk.
Run the following command to activate your virtual environment:
```bash
$ elink_env\Scripts\activate
```
Next, install elink sdk with the activate environment
```bash
pip install elink-sdk --upgrade
```
### 3.2 Option 2: Set up the SDK in a specific folder.
//TODO
#### 3.3 Example
import elink skd and create a new connection to ELinkKVM (ipaddr: `10.42.0.2`)
```python
from elink_sdk import elink

elink.newConnection('10.42.0.2')
```


































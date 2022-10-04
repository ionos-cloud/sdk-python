# Python SDK

**NOTE:
_Please consider using SDK Python v6 releases that are using IONOS Cloud API Version 6, the latest stable API version. New features and improvements will be integrated in IONOS Cloud API Version 6._**

## Overview

The IONOS Cloud SDK for Python provides you with access to the IONOS Cloud API. The client library supports both simple and complex requests. It is designed for developers who are building applications in Python. The SDK for Python wraps the IONOS Cloud API. All API operations are performed over SSL and authenticated using your IONOS Cloud portal credentials. The API can be accessed within an instance running in IONOS Cloud or directly over the Internet from any application that can send an HTTPS request and receive an HTTPS response.

## Getting Started

An IONOS account is required for access to the Cloud API; credentials from your registration are used to authenticate against the IONOS Cloud API.

### Installation & Usage

**Requirements:**
- Python >= 3.5

### pip install

Since this package is hosted on PyPI \([https://pypi.org/](https://pypi.org/)\) you can install it like this

```bash
pip install ionoscloud
```

If the python package is hosted on a repository, you can install directly using:

```bash
pip install git+https://github.com/ionos-cloud/sdk-python.git
```

\(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/ionos-cloud/sdk-python.git`\)

Then import the package:

```python
import ionoscloud
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```bash
python setup.py install --user
```

\(or `sudo python setup.py install` to install the package for all users\)

Then import the package:

```python
import ionoscloud
```

> **_NOTE:_**  The Python SDK does not support Python 2. It only supports Python >= 3.5.


### Authentication

The username and password **or** the authentication token can be manually specified when initializing the SDK client:

```python
configuration = ionoscloud.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD',
    token='YOUR_API_KEY',
)
client = ionoscloud.ApiClient(configuration)
```

Environment variables can also be used. This is an example of how one would do that:

```python
import os

configuration = ionoscloud.Configuration(
    username=os.environ.get('IONOS_USERNAME'),
    password=os.environ.get('IONOS_PASSWORD'),
    token=os.environ.get('IONOS_TOKEN'),
)
client = ionoscloud.ApiClient(configuration)
```

**Warning**: Make sure to follow the Information Security Best Practices when using credentials within your code or storing them in a file.


### HTTP proxies

You can use http proxies by setting the following environment variables:
- `IONOS_HTTP_PROXY` - proxy URL
- `IONOS_HTTP_PROXY_HEADERS` - proxy headers


### Depth

Many of the _List_ or _Get_ operations will accept an optional _depth_ argument. Setting this to a value between 0 and 5 affects the amount of data that is returned. The details returned vary depending on the resource being queried, but it generally follows this pattern. By default, the SDK sets the _depth_ argument to the maximum value.

| Depth | Description |
| :--- | :--- |
| 0 | Only direct properties are included. Children are not included. |
| 1 | Direct properties and children's references are returned. |
| 2 | Direct properties and children's properties are returned. |
| 3 | Direct properties, children's properties, and descendants' references are returned. |
| 4 | Direct properties, children's properties, and descendants' properties are returned. |
| 5 | Returns all available properties. |

### Pretty

The operations will also accept an optional _pretty_ argument. Setting this to a value of `true` or `false` controls whether the response is pretty-printed \(with indentation and new lines\). By default, the SDK sets the _pretty_ argument to `true`.

### Changing the base URL

Base URL for the HTTP operation can be changed in the following way:

```python
import os

configuration = ionoscloud.Configuration(
    username=os.environ.get('IONOS_USERNAME'),
    password=os.environ.get('IONOS_PASSWORD'),
    host=os.environ.get('IONOS_API_URL'),
    server_index=None,
)
client = ionoscloud.ApiClient(configuration)
```

## Feature Reference

The IONOS Cloud SDK for Python aims to offer access to all resources in the IONOS Cloud API and also offers some additional features that make the integration easier:

* authentication for API calls
* handling of asynchronous requests 

## FAQ

1. How can I open a bug/feature request? 

Bugs & feature requests can be open on the repository issues: [https://github.com/ionos-cloud/sdk-python/issues/new/choose](https://github.com/ionos-cloud/sdk-python/issues/new/choose)

1. Can I contribute to the Python SDK?

Pure SDKs are automatically generated using OpenAPI Generator and don’t support manual changes. If you need changes please open an issue and we’ll try to take care of it.


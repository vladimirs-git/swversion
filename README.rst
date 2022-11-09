
.. image:: https://img.shields.io/pypi/v/swversion.svg
   :target: https://pypi.python.org/pypi/swversion
.. image:: https://img.shields.io/pypi/pyversions/swversion.svg
   :target: https://pypi.python.org/pypi/swversion


swversion
=========

Parse the given version string and return *SwVersion* object who can
compare (>, >=, <, <=) software versions of network devices: Cisco, etc.


Requirements
------------

Python >=3.8


Installation
------------

.. code:: bash

    pip install swversion


Usage
-----

.. code:: python

    import re
    from swversion import SwVersion

    text = "Cisco IOS Software, C2960X Software (C2960X-UNIVERSALK9-M), Version 15.2(4)E10, ..."
    text = re.search(r"Version (\S+),", text)[1]

    version1 = SwVersion(text)  # 15.2(4)E10
    version2 = SwVersion("15.2(4)E11")

    assert version1 < version2
    assert version1 <= version2
    assert not version1 > version2
    assert not version1 >= version2
    print(version1)
    print(version2)
    # 15.2(4)e10
    # 15.2(4)e11

[[package]]
name = "click"
version = "8.0.3"
description = "Composable command line interface toolkit"
category = "main"
optional = false
python-versions = ">=3.6"

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.4"
description = "Cross-platform colored terminal text."
category = "main"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*"

[metadata]
lock-version = "1.1"
python-versions = "^3.8"
content-hash = "c946ec5a4b0a44d9ab48cbfcd08ed0703605184e0152661eec3023cea727948d"

[metadata.files]
click = [
    {file = "click-8.0.3-py3-none-any.whl", hash = "sha256:353f466495adaeb40b6b5f592f9f91cb22372351c84caeb068132442a4518ef3"},
    {file = "click-8.0.3.tar.gz", hash = "sha256:410e932b050f5eed773c4cda94de75971c89cdb3155a72a0831139a79e5ecb5b"},
]
colorama = [
    {file = "colorama-0.4.4-py2.py3-none-any.whl", hash = "sha256:9f47eda37229f68eee03b24b9748937c7dc3868f906e8ba69fbcbdd3bc5dc3e2"},
    {file = "colorama-0.4.4.tar.gz", hash = "sha256:5941b2b48a20143d2267e95b1c2a7603ce057ee39fd88e7329b0c292aa16869b"},
]

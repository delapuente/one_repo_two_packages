This repository holds a very simple example of one repository building two
different packages. To switch between the two packages, you can use the
environment variable `TARGET_PACKAGE_NAME`, being one of `pack_a` or `pack_b`.

```
$ TARGET_PACKAGE_NAME=pack_a python setup.py sdist
$ TARGET_PACKAGE_NAME=pack_b python setup.py sdist
```

Built packages are available in the `dist` directory.

```
$ tree dist
dist
├── pack_a-1.0.tar.gz
└── pack_b-1.0.tar.gz
```

You can use the `pip` command to install the packages:

```
$ pip install dist/pack_a-1.0.tar.gz
$ pip install dist/pack_b-1.0.tar.gz
```

And so, two different packages can live in the same repository.

## How does it work?

The `setup.py` script is a minimal Python script that replaces itself with
the one of the target package, and delegate the rest of the execution to it.
After the package is built, the script is restored with the original one.

While installing the package, the `setup.py` script inside the package is
executed. Although there are slightly differences, running the repo setup
and the package setup should be equivalent for the purpose of `distutils`.
# Screenshot

Tool for capturing and organizing screen shots.

Requires [webkit2png](http://www.paulhammond.org/webkit2png/).

## Installation

```shell
$ git clone git@github.com:jefftriplett/screenshots-cli.git
$ cd screenshots-cli
$ pipenv install
```

## Usage

```shell
$ python screenshot.py
Usage: screenshot.py [OPTIONS] COMMAND [ARGS]...

  Screenshot!

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  main*
  init

Create a new project (notice the trailing "/"):
$ python screenshot.py init http://localhost:8000/

View the generated project/config:
$ cat localhost-8000.yml
domain: http://localhost:8000
paths:
- /

Capture your screen shots:
$ python screenshot.py localhost-8000.yml
  [####################################]  100%

Your screen shots are located in: `build/localhost-8000/`
```

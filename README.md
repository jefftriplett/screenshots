# Screenshots

Tool for capturing and organizing screen shots.

Requires [webkit2png](http://www.paulhammond.org/webkit2png/).

## Installation

```shell
$ git clone git@github.com:jefftriplett/screenshots.git
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

## Contact / Social Media

Here are a few ways to keep up with me online. If you have a question about this project, please consider opening a GitHub Issue. 

[![](https://jefftriplett.com/assets/images/social/github.png)](https://github.com/jefftriplett)
[![](https://jefftriplett.com/assets/images/social/globe.png)](https://jefftriplett.com/)
[![](https://jefftriplett.com/assets/images/social/twitter.png)](https://twitter.com/webology)
[![](https://jefftriplett.com/assets/images/social/docker.png)](https://hub.docker.com/u/jefftriplett/)

import click
import delegator

from click_default_group import DefaultGroup
from pathlib import Path
from slugify import slugify
from urllib import parse
from yaml import dump, load

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


CMD = "webkit2png --ignore-ssl-check --fullsize --clipped --width={width} --dir={output_folder} --filename={slug} {url}"
OUTPUT_FOLDER = Path('build')
WIDTH = "1280"


@click.group(cls=DefaultGroup, default='main', default_if_no_args=True)
@click.version_option()
def cli():
    """
    Screenshot!
    """


@cli.command()
@click.argument('url')
@click.argument('output_filename', required=False)
def init(url, output_filename):
    value = parse.urlparse(url)
    if not output_filename:
        domain_slug = slugify(value.netloc)
        output_filename = f'{domain_slug}.yml'

    data = {
        'domain': f'{value.scheme}://{value.netloc}',
        'paths': [
            value.path,
        ]
    }

    output = dump(data, Dumper=Dumper, default_flow_style=False)
    Path(output_filename).write_text(output)


@cli.command()
@click.argument('filename')
@click.argument('output_filename', required=False)
def main(filename, output_filename):
    with open(filename, 'r') as input_buffer:
        website = load(input_buffer.read())

        domain = website['domain']
        paths = website['paths']

        value = parse.urlparse(domain)
        domain_slug = slugify(value.netloc)

        output = []
        output_folder = OUTPUT_FOLDER.joinpath(domain_slug)

        if not output_folder.exists():
            output_folder.mkdir(parents=True)

        with click.progressbar(paths) as paths_progress:
            for path in paths_progress:
                url = f'{domain}{path}'
                slug = slugify(path if len(path.strip('/')) else 'homepage')

                command = CMD.format(
                    output_folder=output_folder,
                    slug=slug,
                    width=WIDTH,
                    url=url
                )

                clipped_filename = output_folder.joinpath(f'{slug}-clipped.png')
                screenshot_filename = output_folder.joinpath(f'{slug}-full.png')

                output.append(f'## {slug} - [{url}]({url})\n\n![]({clipped_filename})\n\n----\n\n')

                if not clipped_filename.exists() or not screenshot_filename.exists():
                    c = delegator.run(command)

            if not output_filename:
                output_filename = f'{domain_slug}.md'

            Path(output_filename).write_text('\n'.join(output))


if __name__ == '__main__':
    cli()

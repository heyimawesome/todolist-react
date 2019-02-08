import sys
import unittest

from flask.cli import FlaskGroup

from project import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def testing():
    print('Testing.. 1.. 2.. 3..')


@cli.command()
def test():
    tests = unittest.TestLoader().discover(
        'project/tests',
        pattern='test*.py'
    )
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    sys.exit(result)


if __name__ == '__main__':
    cli()

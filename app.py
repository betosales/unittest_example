from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'seja bem vindo'


@app.route('/jade')
def jade():
    return 'olá jaderesca'


@app.cli.command('test')
def testando():
    """Esse comando vai realizar os testes"""
    import unittest
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    app.run()

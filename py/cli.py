import click
from os import system as sys

@click.command()
@click.argument('file_name',required=False,type=click.Path())
def cli(file_name=None):
    #print('Running..')
    if file_name==None:
       file_name=r''
    sys('python {0}'.format(file_name))


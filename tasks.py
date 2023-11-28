#tasks.py
from invoke import task

@task(name="hello")
def hello(c):
    print("hello-world")
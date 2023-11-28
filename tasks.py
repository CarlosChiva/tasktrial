#tasks.py
from invoke import task

@task(name="hello")
def hello(c):
    print("hello-world")
@task(name="run")
def run(c):
    hello(c)    
@task(name="retu_string")
def retu_string(s)->str:
    return str(c)+"hello motherfucker"
@task(name="return_int")
def return_int(c)->int:
    return 1    
@task(name="main")
def main(m):
    print(retu_string(return_int()))

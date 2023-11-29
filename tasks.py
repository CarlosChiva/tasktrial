#tasks.py
from invoke import task
from taskersClass.write import write as wr
from taskersClass.read import read as rd

# invoke write --name="sdgk jsdfh"
# invoke write -n="shdglkj dshgf"
# invoke write --name dkflhgdsl
# invoke write -n sfjhgldkfh
@task(help={"name":"write a string to a file"})
def write(c,name="write a string to a file"):
    wr(name)
@task
def read(c)->str:
    return rd.r()    

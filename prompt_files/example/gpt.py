from importlib import reload
import foo
while True:
    reload(foo)
    foo.act()
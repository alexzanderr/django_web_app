



def some_exception():
    from rich.console import Console
    console = Console()
    try:
        do_something()
    except Exception:
        console.print_exception(
            show_locals=True,
            word_wrap=True)


_dictx = {
    "a": "asd",
    "list": [
        1, 12, 123, 123, 123, 123, 123
    ]
}
def normal_print():
    from rich import print as _print
    _print("123")
    _print(_dictx)

from rich.console import Console
console = Console()

def the_console():

    console.print_json(data=_dictx, indent=4)

    console.print(" this is some text ", style="bold black on yellow italic")
    console.print(console.get_datetime())


def text():
    from rich.text import Text
    t = Text("hello my name is andrew i think that rich is very rich")
    t.stylize("bold magenta", 0, 6)

    console.print(t)

def custom_themes():
    from rich.theme import Theme
    custom_theme = Theme({"good": "black on green italic", "bad": "black on red italic"})
    console = Console(theme=custom_theme)
    console.print("good message", style="good")
    console.print("bad message", style="bad")
    console.print("Operation [bad]failed[/bad]")

    console.print(":apple:")
    console.print(":bug:", style="good")
    console.print(":feature:")


from time import sleep
def logs():
    for i, x, y, z in zip(range(100), range(1000), range(100), range(100)):
        console.log("wow", log_locals=True)
        sleep(0.5)



def html():

    console = Console(record=True)
    console.print("asdasd")
    console.log("ASD")
    # console.print(console.export_html())
    console.print(console.export_text())


def tables():
    from rich.table import Table

    table = Table(title="star wars movies")
    table.add_column("time", style="magenta")
    table.add_column("users", style="green italic")
    table.add_column("column", style="red italic")

    table.add_row(str(console.get_datetime()), "abndrew")
    table.add_row(str(console.get_datetime()), "this is good for csv")
    table.add_row(str(console.get_datetime()), "this is good for csv", "this is not empty")

    console.print(table)

def markdown():

    from rich.markdown import Markdown
    markdown_string = \
    """
# django framework

### install django
```shell
sudo pip install Django
```

### create django project
```shell
django-admin startproject $website_name
```

### migrate settings
```shell
python manage.py migrate
```

### run server with custom port
```shell
python manage.py runserver 8123
```

### start custom app
```shell
python manage.py startapp polls
```
(din video-ul ala se vedea ca poti avea mai multe apps)

### create super user
```shell
python manage.py createsuperuser
```
add:
- username
- email
- password



# Databases

## Errors

### AttributeError: 'AuthToken' object has no attribute `_state`

this occurs when a model has `__init__` or `__init__` its improperly configured

models should never have `__init__` defined by the user


### AttributeError: type object 'AuthToken' has no attribute 'objects'

thats because you defined a custom manager inside your model
which is called `tokens`

so you should use
```diff
- x = A.objects.using("django_web_app_postgresql_db").create(token="asdiolfjbasdbjioio12gh317823")
+ x = A.tokens.using("django_web_app_postgresql_db").create(token="asdiolfjbasdbjioio12gh317823")
```

## How to migrate only for a single db but for multiple apps
```shell
1. python manage.py migrate auth --database=db2
2. python manage.py migrate app1 --database=db2
```

## if you want only to migrate for a specific app and for a specific database
```shell
python manage.py migrate api --database=postgres_db
echo "mutlipl"
echo "lines"
echo "of"
echo "shell"
```


## how to use managers on models

```python
# create new one without save
x = A.objects.using("django_web_app_postgresql_db").create(token="andrew2")

# filter by column
x = A.tokens.using("django_web_app_postgresql_db").filter(token="123")

# find all
x = A.tokens.using("django_web_app_postgresql_db").all()


# create new one and save
>>> a = A(token="from_save")
>>> a.save(using="django_web_app_postgresql_db")
>>> a.id
5
>>> a.token
'from_save'


# search for only one
>>> A.tokens.using("django_web_app_postgresql_db").get(token="andrew")
if doesnt exist:
    raises AuthTokens.DoesNotExist() exception
else:
    <AuthToken: <AuthToken token: 123>> object


# delete one
>>> az = A.tokens.using("django_web_app_postgresql_db").get(token="123")
>>> az.delete()
(1, {'api.AuthToken': 1})
```

    """

    mark = Markdown(
        markdown_string,
        code_theme="gruvbox-dark",
        inline_code_theme="gruvbox-dark",
        justify="left")
    console.print(mark)


def progressbars():
    from rich.progress import track
    for i in track(range(100), description="loading ..."):
        sleep(0.1)

def prompt():
    from rich.prompt import Prompt

    name = Prompt.ask("Enter your name")
    from rich.prompt import Prompt

    name = Prompt.ask("Enter your name", choices=["Paul", "Jessica", "Duncan"], default="Paul")

    from rich.prompt import Confirm

    is_rich_great = Confirm.ask("Do you like rich?")

    console.log(is_rich_great)

def tree():
    from rich.tree import Tree
    from rich import print

    tree = Tree("Rich Tree")
    tree.add("something").add("asdasd").add("asujiobdaisbdiasvbd")
    print(tree)

def live():
    # bitcoin live price
    import time

    from rich.live import Live
    from rich.table import Table

    table = Table()
    table.add_column("Row ID")
    table.add_column("Description")
    table.add_column("Level")

    with Live(table, refresh_per_second=4):  # update 4 times a second to feel fluid
        for row in range(12):
            time.sleep(0.01)  # arbitrary delay
            # update the renderable internally
            table.add_row(f"{row}", f"description {row}", "[red]ERROR")

    import time

    from rich.live import Live
    from rich.table import Table

    table = Table()
    table.add_column("Row ID")
    table.add_column("Description")
    table.add_column("Level")

    with Live(table, refresh_per_second=4) as live:  # update 4 times a second to feel fluid
        for row in range(12):
            live.console.print(f"Working on row #{row}")
            time.sleep(0.4)
            table.add_row(f"{row}", f"description {row}", "[red]ERROR")

def syntax_highlighting():
    from rich.console import Console
    from rich.syntax import Syntax

    my_code = '''
    def iter_first_last(values: Iterable[T]) -> Iterable[Tuple[bool, bool, T]]:
        """Iterate and generate a tuple with a flag for first and last value."""
        iter_values = iter(values)
        try:
            previous_value = next(iter_values)
        except StopIteration:
            return
        first = True
        for value in iter_values:
            yield first, False, previous_value
            first = False
            previous_value = value
        yield first, True, previous_value
    '''
    from pathlib import Path
    _path = Path(__file__)
    syntax = Syntax(_path.read_text(), "python", theme="solarized-dark", line_numbers=False)
    console = Console()
    console.print(syntax)

if __name__ == '__main__':
    syntax_highlighting()
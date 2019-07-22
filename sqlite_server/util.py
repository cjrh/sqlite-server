import pathlib
import inspect


def linetag():
    """Returns the current line number in our program."""
    target_frame = inspect.currentframe().f_back.f_back
    linenum = target_frame.f_lineno
    filename = pathlib.Path(target_frame.f_code.co_filename).name
    funcname = target_frame.f_code.co_name
    return f'{filename}:{funcname}:{linenum}'


def printl(*args, **kwargs):
    print(linetag(), *args, **kwargs)

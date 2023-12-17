"""
Helper module that counts functions execution time,
compare results from different executions or with answer,
filter tests that meet the criteria and show the execution results.
"""
import time
from copy import deepcopy
from typing import Callable, Any, Optional, Union

__reference = None


class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    GREY = '\033[90m'


def __render(test, func_name, result, reference, timedelta, equal=True,
             skipped=False):
    def shrink(value):
        max_len = 20
        sorted_types = [list, tuple, set, range]
        if type(value) in sorted_types and len(value) > max_len:
            if type(value) is set:
                value = list(value)
            return value[:max_len]
        else:
            return value

    result = shrink(result)
    reference = shrink(reference)
    test = shrink(test)
    test = tuple(shrink(item) for item in test)

    if not skipped:
        print(f'{round(timedelta, 2):6}s '
              f'{Style.GREEN}{"OK" if equal else ""}{Style.RESET}'
              f'{Style.RED}{"ER" if not equal else ""}{Style.RESET}'
              f'{Style.YELLOW} {func_name}{Style.RESET}'
              f'{Style.GREY} ref:{Style.RESET}{reference}'
              f'{Style.GREY} res:{Style.RESET}{result} '
              f'{Style.GREY} input:{test}{Style.RESET}')
    else:
        print(f'   ---s'
              f'{Style.CYAN} SK {Style.RESET}'
              f'{Style.YELLOW}{func_name}{Style.RESET}'
              f'{Style.GREY} execution skipped. {Style.RESET}')


def __compare(reference: Any, result: Any) -> bool:
    if reference == result:
        return True
    sorted_types = [list, tuple, range, set]
    if type(reference) in sorted_types and type(result) in sorted_types and len(
            reference) == len(result):
        reference = deepcopy(reference)
        result = deepcopy(result)
        try:
            if type(reference) is set:
                reference = list(reference)
            if type(result) is set:
                result = list(result)
            if type(reference[0]) in sorted_types and type(
                    result[0]) in sorted_types:
                reference = [sorted(i) for i in reference]
                result = [sorted(i) for i in result]
        except (TypeError, IndexError):
            pass
        try:
            reference = sorted(reference)
            result = sorted(result)
        except TypeError:
            pass
        return reference == result
    else:
        return False


def execute(
        func: Callable,
        test: Union[list, tuple],
        reference: Any = None,
        include_func: Optional[Callable] = None,
        is_reference: bool = False):
    """
    Executes function, if include function not specified or its result with test
    argument is True. Stores result as a reference for other invocations
    if is_reference = True. Compares result with reference if is_reference
    is not specified. Prints result to command line.
    Args:
        func: function (leetcode problem solution) to execute.
        test: list of arguments for given function.
        reference: you can specify reference to compare for execution
        include_func: boolean function that returns result from test argument
                      (to skip functions with long run times)
        is_reference: saving result as reference for other invocations if True
    """
    if not include_func or include_func(test):
        global __reference
        time_start = time.time()
        result = func(*test)
        timedelta = time.time() - time_start
        if is_reference:
            __reference = reference if reference else deepcopy(result)
        is_results_equal = __compare(reference if reference else __reference,
                                     result)
        __render(test, func.__name__, result, __reference, timedelta,
                 is_results_equal)
    else:
        __render(test, func.__name__, None, None, None, False, skipped=True)

def log(filename=None):
    def wrapper(function):
        def inner(*args, **kwargs):
            function_name = function.__name__
            start_message = f"{function_name} start"
            try:
                result = function(*args, **kwargs)
                result_function = f"{function_name} ok"
                return result
            except Exception as e:
                result_function = (
                    f"{function_name} error: тип ошибки. {type(e).__name__}: {e}. Inputs = {args}, {kwargs}"
                )
                raise e
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(start_message + "\n")
                        f.write(result_function + "\n")
                else:
                    print(start_message)
                    print(result_function)

        return inner

    return wrapper

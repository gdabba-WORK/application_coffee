class NameErrorr(BaseException):
    pass


def my_exception_handle():
    try:
        print("try()")
        raise NameErrorr
        print("try() end")
    except NameErrorr:
        print(NameErrorr)
    finally:
        print("finally()")


if __name__ == "__main__":
    my_exception_handle()
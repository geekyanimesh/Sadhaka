class InvalidMarksError(Exception):
    pass


def calculate_marks(marks):

    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100")

    return marks


try:
    print(calculate_marks(150))

except InvalidMarksError as e:
    print("Error:", e)
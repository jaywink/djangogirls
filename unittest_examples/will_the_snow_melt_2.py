# -*- coding: utf-8 -*-
def parse_integer(string_in):
    """Return an integer from a string or else None."""
    if isinstance(string_in, str):
        string_in = string_in.strip()
    try:
        return int(string_in)
    except ValueError:
        return False # We decide that we'd prefer to return False here.


def will_the_snow_melt_today(temperature_string):
    """Tell the user whether the snow will melt today."""
    temperature_integer = parse_integer(temperature_string)

    if temperature_integer is None:
        return "I don't know what that means!"

    if temperature_integer > 3:
        return "It probably will."
    return "Nope! It's here to stay."


if __name__ == '__main__':
    print("Will the snow melt today?")
    print(will_the_snow_melt_today(input("Type the current temperature: ")))
##  Let's start with two simple functions
    
    def parse_integer(string_in):
        """Return an integer from a string or else None."""
        try:
            return int(string_in)
        except ValueError:
            return None
    
    def will_the_snow_melt_today(temperature_string):
        """Tell the user whether the snow will melt today."""
        temperature_integer = parse_integer(temperature_string)
    
        if temperature_integer is None:
            return "I don't know what that means!"
    
        if temperature_integer > 3:
            return "It probably will."
        return "Nope! It's here to stay."
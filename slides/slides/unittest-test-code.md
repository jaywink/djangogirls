## Meet the unittest library

    import unittest
    from will_the_snow_melt import will_it_snow_today
    
    
    class TestWillTheSnowMelt(unittest.TestCase):
        def test_snow_melts_above_three_degrees(self):
            answer = will_it_snow_today('5')
            self.assertEqual("It probably will.", answer)
    
        def test_snow_does_not_melt_below_three_degrees(self):
            answer = will_it_snow_today('0')
            self.assertEqual("Nope! It's here to stay.", answer)
    
        def test_non_number_confuses_the_function(self):
            answer = will_it_snow_today('lumi')
            self.assertEqual("I don't know what that means!", answer)
    
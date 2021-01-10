class Temperature:
    def ktoc(kelvin):
        """
        Convert kelvin to celcius
        """
        return int(round(kelvin - 273.15, 0))
    def ktof(kelvin):
        """
        Convert kelvin to fahrenheit
        """
        return int(round((((kelvin-273.15)*9)/5)+32, 0))

class Pressure:
    def hpatoinhg(hpa):
        """
        Convert hpa to inches Hg
        """
        return round(hpa*0.02953, 2)

class Speed:
    def mpstomph(meterspersecond):
        """
        Convert meters per second to miles per hour
        """
        return int(round(meterspersecond*2.2369, 0))
    def mpstoknot(mps):
        """
        Convert meters per second to knots
        """
        return int(round(mps*1.9438, 0))

class Length:
    def mmtoin(mm):
        """
        Convert millimeters to inches
        """
        return round(mm*0.03937,1)
    def mtosm(m):
        "Convert meters to statute miles"
        return round(m/1609.344, 1)
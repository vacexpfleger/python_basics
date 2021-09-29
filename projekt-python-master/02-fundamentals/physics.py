'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.807 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''

def earth_gravity_force(weight):
    """
    This function calculates
    how much gravity force you're pulled by on Earth
    """
    force = EARTH_GRAVITY * weight
    return force

def moon_gravity_force(weight):
    """
    This function calculates
    how much gravity you're pulled by on Moon
    """
    force = MOON_GRAVITY * weight
    return force

def object_time(distance):
    """
    This function calculates
    the time it takes for you to hear a sound source from a certain distance
    """
    time = distance/SPEED_OF_SOUND
    return time

def object_lightspeed(index):
    """
    This function calculates
    the speed of light given by a refraction index
    """
    speed = SPEED_OF_LIGHT/index
    return speed
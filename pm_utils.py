import math

def particle_count_to_pm(particle_count: float) -> float:
    """From a particle count per 0.01 cubic feet, calculate
    the estimated mass of PM2.5 in ug/m^3.

    Args:
        particle_count (float): Particle count per 0.01 cubic feet of air

    Returns:
        float: ug/m^3 of PM
    """
    particle_count = particle_count/0.0002831685 ## ratio of 0.01 cubic feet to cubic meter
    # expected particle mass = volume of a spherical particle with 1.75um diameter * unit density
    particle_volume = math.pi/6 * math.pow(1.75,3) # volume in cubic micrometers
    particle_density = 1.0 # 1 gram/cubic centimeter, want micrograms/cubic micrometer
    particle_density = particle_density/1000000 # 1e6 micrograms/1e12 cubic micrometers/cubic cm
    particle_mass = particle_density * particle_volume
    return particle_count * particle_mass

def pm_aqi(pm_measure: float)-> int:
    """Return the AQI for the measured pm2.5
    Based on method published here: https://www.airnow.gov/sites/default/files/2020-05/aqi-technical-assistance-document-sept2018.pdf

    Args:
        pm_measure (float): pm2.5 in micrograms/cubic meter. We reccommend taking a longer term  average
        here. This function only makes a point calculation

    Returns:
        float: AQI for measured PM
    """
    pm_measure = math.floor(pm_measure*10)/10 # truncate to 1 decimal place
    if pm_measure <= 12.0:
        return pm_aqi_breakpoint(pm_measure, 12.0, 0, 50, 0)
    elif pm_measure <= 35.4:
        return pm_aqi_breakpoint(pm_measure,35.4,12.1,100,51)
    elif pm_measure <= 55.4:
        return pm_aqi_breakpoint(pm_measure, 55.4,35.5,150,101)
    elif pm_measure <= 150.4:
        return pm_aqi_breakpoint(pm_measure, 150.4,55.5,200,151)
    elif pm_measure <= 250.4:
        return pm_aqi_breakpoint(pm_measure,250.4,150.5,300,201)
    elif pm_measure <= 500.4:
        return pm_aqi_breakpoint(pm_measure,500,5,250.5,500,301)
    else:
        return 501 # beyond the AQI

def pm_aqi_breakpoint(pm, bp_high, bp_low, index_high, index_low):
    index = ((index_high - index_low)/(bp_high - bp_low))*(pm - bp_low) + index_low
    if index - math.floor(index) > 0.5:
        return math.ceil(index)
    else:
        return math.floor(index)
    
def particle_count_to_aqi(particle_count: float) -> int:
    pm_measure = particle_count_to_pm(particle_count)
    aqi = pm_aqi(pm_measure)
    return aqi


def main():
    print(particle_count_to_pm(2095.35))
    print(particle_count_to_aqi(2095.35))

if __name__ == "__main__":
    main()
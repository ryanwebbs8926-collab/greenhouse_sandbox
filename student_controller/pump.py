"""Pump control for the GHU-2 greenhouse (percent speed, 0 to 100).

Owner: <Ryan Weber>
"""
from .helpers import _clamp

def control_pump(readings, setpoints, dt, state) -> float:
    soil_readings = readings.soil_vwc()
    hum_readings = readings.rh_pct()

    if soil_readings < 0.3 and hum_readings <0.6:
        output = 100
    elif soil_readings < 0.2:
        output = 100
    else:
        output = 0
    return _clamp(output, 0.0, 100.0)
    
    """Return the pump speed for this tick, a number in [0, 100].

    Parameters
    ----------
    readings : SensorReadings
        temperature_c, rh_pct, co2_ppm_primary (K30), co2_ppm_backup (SCD41),
        soil_vwc, par_umol_m2_s.
    setpoints : Setpoints
        temperature_c (day and night aware), co2_ppm, rh_pct, soil_vwc,
        is_daytime.
    dt : float
        The length of this tick in seconds (60 by default).
    state : dict
        A plain dictionary you may use to remember values between ticks.
        All four actuator files share this one dictionary, so start every
        key you use with this file's name (for example, state["pump_total"]).
        Two files that both write state["total"] overwrite each other.

    Returns
    -------
    float
        Pump speed percent, from 0 to 100.
    """
    # TODO: Replace this stub with your Milestone 3 pump design.
    # Your M3 flowchart is the specification. Keep each command in range
    # before you return it:
    #   1. At the top of this file, add "from .helpers import _clamp".
    #   2. Return "_clamp(u, 0.0, 100.0)", where u is your command.
    

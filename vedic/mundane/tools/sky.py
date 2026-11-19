"""Snapshot of the sky for a mundane log entry.

Usage: python3 sky.py 2026-11-19 [hour_utc]

Prints tropical and sidereal (Lahiri, linear approximation) positions,
retrograde flags, aspects between Mars and the slower planets, and the
mean node. Needs skyfield; downloads de421.bsp on first run.
"""
import sys
from skyfield.api import load
from skyfield.framelib import ecliptic_frame

ts = load.timescale()
eph = load('de421.bsp')
earth = eph['earth']
SIGNS = 'Ari Tau Gem Can Leo Vir Lib Sco Sag Cap Aqu Pis'.split()
BODIES = {'Sun': 'sun', 'Moon': 'moon', 'Mercury': 'mercury', 'Venus': 'venus',
          'Mars': 'mars barycenter', 'Jupiter': 'jupiter barycenter',
          'Saturn': 'saturn barycenter', 'Uranus': 'uranus barycenter',
          'Neptune': 'neptune barycenter', 'Pluto': 'pluto barycenter'}


def fmt(x):
    return f"{SIGNS[int(x // 30)]} {int(x % 30):02d}°{int(x % 1 * 60):02d}'"


def lon(t, body):
    return earth.at(t).observe(eph[body]).apparent().frame_latlon(ecliptic_frame)[1].degrees


def ayanamsa(t):
    # Lahiri, linear fit calibrated against AstroSage to about 0.01 degrees
    return 23.85292 + 0.0139689 * ((t.tt - 2451545) / 365.25) - 0.0067


def mean_node(t):
    T = (t.tt - 2451545) / 36525
    return (125.0445479 - 1934.1362891 * T + 0.0020754 * T * T) % 360


def main():
    y, m, d = map(int, sys.argv[1].split('-'))
    h = float(sys.argv[2]) if len(sys.argv) > 2 else 12
    t = ts.utc(y, m, d, h)
    ay = ayanamsa(t)
    pos = {}
    for name, body in BODIES.items():
        x = lon(t, body)
        speed = (lon(ts.tt_jd(t.tt + 0.5), body) - lon(ts.tt_jd(t.tt - 0.5), body) + 540) % 360 - 180
        pos[name] = x
        print(f"{name:8s} trop {fmt(x)}  sid {fmt((x - ay) % 360)} {'R' if speed < 0 else ' '} {speed:+.3f}°/day")
    pos['Rahu'] = mean_node(t)
    print(f"{'Rahu':8s} trop {fmt(pos['Rahu'])}  sid {fmt((pos['Rahu'] - ay) % 360)}  (Ketu opposite)")
    print('--- aspects within 3° (Mars and slower, plus the Sun)')
    names = [n for n in pos if n not in ('Moon', 'Mercury', 'Venus')]
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            sep = abs((pos[a] - pos[b] + 180) % 360 - 180)
            for ang in (0, 60, 90, 120, 180):
                if abs(sep - ang) < 3:
                    print(f"{a}–{b} {ang}° orb {sep - ang:+.2f}")


if __name__ == '__main__':
    main()

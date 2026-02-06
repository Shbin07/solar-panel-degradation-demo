import numpy as np
import matplotlib.pyplot as plt


def radiation_term_per_year(alt_km: float) -> float:
    """
    Very simple altitude-dependent radiation degradation model (fraction per year).
    """
    alt_min, alt_max = 400.0, 700.0
    rad_min, rad_max = 0.004, 0.010  # 0.4%/yr to 1.0%/yr

    alt_clamped = float(np.clip(alt_km, alt_min, alt_max))
    return rad_min + (rad_max - rad_min) * (alt_clamped - alt_min) / (alt_max - alt_min)


def simulate_relative_power(
    years: int,
    alt_km: float,
    constant_deg_per_year: float = 0.005,
):
    t = np.arange(0, years + 1)
    rel = np.ones_like(t, dtype=float)

    yearly_deg = constant_deg_per_year + radiation_term_per_year(alt_km)

    for i in range(1, len(t)):
        rel[i] = rel[i - 1] * (1.0 - yearly_deg)

    return t, rel


def main():
    years = 10
    altitudes = [400, 700]

    for alt in altitudes:
        t, rel = simulate_relative_power(years, alt)
        plt.plot(t, rel, label=f"{alt} km")

    plt.title("Simplified Solar Array Degradation in LEO")
    plt.xlabel("Mission time (years)")
    plt.ylabel("Relative power (P/P0)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

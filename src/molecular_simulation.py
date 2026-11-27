"""Forward physical simulation of Raman spectra for Graphene, SWCNTs, and Graphene/h-BN heterostructures."""

import numpy as np
from src.raman_physics import (
    C_CGS, H_PLANCK, K_BOLTZMANN, laser_wavelength_to_wavenumber,
    stokes_anti_stokes_ratio, swcnt_diameter_from_chiral, swcnt_is_metallic,
    swcnt_rbm_wavenumber, graphene_2d_dispersion, laser_wavelength_to_energy_ev
)
from src.peak_analysis import lorentzian, gaussian, bwf


class MolecularRamanSimulator:
    """Simulates Raman spectra from harmonic oscillator modes, polarizability derivatives, and line broadening."""

    def __init__(self, laser_wavelength_nm: float = 532.0, temperature_k: float = 300.0,
                 instrument_fwhm_cm1: float = 2.0):
        self.laser_nm = laser_wavelength_nm
        self.temp_k = temperature_k
        self.laser_wn = laser_wavelength_to_wavenumber(laser_wavelength_nm)
        self.laser_ev = laser_wavelength_to_energy_ev(laser_wavelength_nm)
        self.inst_fwhm = instrument_fwhm_cm1

    def build_spectrum_from_modes(self, wavenumber_grid: np.ndarray, modes: list) -> np.ndarray:
        """Sum spectral contributions of defined phonon modes over wavenumber_grid.
        
        Each mode dict contains:
            'center': float,
            'fwhm': float (intrinsic vibrational damping),
            'activity': float (proportional to |dalpha/dQ|^2),
            'profile': 'lorentzian' | 'gaussian' | 'bwf',
            'q': float (optional, for BWF).
        """
        spectrum = np.zeros_like(wavenumber_grid, dtype=float)
        for m in modes:
            center = m["center"]
            intrinsic_gamma = m["fwhm"] / 2.0
            total_gamma = np.sqrt(intrinsic_gamma**2 + (self.inst_fwhm / 2.0)**2)
            amp = m["activity"]
            profile = m.get("profile", "lorentzian")

            if profile == "lorentzian":
                spectrum += lorentzian(wavenumber_grid, center, total_gamma, amp)
            elif profile == "gaussian":
                sigma = total_gamma / np.sqrt(2.0 * np.log(2.0))
                spectrum += gaussian(wavenumber_grid, center, sigma, amp)
            elif profile == "bwf":
                q = m.get("q", -4.5)
                spectrum += bwf(wavenumber_grid, center, total_gamma, amp, q)
        return spectrum

    def simulate_graphene(self, wavenumber_grid: np.ndarray, sample_type: str = "monolayer") -> dict:
        """Simulate Graphene Raman spectrum (monolayer, bilayer, defective)."""
        w_2d = graphene_2d_dispersion(self.laser_ev, base_2d_cm1=2684.8)

        if sample_type == "monolayer":
            modes = [
                {"center": 1582.4, "fwhm": 13.0, "activity": 3200.0, "profile": "lorentzian", "assignment": "G (E2g)"},
                {"center": w_2d, "fwhm": 25.0, "activity": 8800.0, "profile": "lorentzian", "assignment": "2D (two-phonon iTO)"},
            ]
        elif sample_type == "bilayer":
            modes = [
                {"center": 1581.8, "fwhm": 14.0, "activity": 3500.0, "profile": "lorentzian", "assignment": "G (E2g)"},
                {"center": w_2d - 32.0, "fwhm": 24.0, "activity": 1800.0, "profile": "lorentzian", "assignment": "2D_11"},
                {"center": w_2d - 4.5, "fwhm": 23.0, "activity": 2900.0, "profile": "lorentzian", "assignment": "2D_12"},
                {"center": w_2d + 15.5, "fwhm": 23.5, "activity": 2800.0, "profile": "lorentzian", "assignment": "2D_21"},
                {"center": w_2d + 39.0, "fwhm": 24.5, "activity": 1750.0, "profile": "lorentzian", "assignment": "2D_22"},
            ]
        elif sample_type == "defective":
            modes = [
                {"center": 1348.0, "fwhm": 26.0, "activity": 2800.0, "profile": "lorentzian", "assignment": "D (defect A1g)"},
                {"center": 1583.5, "fwhm": 16.5, "activity": 3100.0, "profile": "lorentzian", "assignment": "G (E2g)"},
                {"center": 1621.5, "fwhm": 13.0, "activity": 480.0, "profile": "lorentzian", "assignment": "D' (intravalley defect)"},
                {"center": w_2d, "fwhm": 36.0, "activity": 4200.0, "profile": "lorentzian", "assignment": "2D"},
                {"center": 2942.0, "fwhm": 42.0, "activity": 520.0, "profile": "lorentzian", "assignment": "D+D' combination"},
            ]
        else:
            raise ValueError(f"Unknown graphene sample type: {sample_type}")

        intensity = self.build_spectrum_from_modes(wavenumber_grid, modes)
        return {"wavenumber": wavenumber_grid, "intensity": intensity, "modes": modes}

    def simulate_swcnt(self, wavenumber_grid: np.ndarray, n: int = 10, m: int = 10) -> dict:
        """Simulate Single-Walled Carbon Nanotube Raman spectrum for given chiral indices (n, m)."""
        d_t = swcnt_diameter_from_chiral(n, m)
        is_metal = swcnt_is_metallic(n, m)
        w_rbm = swcnt_rbm_wavenumber(d_t)

        if is_metal:
            modes = [
                {"center": w_rbm, "fwhm": 6.5, "activity": 4500.0, "profile": "lorentzian", "assignment": f"RBM ({n},{m}) d={d_t:.2f}nm"},
                {"center": 1342.0, "fwhm": 25.0, "activity": 320.0, "profile": "lorentzian", "assignment": "D"},
                {"center": 1548.0, "fwhm": 32.0, "activity": 1850.0, "profile": "bwf", "q": -4.5, "assignment": "G- (circumferential BWF)"},
                {"center": 1592.0, "fwhm": 14.0, "activity": 4200.0, "profile": "lorentzian", "assignment": "G+ (axial LO)"},
                {"center": 2665.0, "fwhm": 35.0, "activity": 2100.0, "profile": "lorentzian", "assignment": "2D (G')"},
            ]
        else:
            modes = [
                {"center": w_rbm, "fwhm": 5.5, "activity": 3800.0, "profile": "lorentzian", "assignment": f"RBM ({n},{m}) d={d_t:.2f}nm"},
                {"center": 1345.0, "fwhm": 22.0, "activity": 260.0, "profile": "lorentzian", "assignment": "D"},
                {"center": 1568.0, "fwhm": 12.0, "activity": 1600.0, "profile": "lorentzian", "assignment": "G- (circumferential TO)"},
                {"center": 1591.5, "fwhm": 10.0, "activity": 3950.0, "profile": "lorentzian", "assignment": "G+ (axial LO)"},
                {"center": 2674.0, "fwhm": 29.0, "activity": 2400.0, "profile": "lorentzian", "assignment": "2D (G')"},
            ]

        intensity = self.build_spectrum_from_modes(wavenumber_grid, modes)
        return {
            "wavenumber": wavenumber_grid,
            "intensity": intensity,
            "diameter_nm": d_t,
            "is_metallic": is_metal,
            "chirality": (n, m),
            "modes": modes
        }

    def simulate_graphene_hbn(self, wavenumber_grid: np.ndarray) -> dict:
        """Simulate Graphene on hexagonal Boron Nitride (h-BN) van der Waals heterostructure.
        
        Features sharp h-BN E2g optical mode at 1366.8 cm^-1 and ultra-narrow Graphene 2D peak.
        """
        modes = [
            {"center": 1366.8, "fwhm": 9.0, "activity": 2200.0, "profile": "lorentzian", "assignment": "h-BN E2g optical phonon"},
            {"center": 1582.8, "fwhm": 13.5, "activity": 3100.0, "profile": "lorentzian", "assignment": "Graphene G (E2g)"},
            {"center": 2680.5, "fwhm": 17.5, "activity": 9900.0, "profile": "lorentzian", "assignment": "Graphene 2D (ultra-narrow)"},
        ]
        intensity = self.build_spectrum_from_modes(wavenumber_grid, modes)
        return {"wavenumber": wavenumber_grid, "intensity": intensity, "modes": modes}

    def simulate_temperature_series(self, wavenumber_grid: np.ndarray,
                                   temperatures: list = [100.0, 300.0, 500.0, 800.0]) -> dict:
        """Simulate Stokes and anti-Stokes intensities across varying temperatures."""
        nu_g = 1582.0
        results = {}
        for T in temperatures:
            r_as_s = stokes_anti_stokes_ratio(nu_g, self.laser_nm, T)
            gamma_t = 12.0 * (1.0 + 0.5 * (T / 300.0)**1.2)
            i_stokes = lorentzian(wavenumber_grid, nu_g, gamma_t / 2.0, 3200.0)
            i_anti = lorentzian(wavenumber_grid, -nu_g, gamma_t / 2.0, 3200.0 * r_as_s)
            results[T] = {
                "ratio_anti_to_stokes": float(r_as_s),
                "fwhm_cm1": float(gamma_t),
                "stokes_curve": i_stokes,
                "anti_stokes_curve": i_anti,
            }
        return results

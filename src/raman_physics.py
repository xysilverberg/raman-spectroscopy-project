"""Theoretical physics foundations of Raman scattering, molecular vibrations, selection rules, and dispersion relations."""

import numpy as np

C_SI = 299792458.0
C_CGS = 2.99792458e10
H_PLANCK = 6.62607015e-34
H_BAR = H_PLANCK / (2.0 * np.pi)
K_BOLTZMANN = 1.380649e-23
AMU_KG = 1.66053906660e-27
EV_TO_JOULE = 1.602176634e-19


def reduced_mass_diatomic(m1_amu: float, m2_amu: float) -> float:
    """Reduced mass in kilograms from atomic masses in unified atomic mass units (amu)."""
    mu_amu = (m1_amu * m2_amu) / (m1_amu + m2_amu)
    return mu_amu * AMU_KG


def harmonic_wavenumber(k_force_nm: float, mu_kg: float) -> float:
    """Calculate vibrational wavenumber in cm^-1 from force constant k (N/m) and reduced mass mu (kg)."""
    omega = np.sqrt(k_force_nm / mu_kg)
    nu_bar = omega / (2.0 * np.pi * C_CGS)
    return nu_bar


def force_constant_from_wavenumber(nu_bar_cm1: float, mu_kg: float) -> float:
    """Calculate harmonic force constant in N/m from wavenumber in cm^-1 and reduced mass mu (kg)."""
    omega = 2.0 * np.pi * C_CGS * nu_bar_cm1
    k = mu_kg * (omega**2)
    return k


def laser_wavelength_to_wavenumber(wavelength_nm: float) -> float:
    """Convert laser wavelength in nm to excitation wavenumber in cm^-1."""
    return 1e7 / wavelength_nm


def laser_wavelength_to_energy_ev(wavelength_nm: float) -> float:
    """Convert laser wavelength in nm to photon energy in eV."""
    return (H_PLANCK * C_SI / (wavelength_nm * 1e-9)) / EV_TO_JOULE


def stokes_anti_stokes_ratio(nu_v_cm1: float, laser_wavelength_nm: float, temp_k: float) -> float:
    """Calculate theoretical anti-Stokes to Stokes intensity ratio at temperature temp_k (K).
    
    Includes Boltzmann thermal factor and scattered photon frequency quartic factor:
    I_AS / I_S = ((nu_0 + nu_v)/(nu_0 - nu_v))^4 * exp(- h * c * nu_v / (k_B * T))
    """
    nu_0 = laser_wavelength_to_wavenumber(laser_wavelength_nm)
    freq_factor = ((nu_0 + nu_v_cm1) / (nu_0 - nu_v_cm1))**4
    energy_joule = H_PLANCK * C_CGS * nu_v_cm1
    boltzmann_factor = np.exp(-energy_joule / (K_BOLTZMANN * temp_k))
    return freq_factor * boltzmann_factor


def swcnt_diameter_from_chiral(n: int, m: int, a_cc: float = 0.142) -> float:
    """Calculate Single-Walled Carbon Nanotube diameter in nm from chiral indices (n, m).
    
    Lattice constant a = sqrt(3) * a_cc = 0.246 nm.
    """
    a = np.sqrt(3.0) * a_cc
    c_h = a * np.sqrt(n**2 + n * m + m**2)
    diameter = c_h / np.pi
    return diameter


def swcnt_is_metallic(n: int, m: int) -> bool:
    """Determine if SWCNT is metallic based on chiral indices condition (2n + m) mod 3 == 0."""
    return (2 * n + m) % 3 == 0


def swcnt_rbm_wavenumber(diameter_nm: float, a_const: float = 227.0, b_const: float = 14.0) -> float:
    """Radial Breathing Mode (RBM) wavenumber in cm^-1 from tube diameter: omega_RBM = A/d_t + B."""
    return (a_const / diameter_nm) + b_const


def graphene_2d_dispersion(laser_energy_ev: float, base_2d_cm1: float = 2684.8,
                           ref_laser_energy_ev: float = 2.3305,
                           dispersion_slope: float = 100.0) -> float:
    """Double resonance dispersion of Graphene 2D band with laser excitation energy (domega/dE ~ 100 cm^-1/eV)."""
    return base_2d_cm1 + dispersion_slope * (laser_energy_ev - ref_laser_energy_ev)


def grating_diffraction_angle(wavelength_nm: float, incident_angle_deg: float,
                              groove_density_per_mm: float = 1800.0, order: int = 1) -> float:
    """Grating equation: m * lambda = d * (sin(theta_i) + sin(theta_d)). Returns theta_d in degrees."""
    d_nm = 1e6 / groove_density_per_mm
    theta_i_rad = np.radians(incident_angle_deg)
    sin_theta_d = (order * wavelength_nm / d_nm) - np.sin(theta_i_rad)
    if np.abs(sin_theta_d) > 1.0:
        raise ValueError(f"Diffraction condition unphysical: sin(theta_d) = {sin_theta_d:.4f}")
    return np.degrees(np.arcsin(sin_theta_d))

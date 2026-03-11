# Radar Signal Processing & Interferometry Analysis

This project presents the analysis of radar measurement data using signal processing techniques and interferometry. The study focuses on processing RAW radar data from multi-antenna systems to analyze spectral characteristics, perform signal integration, compute cross-spectra, and estimate the Angle of Arrival (AOA) of received signals.

The project was developed as part of the **Telecommunication Engineering course** at **Hochschule Wismar – University of Applied Sciences (Germany)**.

---

## Project Objective

The primary objective of this project is to analyze radar signals received by multiple antennas and estimate signal characteristics such as:

- Signal spectra
- Cross-spectral phase relationships
- Echo power distribution
- Angle-of-Arrival (AOA)
- Sensor array coverage for interferometry

The analysis is implemented using scientific computing tools in **Python**.

---

## Radar Systems Used

### Saura Radar System
- Uses an array beam consisting of **4 individual antennas**
- Used to analyze spectral properties and signal superposition.

### MAARSY Radar System
- Uses **3 subarrays forming a beam**
- Used for interferometric processing and Angle-of-Arrival estimation.

---

## Implemented Tasks

### Task 1 – Spectral Analysis
Magnitude and phase spectra were generated for different receiver channels to study the frequency characteristics of the radar signals.

Key analysis:
- Magnitude spectrum
- Phase spectrum
- Frequency–range visualization

---

### Task 2 – Signal Combination
Two signal combination methods were compared:

1. **Superposition of time series signals** (receiver channels 2–5)
2. **Combination of individual spectra**

This comparison helps understand how different signal processing methods influence spectral characteristics.

---

### Task 3 – Signal Integration
Non-Coherent Integration (NCI) was applied to improve signal detection and reduce noise in spectral analysis.

Spectra were analyzed for multiple receiver channels after integration.

---

### Task 4 – Cross-Spectral Analysis
Cross-spectra between receiver channels were computed to analyze phase relationships between signals received at different antennas.

Outputs include:
- Cross-spectrum magnitude
- Cross-spectrum phase

This step is essential for interferometric processing.

---

### Task 5 – MAARSY Radar Data Processing
RAW radar data from MAARSY was processed to generate:

- Magnitude spectra
- Phase spectra
- Cross-spectra between receiver channels

This task extends the spectral analysis to another radar system.

---

### Task 6 – Echo Power and Angle-of-Arrival Estimation

Echo power was calculated for individual receivers and combined antenna signals.

Using interferometric phase differences between antennas, the **Angle of Arrival (AOA)** of the signal was estimated in terms of:

- Azimuth angle (φ)
- Elevation angle (θ)

---

### Task 7 – Sensor Array Simulation

Different antenna array configurations were simulated to evaluate coverage area for AOA estimation.

Simulated sensor layouts include:

- Circular array
- Spiral array
- Random array

Coverage areas were analyzed to evaluate performance of each array geometry.

---

## Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib
- Signal Processing (FFT, Spectral Analysis, Integration)
- Interferometric Phase Analysis

---

## Project Structure

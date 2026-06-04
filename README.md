# Aiding System For Visually Impaired Individuals

**"Enhanced Mobility Device with Proximity Sensors Technology"**

*Tsotlhe Seiphepi, Adamu Murtala Zungeru, Jwaone Gaboitaolelwe*  
Department of Electrical, Computer and Telecommunications Engineering  
Botswana International University of Science and Technology — Palapye, Botswana


## Tech Stack

![LaTeX](https://img.shields.io/badge/LaTeX-008080?style=for-the-badge&logo=latex&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tinkercad](https://img.shields.io/badge/Tinkercad-1477D1?style=for-the-badge&logo=autodesk&logoColor=white)
![Proteus](https://img.shields.io/badge/Proteus_8-00A99D?style=for-the-badge&logo=protel&logoColor=white)

| Tool | Purpose |
|---|---|
| **LaTeX / IEEEtran** | Research paper typesetting |
| **Proteus 8** | Circuit simulation |
| **Tinkercad** | 3D circuit prototyping |
| **Python** | Figure extraction scripts |

---

## Overview

This repository contains the research paper, LaTeX source, and all extracted figures for the
**Enhanced Mobility Device** — a proximity-sensor-based walking stick designed to assist
visually impaired individuals in navigating their environments safely and independently.

The device integrates HC-SR04 ultrasonic proximity sensors and NE555 timers into a handheld
rechargeable stick. It detects obstacles at two range thresholds (1 m and 3 m) and provides
haptic (DC motor vibration) and auditory (piezoelectric buzzer) feedback.

---


## Repository Structure

```
aiding-system-visually-impaired/
├── paper/
│   ├── main.tex              # Full LaTeX source of the paper
│   ├── references.bib        # BibTeX bibliography
│   └── figures/              # All figures extracted from the original PDF
│       ├── fig01_block_diagram.png
│       ├── fig02_flowchart.png
│       ├── fig03_power_supply.png
│       ├── fig04a_hcsr04_sensor.jpeg
│       ├── fig04b_sensory_circuit.png
│       ├── fig05_timing_circuit.png
│       ├── fig06_timing_circuit_diagram.png
│       ├── fig07_oscilloscope_ne555.jpeg
│       ├── fig08_dac_circuit.png
│       ├── fig09_oscilloscope_filter.jpeg
│       ├── fig10_comparator_3m.png
│       ├── fig11_comparator_1m.png
│       ├── fig13a_output_3m.png
│       ├── fig13b_output_1m.png
│       ├── fig14a_tinkercad_sensing.png
│       ├── fig14b_tinkercad_output.png
│       ├── fig14c_tinkercad_overview.png
│       ├── fig15_proteus_simulation.png
│       ├── fig16_offstate_voltages.png
│       ├── fig17_onstate_1m.png
│       └── fig18_onstate_3m.png
├── extract_images.py         # Script used to extract figures from the original PDF
├── rename_figures.py         # Script used to rename extracted figures
└── README.md
```

---

## System Design

The device consists of the following subsystems:

| Subsystem | Component | Function |
|---|---|---|
| Power Supply | 9 V battery | Powers all sub-circuits |
| Sensing Circuit | HC-SR04 (ultrasonic) | Detects obstacles, range 2 cm – 400 cm |
| Timing Circuit | NE555 (astable mode) | Generates 250 Hz clock for continuous sampling |
| DAC Circuit | RC low-pass filter (R = 200 kΩ, C = 1 µF) | Converts digital sensor output to analogue voltage |
| Comparator Circuit | LM358 op-amp (×2) | Compares distance voltages against 3 m and 1 m thresholds |
| Output Circuit | Relay (NT72C), DC motor, piezo buzzer | Provides haptic and auditory feedback |

### Alert Logic

- **Object at ≤ 3 m:** buzzer activates
- **Object at ≤ 1 m:** buzzer + DC motor (vibration) activate

---

## Building the PDF

Requires a LaTeX distribution (TeX Live, MiKTeX, or MacTeX) with the IEEEtran bibliography style.

```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Or with `latexmk`:

```bash
cd paper
latexmk -pdf main.tex
```

---

## Keywords

Object Detection · Proximity Sensor (HC-SR04) · NE555 Timer · DC Motor · Assistive Technology · Visually Impaired

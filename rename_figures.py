import os
import shutil

figures_dir = r"C:\Users\tsotl\aiding-system-visually-impaired\paper\figures"

rename_map = {
    "fig_p3_1.png":   "fig01_block_diagram.png",
    "fig_p4_1.png":   "fig02_flowchart.png",
    "fig_p5_1.png":   "fig03_power_supply.png",
    "fig_p6_1.jpeg":  "fig04a_hcsr04_sensor.jpeg",
    "fig_p6_2.png":   "fig04b_sensory_circuit.png",
    "fig_p7_1.png":   "fig05_timing_circuit.png",
    "fig_p8_1.png":   "fig06_timing_circuit_diagram.png",
    "fig_p9_1.jpeg":  "fig07_oscilloscope_ne555.jpeg",
    "fig_p9_2.png":   "fig08_dac_circuit.png",
    "fig_p10_1.jpeg": "fig09_oscilloscope_filter.jpeg",
    "fig_p11_1.png":  "fig10_comparator_3m.png",
    "fig_p12_1.png":  "fig11_comparator_1m.png",
    "fig_p13_1.png":  "fig13a_output_3m.png",
    "fig_p13_2.png":  "fig13b_output_1m.png",
    "fig_p14_1.png":  "fig14a_tinkercad_sensing.png",
    "fig_p15_1.png":  "fig14b_tinkercad_output.png",
    "fig_p15_2.png":  "fig14c_tinkercad_overview.png",
    "fig_p16_1.png":  "fig15_proteus_simulation.png",
    "fig_p17_1.png":  "fig16_offstate_voltages.png",
    "fig_p18_1.png":  "fig17_onstate_1m.png",
    "fig_p18_2.png":  "fig18_onstate_3m.png",
}

for old, new in rename_map.items():
    src = os.path.join(figures_dir, old)
    dst = os.path.join(figures_dir, new)
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"Renamed: {old} -> {new}")
    else:
        print(f"Missing: {old}")

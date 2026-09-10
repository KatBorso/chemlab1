#the code produces the bar graph for the measurements lab
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# GRAPH 1: Graduated Cylinder - Water at 21°C
# ============================================================

volume_cylinder = np.array([10, 20, 30, 40], dtype=float)
mass_cylinder = np.array([52.2, 61.4, 72.5, 81.8], dtype=float)

# Calculate density from changes in mass and volume
density_cylinder = np.diff(mass_cylinder) / np.diff(volume_cylinder)

# Convert NumPy values to regular Python floats
density_cylinder = [float(x) for x in density_cylinder]

density_volumes_cylinder = [20, 30, 40]

# Average experimental density
avg_density_cylinder = float(np.mean(density_cylinder))

# True density of water at 21°C
true_density_cylinder = 0.9980

# Create graph
plt.figure(figsize=(8, 6))

plt.bar(
    density_volumes_cylinder,
    density_cylinder,
    width=7,
    color="steelblue",
    edgecolor="black",
    label="Experimental Density"
)

# Average line
plt.axhline(
    y=avg_density_cylinder,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average = {avg_density_cylinder:.3f} g/mL"
)

# True density line
plt.axhline(
    y=true_density_cylinder,
    color="green",
    linestyle="-",
    linewidth=2,
    label=f"True Density = {true_density_cylinder:.4f} g/mL"
)

plt.title("Density of Water Using Graduated Cylinder at 21°C")
plt.xlabel("Volume (mL)")
plt.ylabel("Density (g/mL)")
plt.xticks([20, 30, 40])
plt.ylim(0.7, 1.2)
plt.grid(axis="y", alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()


# ============================================================
# GRAPH 2: Beaker - Water at 22°C
# ============================================================

volume_beaker = np.array([10, 20, 30, 40], dtype=float)
mass_beaker = np.array([43.9, 53.8, 63.7, 73.5], dtype=float)

# Calculate density from changes in mass and volume
density_beaker = np.diff(mass_beaker) / np.diff(volume_beaker)

# Convert NumPy values to regular Python floats
density_beaker = [float(x) for x in density_beaker]

density_volumes_beaker = [20, 30, 40]

# Average experimental density
avg_density_beaker = float(np.mean(density_beaker))

# True density of water at 22°C
true_density_beaker = 0.9978

# Create graph
plt.figure(figsize=(8, 6))

plt.bar(
    density_volumes_beaker,
    density_beaker,
    width=7,
    color="darkorange",
    edgecolor="black",
    label="Experimental Density"
)

# Average line
plt.axhline(
    y=avg_density_beaker,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average = {avg_density_beaker:.3f} g/mL"
)

# True density line
plt.axhline(
    y=true_density_beaker,
    color="green",
    linestyle="-",
    linewidth=2,
    label=f"True Density = {true_density_beaker:.4f} g/mL"
)

plt.title("Density of Water Using Beaker at 22°C")
plt.xlabel("Volume (mL)")
plt.ylabel("Density (g/mL)")
plt.xticks([20, 30, 40])
plt.ylim(0.7, 1.2)
plt.grid(axis="y", alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()


# ============================================================
# PRINT RESULTS
# ============================================================

print("Graduated Cylinder - 21°C")
print("--------------------------------")

for volume, density in zip(density_volumes_cylinder, density_cylinder):
    print(f"{volume} mL: {density:.3f} g/mL")

print(f"Average density: {avg_density_cylinder:.3f} g/mL")
print(f"True density: {true_density_cylinder:.4f} g/mL")


print("\nBeaker - 22°C")
print("--------------------------------")

for volume, density in zip(density_volumes_beaker, density_beaker):
    print(f"{volume} mL: {density:.3f} g/mL")

print(f"Average density: {avg_density_beaker:.3f} g/mL")
print(f"True density: {true_density_beaker:.4f} g/mL")

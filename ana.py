import matplotlib.pyplot as plt

file_paths = [
    "tracenewt.txt",
    "tracemodift.txt"
]

timestamps = {
    "traceNew": [],
    "traceModif": []
}

for key, path in zip(timestamps.keys(), file_paths):
    with open(path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 2 and parts[1].replace('.', '', 1).isdigit():
                timestamps[key].append(float(parts[1]))

import numpy as np

def calculate_packets_over_time(timestamps, interval=1.0):
    """Calcule le nombre de paquets par intervalle de temps."""
    start_time = min(timestamps)
    end_time = max(timestamps)
    bins = np.arange(start_time, end_time, interval)
    packet_counts, _ = np.histogram(timestamps, bins=bins)
    return bins[:-1], packet_counts

results = {key: calculate_packets_over_time(value) for key, value in timestamps.items()}

results
plt.figure(figsize=(14, 8))

for key, (times, counts) in results.items():
    plt.plot(times, counts, label=f"Trace {key}")

plt.xlabel('Temps (s)')
plt.ylabel('Nombre de paquets')
plt.legend()

plt.savefig('ananewmodif.svg', format='svg')
plt.grid(True)
plt.show()
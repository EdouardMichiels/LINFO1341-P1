from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd

file_path = 'tracenewff.txt'

timestamps = []
protocols = []

with open(file_path, 'r') as file:
    for line in file:
        parts = line.split()
        if len(parts) > 4:
            try:
                time = float(parts[1])
                protocol = parts[4]
                timestamps.append(time)
                protocols.append(protocol)
            except ValueError:
                continue

df = pd.DataFrame({
    'Time': timestamps,
    'Protocol': protocols
})

protocol_counts = df['Protocol'].value_counts()

top_protocols = protocol_counts.nlargest(5).index
df_filtered = df[df['Protocol'].isin(top_protocols)]

plt.figure(figsize=(15, 8))
for protocol in top_protocols:
    subset = df_filtered[df_filtered['Protocol'] == protocol]
    plt.scatter(subset['Time'], subset['Protocol'], label=protocol, s=10)

plt.xlabel('Time (s)')
plt.ylabel('Protocol')
plt.legend()
plt.grid(True)


plt.savefig('protoplot.svg', format='svg')

plt.show(), protocol_counts

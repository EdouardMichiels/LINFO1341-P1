import matplotlib.pyplot as plt

labels = ['TCP', 'DNS', 'TLSv1.3', 'HTTP', 'SSDP', 'MDNS']
sizes = [321, 27, 98, 4, 12, 3]

fig, ax = plt.subplots()
ax.pie(sizes,  shadow=True, startangle=90)


plt.legend(labels, title="Protocoles", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
plt.savefig('camemplot.svg', format='svg')
plt.show()

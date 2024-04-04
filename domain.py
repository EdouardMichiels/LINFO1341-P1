import re
import matplotlib.pyplot as plt

fichier_path = 'tracenewff.txt'
with open(fichier_path, 'r') as file:
    data = file.read()

domains = re.findall(r'\b[\w.-]+(?:\.com|\.tech)\b', data)

domain_counts = {}
for domain in domains:
    domain_counts[domain] = domain_counts.get(domain, 0) + 1

filtered_domain_counts = {domain: count for domain, count in domain_counts.items() if count > 0}

labels, counts = zip(*filtered_domain_counts.items())

if labels and counts:
    plt.figure(figsize=(10, 8))
    plt.bar(labels, counts)
    plt.xlabel('Noms de domaine .com')
    plt.ylabel('Nombre d\'occurrences')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    plt.savefig('domainplot.svg', format='svg')
    plt.show()

else:
    print("Aucun nom de domaine .com trouvé plus d'une fois.")



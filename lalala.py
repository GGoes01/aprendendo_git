import matplotlib.pyplot as plt

# Coordenadas

x = [0, 1, .75, .25, 0]
y = [0, 0, 1, 1, 0]

# Plot

plt.figure(0, figsize=(8, 6))
plt.plot(x, y, color='purple', linewidth=3)
plt.title('Traprézio Roxo', fontsize='16')
plt.show()


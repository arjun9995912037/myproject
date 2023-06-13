import numpy as np
import matplotlib.pyplot as plt
# Baseband pulse shaping with raised cosine
dt = 0.01
n = np.arange(-20, 20, dt)
Nc = 4
t = np.arange(-Nc, Nc, dt) # Length of shaping cosine pulse
bt = np.arange(-1, 1, dt) # Two bit time
bl = bt.size - 1 # Two bit length
bitfill = np.zeros(int(1 / dt))
b1 = np.concatenate(([1], bitfill))
b0 = np.concatenate(([-1], bitfill))
bits = np.concatenate((b0, b1, b0, b0, b1, b1, b0, b0, b0, b1, b1, b1, b0, b0, b0, b0, b1, b1, b1,
b1, b1, b0, b0, b0, b0, b0, b0, b0, b0, b0, b1, b1, b1, b1, b1, b0, b0, b0, b0,
b0, b1, b1, b1, b0, b1, b0, b0, b0, b1, b0, b0, b1, b1, b1, b0, b1, b0, b1, b0)) # Bit stream
b = 0.25 # Beta value
ps = np.cos(np.pi * b * t) / (1 - (2 * b * t) ** 2) * np.sin(np.pi * t) / (np.pi * t) # Raised cosine function
ps[np.isnan(ps)] = 1
ps[np.isinf(ps)] = 0
baseband = np.convolve(bits, ps, mode="full")
# If noise is to be added, uncomment this part
# snr = 10 # dB
# baseband = np.random.randn(len(baseband)) + 1j * np.random.randn(len(baseband))
# baseband += 10 ** (-snr / 20) * (np.random.randn(len(baseband)) + 1j * np.random.randn(len(baseband)))
# baseband = baseband.real
plt.plot(t, ps)
plt.grid(True)
plt.show()
plt.plot(baseband)
plt.grid(True)
plt.show()
eyedia = np.empty((0, bl + 1))
r = 0
for i in range(Nc * (bl + 1), baseband.size - Nc * bl + 1, int(bl / 2 + 1)):
 # r = np.random.randint(bl // 4) # Uncomment if time jitter is required
 i += r
 eyedia = np.vstack((eyedia, baseband[i:i + bl + 1]))
 plt.plot(bt, eyedia.T)
 plt.title("Eye Diagram")
 plt.grid(True)
 plt.show()

import random, time

random.seed(42)

# TinyML dimensions: 8 features -> 16 hidden -> 5 classes
N, D, H, C = 100, 8, 16, 5

# Synthetic satellite sensor data (int8 quantized style)
X = [[random.randint(-64, 63) for _ in range(D)] for _ in range(N)]

# TinyML MLP weights (int8)
W1 = [random.randint(-64, 63) for _ in range(D * H)]
W2 = [random.randint(-64, 63) for _ in range(H * C)]
b1 = [0] * H
b2 = [0] * C

def relu(x):
    return x if x > 0 else 0

def forward(x, w1, w2):
    h = [0] * H
    for i in range(H):
        s = b1[i]
        base = i * D
        for j in range(D):
            s += x[j] * w1[base + j]
        h[i] = relu(s)
    o = [0] * C
    for i in range(C):
        s = b2[i]
        base = i * H
        for j in range(H):
            s += h[j] * w2[base + j]
        o[i] = s
    return o

def argmax(v):
    m, idx = v[0], 0
    for i in range(1, len(v)):
        if v[i] > m:
            m, idx = v[i], i
    return idx

# Clean labels
y = [argmax(forward(x, W1, W2)) for x in X]

def flip_bits(weights, prob):
    w = weights[:]
    for i in range(len(w)):
        if random.random() < prob:
            bit = random.randint(0, 7)
            u = (w[i] + 128) & 0xFF
            u ^= (1 << bit)
            w[i] = u - 128
    return w

def accuracy(w1, w2):
    c = 0
    for idx in range(N):
        if argmax(forward(X[idx], w1, w2)) == y[idx]:
            c += 1
    return c / N

print("ESP32-S3 SEU Fault Injection Baseline")
print("Samples:", N)
base = accuracy(W1, W2)
print("Baseline accuracy:", base)

rates = [0, 1e-5, 5e-5, 1e-4, 5e-4, 1e-3, 5e-3]
results = []
for r in rates:
    t0 = time.ticks_ms()
    w1f = flip_bits(W1, r)
    w2f = flip_bits(W2, r)
    acc = accuracy(w1f, w2f)
    dt = time.ticks_diff(time.ticks_ms(), t0)
    deg = base - acc
    print("Rate:", r, "Acc:", acc, "Deg:", deg, "ms:", dt)
    results.append((r, acc, deg, dt))

with open("seu_baseline_esp32.txt", "w") as f:
    f.write("rate,acc,deg,ms\n")
    for r, acc, deg, dt in results:
        f.write("{},{},{},{}\n".format(r, acc, deg, dt))
print("Saved to seu_baseline_esp32.txt")
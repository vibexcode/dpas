# dpas
# DPAS: Decimal Positional Angle System

**A representational framework for angular orientation based on decimal semantics.**

![DPAS Comparison](assets/dpas_comparison.png)

## Abstract
Classical angle systems (Degrees, Radians) are essential for analytic geometry but often lack semantic alignment with the decimal positional notation we use daily. The **Decimal Positional Angle System (DPAS)** proposes a labeling scheme where orthogonal transitions correspond to decimal digit capacity (0–9, 10–19, etc.).

This is **not** a replacement for trigonometric calculation but a conceptual overlay designed for robotics, UI/UX, and educational clarity.

## The Core Concept: "Decimal Overflow"
In DPAS, a full rotation is divided into **40 Macro Units**, distributed across 4 orthogonal domains (quadrants). This mirrors the "tens" digit logic:

| Domain (Quadrant) | DPAS Macro Range | Classic Degrees | Tens Digit Indicator |
|-------------------|------------------|-----------------|----------------------|
| **I (X+, Y+)** | 0.0 – 9.9        | 0° – 90°        | `0x` (Single Digit)  |
| **II (X-, Y+)** | 10.0 – 19.9      | 90° – 180°      | `1x`                 |
| **III (X-, Y-)** | 20.0 – 29.9      | 180° – 270°     | `2x`                 |
| **IV (X+, Y-)** | 30.0 – 39.9      | 270° – 360°     | `3x`                 |

## Features
- **Macro Scale (0-40):** Ideal for high-level logic and state machines.
- **Micro Scale (0-400):** Decimal subdivision for finer precision.
- **Zero Overhead:** Purely a representational layer; preserves all trigonometric identities.

## Python Implementation

The included `dpas.py` provides a robust class for converting and handling DPAS values.

### Installation
Just copy `dpas.py` into your project. No external dependencies required.

### Usage

```python
from dpas import DPAS

# 1. Convert from Degrees
angle = DPAS(195, mode='degrees')

print(f"Macro Value: {angle.macro}")  # Output: 21.66...
print(f"Domain: {angle.domain}")      # Output: 3 (Because it's in the 20s)

# 2. Check State Logic
if angle.domain == 3:
    print("System is in the 3rd Quadrant (South-West)")

# 3. Convert back
print(f"Back to Degrees: {angle.degrees}")

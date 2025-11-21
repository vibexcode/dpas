import math

class DPAS:
    """
    Decimal Positional Angle System (DPAS) Framework
    Reference: A Decimal Positional Framework for Angular Representation
    
    Features:
    - Conversions between Degrees, Radians, Macro (0-40), and Micro (0-400).
    - Automatic domain (quadrant) detection based on decimal overflow.
    """
    
    def __init__(self, value, mode='degrees'):
        """
        Initialize a DPAS angle.
        
        :param value: The numerical value of the angle.
        :param mode: The input format ('degrees', 'radians', 'macro', 'micro').
        """
        # Store internally as degrees to maintain consistency
        if mode == 'degrees':
            self._deg = value % 360
        elif mode == 'radians':
            self._deg = math.degrees(value) % 360
        elif mode == 'macro':   # 0-40 scale (10 units per quadrant)
            self._deg = (value * 9.0) % 360
        elif mode == 'micro':   # 0-400 scale (Decimal subdivision)
            self._deg = (value * 0.9) % 360
        else:
            raise ValueError("Invalid mode! Use: 'degrees', 'radians', 'macro', 'micro'")

    # --- Properties ---

    @property
    def degrees(self):
        """Returns the angle in standard degrees (0-360)."""
        return self._deg

    @property
    def radians(self):
        """Returns the angle in radians."""
        return math.radians(self._deg)

    @property
    def macro(self):
        """
        DPAS Macro Value (0 - 40).
        Represents the angle in the 40-unit decimal system.
        Example: 90 degrees -> 10.0
        """
        return self._deg / 9.0

    @property
    def micro(self):
        """
        DPAS Micro Value (0 - 400).
        Represents finer precision using decimal subdivision.
        Example: 90 degrees -> 100.0
        """
        return self._deg / 0.9

    @property
    def domain(self):
        """
        Determines the orthogonal domain (Quadrant) of the angle.
        Based on the tens digit of the Macro value:
        0 - 9.99...   -> Domain 1 (Quadrant I)
        10 - 19.99... -> Domain 2 (Quadrant II)
        20 - 29.99... -> Domain 3 (Quadrant III)
        30 - 39.99... -> Domain 4 (Quadrant IV)
        """
        m = self.macro
        if 0 <= m < 10: return 1
        elif 10 <= m < 20: return 2
        elif 20 <= m < 30: return 3
        return 4

    def __repr__(self):
        return (f"<DPAS Angle | Deg: {self.degrees:.2f}° | "
                f"Macro: {self.macro:.2f} | Domain: {self.domain}>")

# --- Example Usage ---

if __name__ == "__main__":
    # 1. Conversion from Degrees to DPAS
    angle1 = DPAS(90, mode='degrees')
    print(f"Input: 90 Degrees")
    print(f" -> DPAS Macro: {angle1.macro} (Expected: 10.0)")
    print(f" -> DPAS Micro: {angle1.micro} (Expected: 100.0)")
    print(f" -> Domain: {angle1.domain}")
    print("-" * 40)

    # 2. Creating an Angle from DPAS Macro Value (e.g., 25.5 units)
    # Since it's between 20 and 30, it must be in Domain 3.
    angle2 = DPAS(25.5, mode='macro')
    print(f"Input: 25.5 DPAS (Macro)")
    print(f" -> Equivalent Degrees: {angle2.degrees}°")
    print(f" -> Domain: {angle2.domain}")
    print("-" * 40)
    
    # 3. Robotics/Game Logic Example
    # Checking the state of an object based on its rotation.
    current_rotation = DPAS(195, 'degrees')
    
    print(f"State Check for {current_rotation.degrees}°:")
    if current_rotation.domain == 3:
        print(f" -> STATUS: Object is in Domain 3 (X- / Y-).")
        print(f" -> Decimal Position: {current_rotation.macro:.2f} (Between 20 and 30)")

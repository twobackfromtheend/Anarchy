def sign(value: float) -> float:
    return 0 if value == 0 else (1 if value > 0 else - 1)

def clamp(x, min_, max_) -> float:
    return max(min(x,max_),min_)

def clamp01(x) -> float:
    return clamp(x, 0, 1)

def clamp11(x) -> float:
    return clamp(x, -1, 1)
"""Independent equation-level utilities; not original experiment code."""
import math

def reserve(net, capacity, charge_limit, discharge_limit, eta_c, eta_d, dt=1.0):
    net = list(net)
    if not net or any(not math.isfinite(n) for n in net):
        raise ValueError("A finite nonempty net-demand window is required")
    if not (capacity > 0 and charge_limit >= 0 and discharge_limit >= 0 and 0 < eta_c <= 1 and 0 < eta_d <= 1 and dt > 0):
        raise ValueError("Invalid physical parameters")
    a = [dt * (max(n, 0)/eta_d - eta_c*min(max(-n, 0), charge_limit)) for n in net]
    r = 0.0
    thresholds = []
    for value in reversed(a):
        r = max(0.0, r + value)
        thresholds.append(r)
    return {"reserve": r, "terminal": max(0.0, sum(a)),
            "capacity infeasible": max(thresholds) > capacity,
            "power infeasible": max(net) > discharge_limit}

def block_threshold(blocks, alpha=0.1):
    """Each input block contains already formed nonnegative hourly scores."""
    blocks = [list(b) for b in blocks]
    if not blocks or any(not b for b in blocks) or not 0 < alpha < 1:
        raise ValueError("Nonempty score blocks and alpha in (0,1) required")
    if any(not math.isfinite(z) or z < 0 for b in blocks for z in b):
        raise ValueError("Scores must be finite and nonnegative")
    maxima = sorted(max(b) for b in blocks)
    k = math.ceil((len(maxima)+1)*(1-alpha))
    return math.inf if k > len(maxima) else maxima[k-1]

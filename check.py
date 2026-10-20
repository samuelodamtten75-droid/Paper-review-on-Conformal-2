"""Deterministic checks only; does not rerun manuscript experiments."""
import math
from reserve import reserve, block_threshold
r=reserve([-10,10],5,90,90,1,1)
assert r['reserve']==0 and r['capacity infeasible']
r=reserve([10,-10],20,90,90,1,1)
assert r['reserve']==10 and r['terminal']==0 and not r['capacity infeasible']
assert reserve([91],200,90,90,1,1)['power infeasible']
assert block_threshold([[float(i)] for i in range(120)])==108
assert math.isinf(block_threshold([[0]],.1))
eta=math.sqrt(.9)
print('Equation-level checks passed. No experimental reproduction performed.')
for name,charge,discharge,initial,final in [('Greedy',156.324,140.713,.116,.094),('Learned block',123.882,111.481,.260,.273),('Fixed',63.714,57.343,.293,.293)]:
    predicted=eta*charge-discharge/eta
    residual=predicted-(final-initial)
    allowance=.0005*(eta+1/eta)+.001
    print(f'{name}: storage change from flows {predicted:.9f} MWh; boundary {final-initial:.9f} MWh; residual {residual*1000:.3f} kWh; rounding allowance {allowance*1000:.3f} kWh')
    if abs(residual)>allowance: print('FLAG: discrepancy exceeds stated display rounding; original logs required.')

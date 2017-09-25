import numpy as np

alpha = 1/137.
beta = 2.5
lambda_free = 0.45517005e+6
Z = 29.
Z_eff = 28.339

lambda_bound = (1-beta*(Z_eff*alpha)**2)*lambda_free

print str(1./lambda_bound)

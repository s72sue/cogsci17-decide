from psyrun import Param

from cogsci17_decide.trial import DecisionTrial

pspace = (
    (
        Param(
            network=['UsherMcClelland'],
            scale=[1.],
            share_thresholding_intercepts=[False]) +
        Param(network=['DriftDiffusion']) *
        Param(share_thresholding_intercepts=[False, True]) *
        Param(scale=[0.2, 1.])
    ) *
    Param(baseline=[0.2, 0.6, 1.0]) *
    Param(target_sep=[0.05, 0.1, 0.15, 0.2]) *
    Param(noise=[0.0, 0.01, 0.02, 0.03, 0.04, 0.05]) *
    Param(seed=range(50))
)

min_items = 1
max_jobs = None


def execute(**kwargs):
    return DecisionTrial().run(**kwargs)

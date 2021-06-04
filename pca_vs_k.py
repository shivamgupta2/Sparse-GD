import numpy as np
import scipy
import robustlib as rl
import importlib as il
from scipy import special
from numpy import linalg as LA
import matplotlib.pyplot as plt

fsize = 20
fpad = 10
figsize = (8,4)
fontname = 'serif'

keys_pca2 = [rl.RSPCAb, rl.RSPCAdense, rl.GDPCA] 

d_pca2, eps_pca2, mass_pca2, m_pca2 = 300, 0.1, 2, 2000

params_pca2 = rl.Params(d = d_pca2,  eps = eps_pca2, mass = mass_pca2, m = m_pca2)
ylims_pca2 = (0, 0.7)
model_pca2 = rl.RSPCA_MixtureModel()
trials_pca2 = 30

k_bounds_pca2 = (1, 31, 3)

plot_m_loss_pca2 = rl.load_data(model_pca2, params_pca2, rl.err_rspca, keys_pca2)
plot_m_loss_pca2.unknown_norm = False

inputfilename_pca2 = 'data/mixture-rspca-loss-vs-k.pkl'

plot_m_loss_pca2.setdata_tofile(inputfilename_pca2, 'k', k_bounds_pca2, trials_pca2, ylims_pca2, y_is_m = False)

inputfilename_pca2 = 'data/mixture-rspca-loss-vs-k.pkl'
outputfilename_pca2 = 'figs/mixture-rspca-loss-vs-k.pdf'

plot_m_loss_pca2 = rl.plot_data(model_pca2, params_pca2, rl.err_rspca, keys_pca2)

xs = []
xlabel_pca2 = 'k'
ylabel_pca2 = 'L2 Loss'
title_pca2 = 'd = {d}, eps = {eps}, m = {m}'.format(d=d_pca2, eps=eps_pca2, m=m_pca2)

plot_m_loss_pca2.plotxy_fromfile(outputfilename_pca2, inputfilename_pca2, 'k', k_bounds_pca2, (0, 1), title_pca2, xlabel_pca2, ylabel_pca2, figsize = figsize, fsize = fsize, fpad = fpad, fontname = fontname, explicit_xs = False, xs = xs)
plt.show()

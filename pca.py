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
keys_pca1 = [rl.RSPCAb, rl.RSPCAdense, rl.GDPCA] 

d_pca1, k_pca1, eps_pca1, mass_pca1 = 200, 4, 0.1, 10

tv_pca1 = np.append(np.ones(k_pca1), np.zeros(d_pca1-k_pca1))/np.sqrt(k_pca1)
print(tv_pca1)
fv_pca1 = np.append(np.zeros(d_pca1-k_pca1), np.ones(k_pca1))

params_pca1 = rl.Params(d = d_pca1, k = k_pca1, eps = eps_pca1, mass = mass_pca1, tv = tv_pca1, fv = fv_pca1)
ylims_pca1 = (0, 0.7)
model_pca1 = rl.RSPCA_MixtureModel()
trials_pca1 = 10

m_bounds_pca1 = (10, 5000, 1000)

plot_m_loss_pca1 = rl.load_data(model_pca1, params_pca1, rl.err_rspca, keys_pca1)
plot_m_loss_pca1.unknown_norm = False

inputfilename_pca1 = 'data/mixture-rspca-loss-vs-m.pkl'

plot_m_loss_pca1.setdata_tofile(inputfilename_pca1, 'm', m_bounds_pca1, trials_pca1, ylims_pca1, y_is_m = False)

inputfilename_pca1 = 'data/mixture-rspca-loss-vs-m.pkl'
outputfilename_pca1 = 'figs/mixture-rspca-loss-vs-m.pdf'

plot_m_loss_pca1 = rl.plot_data(model_pca1, params_pca1, rl.err_rspca, keys_pca1)

xs = []
xlabel_pca1 = 'm'
ylabel_pca1 = 'L2 Loss'
title_pca1 = 'd = {d}, k = {k}, eps = {eps}'.format(d=d_pca1, k=k_pca1, eps=eps_pca1)

plot_m_loss_pca1.plotxy_fromfile(outputfilename_pca1, inputfilename_pca1, 'm', m_bounds_pca1, (0, 1), title_pca1, xlabel_pca1, ylabel_pca1, figsize = figsize, fsize = fsize, fpad = fpad, fontname = fontname, explicit_xs = False, xs = xs)
plt.show()

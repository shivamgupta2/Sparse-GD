import robustlib as rl
import matplotlib.pyplot as plt
trials_rsm3 = 10
figsize=(8,4)
fontname='serif'
fsize=20
fpad=10
d_rsm3, k_rsm3, m_rsm3 = 10, 1, 5000
nItrs_rsm3 = 200

eps_bounds_rsm3 = (0.01, 0.5, 0.01)

model_rsm3 = rl.TailFlipModel()

keys_rsm3 = [rl.Oracle, rl.RME_sp, rl.NP_sp, rl.ransacGaussianMean, rl.GDAlgs]
#keys_rsm3 = [rl.GDAlgs]
model_params_rsm3 = rl.Params(d=d_rsm3, k=k_rsm3, m=m_rsm3, nItrs=nItrs_rsm3)
ylims_rsm3 = (0, 1)
xs = []

inputfilename_rsm3 = 'data/tailflip-loss-vs-eps-pkl'
outputfilename_rsm3 = 'figs/tailflip-loss-vs-eps.pdf'
plot_m_loss_rsm3 = rl.load_data(model_rsm3, model_params_rsm3, rl.err, keys_rsm3)
#plot_m_loss_rsm3.setdata_tofile(inputfilename_rsm3, 'eps', eps_bounds_rsm3, trials_rsm3, ylims_rsm3, explicit_xs=False, xs=xs)
title_rsm3 = 'd = {d}, k = {k}, n = {m}, Noise is tail flipping'.format(d=d_rsm3, k=k_rsm3, m=m_rsm3)
xlabel_rsm3 = 'eps'
ylabel_rsm3 = 'L2 loss'
plot_m_loss_rsm3_plt = rl.plot_data(model_rsm3, model_params_rsm3, rl.err, keys_rsm3)
plot_m_loss_rsm3_plt.plotxy_fromfile(outputfilename_rsm3, inputfilename_rsm3, 'eps', eps_bounds_rsm3, (0, 1), title_rsm3, xlabel_rsm3, ylabel_rsm3, figsize=figsize, fsize=fsize, fpad=fpad, fontname=fontname, explicit_xs = False, xs = xs)
plt.savefig('tailfip-loss-vs-eps')


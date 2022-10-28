# Robust Sparse Mean Estimation via Non-Convex Optimization

A python implementation of a non-convex optimization based algorithm for robust sparse mean estimation, in the paper https://arxiv.org/abs/2109.11515. We compare our algorithm to existing algorithms for this problem, especially the one in the paper "Outlier-Robust High-Dimensional Sparse Estimation via Iterative Filtering" (https://arxiv.org/abs/1911.08085), authored by [Ilias Diakonikolas](http://www.iliasdiakonikolas.org/), [Daniel M. Kane](https://cseweb.ucsd.edu/~dakane/), [Sushrut Karmalkar](https://www.cs.utexas.edu/~sushrutk/), [Eric Price](https://www.cs.utexas.edu/~ecprice/) and [Alistair Stewart](http://www.alistair-stewart.com/). We also consider the noise models from that paper. We make use of some of the code in that paper for our experiments. 

Explanation of Files
==
* `robustlib.py`: Library containing code for robust mean estimation and robust PCA algorithms as well as to plot comparisons between the performance of these algorithms across various noise models.
*  `constant_vs_m.py`: Runs our algorithm and compares it to other algorithms under the constant bias noise model for increasing number of samples, and plots l_2 error.
*  `tflip_vs_m.py`: Runs our algorithm and compares it to other algorithms under the tail-flipping noise model for increasing number of samples, and plots l_2 error.
*  `lhiding_vs_m.py`: Runs our algorithm and compares it to other algorithms under the linear-hiding noise model for increasing number of samples, and plots l_2 error. 
*  `constant_vs_k.py`: Runs our algorithm and compares it to other algorithms under the constant bias noise model for increasing sparsity, and plots l_2 error. 
*  `lhiding_vs_k.py`: Runs our algorithm and compares it to other algorithms under the linear-hiding noise model for increasing sparsity, and plots l_2 error. 
*  `tflip_vs_eps.py`: Runs our algorithm and compares it to other algorithms under the tail-flipping noise model for increasing epsilon, and plots l_2 error.


Reference
==

This repository is an implementation of our paper "Outlier-Robust Sparse Estimation via Non-Convex Optimization", authored by [Yu Cheng](https://cs.brown.edu/people/ycheng79/), [Ilias Diakonikolas](http://www.iliasdiakonikolas.org/), [Rong Ge](https://users.cs.duke.edu/~rongge/), [Shivam Gupta](https://scholar.google.com/citations?user=HsbPV-EAAAAJ&hl=en), [Daniel M. Kane](https://cseweb.ucsd.edu/~dakane/) and [Mahdi Soltanolkotabi](https://viterbi-web.usc.edu/~soltanol/)

If you use the code for our paper, we ask that you please cite 
```
@inproceedings{cheng2022sparsegd,
  title = {Outlier-Robust Sparse Estimation via Non-Convex Optimization},
  author = {Cheng, Yu and Diakonikolas, Ilias and Kane, Daniel M. and Ge, Rong and Gupta, Shivam and Soltanolkotabi, Mahdi},
  publisher = {arXiv},
  year = {2021},
  url = {https://arxiv.org/abs/2109.11515},
  copyright = {arXiv.org perpetual, non-exclusive license},
  doi = {10.48550/ARXIV.2109.11515}
}
```

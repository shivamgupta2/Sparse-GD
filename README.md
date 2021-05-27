# Robust Sparse Mean Estimation via Non-Convex Optimization

A python implementation of a non-convex optimization based algorithm for robust sparse mean estimation. We compare our algorithm to existing algorithms for this problem, especially the one in the paper "Outlier-Robust High-Dimensional Sparse Estimation via Iterative Filtering", authored by [Ilias Diakonikolas](http://www.iliasdiakonikolas.org/), [Daniel M. Kane](https://cseweb.ucsd.edu/~dakane/), [Sushrut Karmalkar](https://www.cs.utexas.edu/~sushrutk/), [Eric Price](https://www.cs.utexas.edu/~ecprice/) and [Alistair Stewart](http://www.alistair-stewart.com/).

Explanation of Files
==
* `robustlib.py`: Library containing code for robust mean estimation and robust PCA algorithms as well as to plot comparisons between the performance of these algorithms across various noise models.
*  `constant_vs_m.py`: Runs our algorithm and compares it to other algorithms under the constant bias noise model for increasing number of samples, and plots l_2 error.
*  `tflip_vs_m.py`: Runs our algorithm and compares it to other algorithms under the tail-flipping noise model for increasing number of samples, and plots l_2 error.
*  `lhiding_vs_m.py`: Runs our algorithm and compares it to other algorithms under the linear-hiding noise model for increasing number of samples, and plots l_2 error. 
*  `constant_vs_k.py`: Runs our algorithm and compares it to other algorithms under the constant bias noise model for increasing sparsity, and plots l_2 error. 
*  `lhiding_vs_k.py`: Runs our algorithm and compares it to other algorithms under the linear-hiding noise model for increasing sparsity, and plots l_2 error. 
*  `tflip_vs_eps.py`: Runs our algorithm and compares it to other algorithms under the tail-flipping noise model for increasing epsilon, and plots l_2 error.

<!--
Reference
==

This repository is an implementation of our paper "Outlier-Robust High-Dimensional Sparse Estimation via Iterative Filtering", authored by [Ilias Diakonikolas](http://www.iliasdiakonikolas.org/), [Daniel M. Kane](https://cseweb.ucsd.edu/~dakane/), [Sushrut Karmalkar](https://www.cs.utexas.edu/~sushrutk/), [Eric Price](https://www.cs.utexas.edu/~ecprice/) and [Alistair Stewart](http://www.alistair-stewart.com/).

If you use the code for our paper, we ask that you please cite 
```
@inproceedings{diakonikolas2019outlier,
  title={Outlier-robust high-dimensional sparse estimation via iterative filtering},
  author={Diakonikolas, Ilias and Kane, Daniel and Karmalkar, Sushrut and Price, Eric and Stewart, Alistair},
  booktitle={Advances in Neural Information Processing Systems},
  pages={10689--10700},
  year={2019}
}
```
-->

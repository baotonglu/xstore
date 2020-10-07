#!/usr/bin/env python

from gnuplot import *
from common import *

"""
Experiment setup
24 threads, 1 server, 15 clients, 1 coroutine per client
`cmd: ./run.py  -st 24 -cc 1 -w ycsba -t 24  -sa "-db_type dummy -ycsb_num 10000000" -ca='-total_accts=10000000 -need_hash -workloads=dynamic2' -e 60 -n 15 -c s -a "micro" -s val00`

learned.toml
`
[[stages]]
type = "lr"
parameter = 1

[[stages]]
type = "lr"
## typically, they use much larger models
parameter = 400000
#parameter = 1000000
`

"""
xstore_points = [(2.42431e+06,0.0127433,0.339241,),(4.23381e+07,0.0195485,0.554026,),(4.00388e+07,0.0210298,0.588427,),(3.67351e+07,0.0250979,0.645831,),(3.42214e+07,0.0302861,0.71541,),(3.73285e+07,0.0207041,0.58114,),(4.13269e+07,0.020993,0.443285,),(4.12104e+07,0.0224877,0.51955,),(3.76191e+07,0.0257577,0.582519,),(3.79101e+07,0.0265728,0.578269,),(3.91076e+07,0.0210432,0.411802,),(4.02996e+07,0.0280183,0.478153,),(3.93311e+07,0.0306281,0.531388,),(3.70916e+07,0.0357004,0.578158,),(3.77133e+07,0.0202359,0.502045,),(3.61801e+07,0.0244717,0.358136,),(3.75362e+07,0.0270205,0.419479,),(3.82901e+07,0.0315918,0.4608,),(3.84401e+07,0.0336576,0.500261,),(3.48342e+07,0.0228696,0.33359,),(3.39862e+07,0.02569,0.303327,),(3.42614e+07,0.0278375,0.337448,),(3.50242e+07,0.0299951,0.370227,),(3.56236e+07,0.0313997,0.402225,),(3.63486e+07,0.0326606,0.433316,),(3.36188e+07,0.0258366,0.318943,),(3.24628e+07,0.0288894,0.27035,),(3.2447e+07,0.0313849,0.296955,),(3.31027e+07,0.031529,0.323035,),(3.36187e+07,0.03495,0.361217,),(3.31051e+07,0.0223949,0.324619,),(3.09959e+07,0.0216635,0.195139,),(3.11027e+07,0.0225686,0.210818,),(3.0988e+07,0.0254153,0.232489,),(3.15206e+07,0.0311371,0.264933,),(3.17834e+07,0.0330733,0.296558,),(3.19273e+07,0.034171,0.314768,),(3.08138e+07,0.0209515,0.222811,),(3.01273e+07,0.0230624,0.183944,),(2.99921e+07,0.0271042,0.211572,),(3.03638e+07,0.030074,0.229408,),(3.04891e+07,0.0313096,0.24675,),(3.07369e+07,0.0312464,0.264753,),(3.08092e+07,0.0356962,0.281593,),(2.98168e+07,0.0213437,0.194216,),(2.93506e+07,0.023558,0.168022,),(2.90747e+07,0.0266029,0.183301,),(2.95352e+07,0.028469,0.198559,),(2.95477e+07,0.0316512,0.213623,),(2.97028e+07,0.0335671,0.235657,),(3.00558e+07,0.0299221,0.257058,),(2.95293e+07,0.0203877,0.209959,),(2.87122e+07,0.0216022,0.14488,),(2.83512e+07,0.0252384,0.163372,),(2.87824e+07,0.0273161,0.176069,),(2.88348e+07,0.0290426,0.188838,),(2.8918e+07,0.0306046,0.201439,),(2.90354e+07,0.0305573,0.213574,),(2.91733e+07,0.0327267,0.226225,),(2.84299e+07,0.019987,0.154535,),]

rpc_points = [(388461,0,1.00003,),(3.05761e+07,0,1,),(3.08132e+07,0,1,),(3.01508e+07,0,1,),(2.98791e+07,0,1,),(2.9511e+07,0,1,),(2.91612e+07,0,1,),(2.90219e+07,0,1,),(2.86407e+07,0,1,),(2.84388e+07,0,1,),(2.8259e+07,0,1,),(2.80256e+07,0,1,),(2.77899e+07,0,1,),(2.7647e+07,0,1,),(2.73543e+07,0,1,),(2.71139e+07,0,1,),(2.70189e+07,0,1,),(2.68407e+07,0,1,),(2.66832e+07,0,1,),(2.64766e+07,0,1,),(2.63296e+07,0,1,),(2.61911e+07,0,1,),(2.59909e+07,0,1,),(2.5847e+07,0,1,),(2.57213e+07,0,1,),(2.57053e+07,0,1,),(2.55492e+07,0,1,),(2.529e+07,0,1,),(2.52838e+07,0,1,),(2.51909e+07,0,1,),(2.51053e+07,0,1,),(2.49715e+07,0,1,),(2.48552e+07,0,0.999999,),(2.47953e+07,0,1,),(2.47441e+07,0,1,),(2.46489e+07,0,1,),(2.45186e+07,0,1,),(2.42877e+07,0,1,),(2.42684e+07,0,1,),(2.42606e+07,0,0.999999,),(2.40975e+07,0,1,),(2.42086e+07,0,1,),(2.39561e+07,0,1,),(2.38576e+07,0,1,),(2.38424e+07,0,1,),(2.38107e+07,0,1,),(2.38132e+07,0,1,),(2.37782e+07,0,1,),(2.34753e+07,0,1,),(2.37695e+07,0,1,),(2.34466e+07,0,1,),(2.3493e+07,0,1,),(2.34455e+07,0,1,),(2.3428e+07,0,1,),(2.3397e+07,0,1,),(2.32652e+07,0,1,),(2.32373e+07,0,1,),(2.32606e+07,0,1,),(2.31844e+07,0,1,),(2.31e+07,0,1,),]

xstore_wo_bg_points = [(1.09602e+06,0.00792189,0.176452,),(4.37995e+07,0.00482575,0.364831,),(4.54783e+07,0.00396743,0.507493,),(3.98796e+07,0.00357108,0.614711,),(3.4058e+07,0.00299758,0.740772,),(3.10987e+07,0.00235921,0.830282,),(2.97081e+07,0.00208038,0.86327,),(2.84316e+07,0.00160669,0.89915,),(2.75054e+07,0.00132848,0.925208,),(2.69844e+07,0.00110189,0.938209,),(2.64179e+07,0.000905807,0.9483,),(2.62429e+07,0.00085269,0.956946,),(2.60901e+07,0.000672037,0.963907,),(2.55502e+07,0.000534332,0.971878,),(2.51659e+07,0.000419795,0.977797,),(2.51277e+07,0.000346488,0.980909,),(2.48494e+07,0.000308842,0.983481,),(2.45803e+07,0.000250053,0.986524,),(2.45291e+07,0.000180291,0.988782,),(2.45295e+07,0.000156439,0.989903,),(2.43357e+07,0.000144151,0.990966,),(2.41134e+07,0.000123479,0.991797,),(2.4119e+07,9.55875e-05,0.992561,),(2.39044e+07,7.42042e-05,0.993309,),(2.38731e+07,6.81565e-05,0.993955,),(2.37292e+07,5.62285e-05,0.994297,),(2.3778e+07,4.09174e-05,0.994564,),(2.37242e+07,3.8886e-05,0.994824,),(2.3602e+07,4.5285e-05,0.995031,),(2.33002e+07,3.82407e-05,0.995282,),(2.33228e+07,3.03112e-05,0.995449,),(2.30522e+07,2.03528e-05,0.995571,),(2.2904e+07,2.09946e-05,0.995741,),(2.29149e+07,2.10237e-05,0.995936,),(2.27028e+07,1.67263e-05,0.996026,),(2.27518e+07,1.5349e-05,0.99609,),(2.25458e+07,1.08519e-05,0.996161,),(2.26259e+07,8.50814e-06,0.996237,),(2.2514e+07,4.1124e-06,0.996252,),(2.24784e+07,5.2666e-06,0.996291,),(2.22055e+07,2.36886e-06,0.996337,),(2.22805e+07,3.77709e-06,0.996334,),(2.23256e+07,4.6644e-06,0.996364,),(2.19508e+07,3.40208e-06,0.99643,),(2.21677e+07,4.46051e-06,0.996424,),(2.21554e+07,4.5109e-06,0.996422,),(2.21167e+07,1.56971e-06,0.996447,),(2.19051e+07,1.58523e-06,0.996424,),(2.1837e+07,2.26422e-06,0.996423,),(2.18811e+07,3.94216e-06,0.99645,),(2.16619e+07,1.21421e-06,0.996446,),(2.16918e+07,1.3093e-06,0.996427,),(2.17226e+07,8.23172e-07,0.996428,),(2.14938e+07,1.95751e-06,0.996448,),(2.15277e+07,7.81811e-07,0.996474,),(2.14005e+07,8.35546e-07,0.996486,),(2.14032e+07,8.84811e-07,0.996512,),(2.14433e+07,1.32453e-06,0.996539,),(2.14362e+07,1.12879e-06,0.996535,),(2.14195e+07,1.03139e-06,0.996537,),]

xstore_thpt = extract_one_dim(xstore_points,0)
xstore_invalid = extract_one_dim(xstore_points,1)
xstore_fallback = extract_one_dim(xstore_points,2)

xstore_wo_bg_thpt = extract_one_dim(xstore_wo_bg_points,0)
xstore_wo_bg_invalid = extract_one_dim(xstore_wo_bg_points,1)
xstore_wo_bg_fallback = extract_one_dim(xstore_wo_bg_points,2)

rpc_thpt = extract_one_dim(rpc_points,0)

data = [xstore_thpt[1:-1],xstore_wo_bg_thpt[1:-1],rpc_thpt[1:-1]]
ylabel = "Thpt"
legends = ["Xstore","Xstore wo update","RPC"]
ylim = 4.83285e+07

data1 = [xstore_invalid[1:-1],xstore_fallback[1:-1],
         xstore_wo_bg_invalid[1:-1],xstore_wo_bg_fallback[1:-1]
]

legends1 = ["Invaid ratio","Fallback ratio",
            "No update invalid ratio","No update fallback ratio"]
def main():
    output_aligned_lines("ycsbd",data,legends)
    output_aligned_lines("ycsbd_ratio",data1,legends1)

if __name__ == "__main__":
    main()
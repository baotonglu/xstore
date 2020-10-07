#!/usr/bin/env python

from gnuplot import *

"""
 Used experiment setup:
 - learned.toml:
   {

[[stages]]
type = "lr"
parameter = 1

[[stages]]
type = "lr"
## typically, they use much larger models
parameter = 100000 ## larger is better

}

keys: 10,000,000; using YCSBHash
1 fstore server (12 threads).

Clients use the same #thread as server, each with 6 coroutine.
...

"""

rpc_thpts = [
    11.75083963,
    17.21717848,
    18.96709591,
    21.21259380,
    20.79702557,
    21.02255861,
    21.06653246,
    20.83072562
]

rpc_lats = [
    5.48123,
    7.1544,
    10.9653,
    14.1716,
    19.7381,
    24.1275,
    25.3927,
    27.4726,
]

btree_thpts = [3.37671096,
               4.76237942,
               4.76241511,
               4.76243196,
               4.76242331
               ]

btree_lats = [
    21.0323,
    28.7889,
    45.0051,
    55.7117,
    70.8427,
]

sc_thpts = [7.63163645,
            14.34216880,
            15.88023158,
            15.87948391,
            15.88097543,
            15.87978063,
            15.88086191,
            15.87965399,
            15.88104280
            ]

sc_lats = [8.47967,
           9.20777,
           12.9953,
           15.9626,
           20.885,
           25.4654,
           28.1208,
           35.4989,
           39.3232,
           ]

hybrid_thpts = [11.75083963,
                17.21717848,
                22.23607595,
                23.06713643,
                23.07278290,
                23.07646720,
                23.06453187,
                23.07008926
                ]
hybrid_lats = [5.48123,
               7.1544,
               9.04291,
               10.7488,
               14.2724,
               17.7709,
               19.3733,
               22.3401
               ]
# use coroutine = 2
# client machine settings: [1,2,3,4,5,6,7,8,10,12,14,15]
sc_thpts_2 = [7213227.00, 14032012.38,  26788433.05,
              30953717.55, 31751569.38, 31759712.58, 31762295.15, 31759088.00, 31759136.42,
              31763321.54, 31550543.71, 30314439.42,
              30066554.89]
sc_lats_2 = [5.84738, 6.40919,
             6.5842, 7.04736, 8.00613, 9.91357, 10.7909, 12.028, 12.7687, 15.4216, 17.311, 17.9885, 19.9416]

rpc_thpts_2 = [9958484.35, 16948576.01, 20856072.61,
               23327579.65, 25777254.18, 26753545.69, 27804524.38, 28652541.51, 28945160.60, 29030652.92, 29286413.92,
               29030114.48,
               29007642.93]
rpc_lats_2 = [4.05817, 4.88279, 5.794,
              6.47636, 7.4565, 8.578, 9.50694, 11.8754, 13.0113, 15.3322, 17.3052, 19.5151, 21.7702]

# all coroutine == 1 // seems using too many coroutines causes performance drop for RDMA
scs = {
    1: (4011852.48, 5.92749),
    2: (7567489.40, 5.93193),
    4: (14626361.83, 6.08275),
    6: (21559751.09, 6.09052),
    8: (27207710.53, 6.41318),
    10: (30916140.91, 7.33364),
    12: (31747036.68, 8.10456),
    14: (31758347.15,  9.30428),
    15: (31760332.73, 9.83267),
}

rpcs = {
    1: (5593658.14, 3.85236),
    2: (9991639.75, 4.10361),
    4: (16650770.52, 4.78502),
    6: (21048263.59, 5.53351),
    8: (24204784.28, 6.49256),
    10: (25643227.80, 7.31005),
    12: (27004561.04, 8.52083),
    14: (28035615.38, 9.73366),
    15: (28258339.85, 10.7066),
}

nts = {
    1: (1732259.77, 13.9512),
    2: (3255060.37, 14.3526),
    4: (6299171.39, 14.5088),
    6: (8750296.55, 15.4833),
    8: (9524717.16, 18.7233),
    10: (9524802.37, 20.4468),
    12: (9524797.06, 28.0206),
    14: (9524802.61, 34.0163),
    15: (9524786.88, 36.0173)
}


def main():
    #    output_gnuplot_res("ycsbc", 12, (sc_thpts_2, sc_lats_2),
    #                       (rpc_thpts_2, rpc_lats_2)
    #                       )
    output_res_2("ycsbc", scs, rpcs, nts)


if __name__ == "__main__":
    main()
import numpy as np

def custom_gen_data(g=[.95], sn=.3, T=3000, framerate=30, firerate_range=(0.1, 1.0), b=0, N=20, seed=13):
    np.random.seed(seed)
    firing_rates = np.random.uniform(low=firerate_range[0], high=firerate_range[1], size=N)
    trueSpikes = np.array([
        np.random.rand(T) < fr / float(framerate)
        for fr in firing_rates
    ])

    truth = trueSpikes.astype(float)

    for i in range(2, T):
        if len(g) == 2:
            truth[:, i] += g[0] * truth[:, i - 1] + g[1] * truth[:, i - 2]
        else:
            truth[:, i] += g[0] * truth[:, i - 1]

    Y = b + truth + sn * np.random.randn(N, T)
    return Y, truth, trueSpikes, firing_rates


Y, truth, trueSpikes, firing_rates = custom_gen_data(N=400, firerate_range=(0.1, 5.0))
spike_times_list = np.array([np.where(trueSpikes[i])[0]/30 for i in range(trueSpikes.shape[0])], dtype=object)
np.save('../data/spike_times.npy', spike_times_list, allow_pickle=True)

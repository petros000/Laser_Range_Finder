def get_Range(las, trgt, receiv, atmos):
    res = 0
    range_min = 100
    range_max = 100_000
    while range_max - range_min >= 5:
        range_mid = round((range_min + range_max) / 2)
        tau_atm = atmos.get_transmission_coefficient(range_mid)
        E_las = las.get_power_density(range_mid) * tau_atm
        I_tgt = trgt.get_radiation_power(E_las)
        P_sig = receiv.get_power_signal(I_tgt, range_mid) * tau_atm
        snr_cur = receiv.get_SNR(P_sig)

        if receiv.snr - 0.05 <= snr_cur <= receiv.snr + 0.05:
            return range_mid
        if snr_cur > receiv.snr:
            range_min = range_mid
        else:
            range_max = range_mid

    return res





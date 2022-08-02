from atmosphere import Atmosphere
from laser import Laser
from receiver import Receiver
from target import Target


def get_Range(las, trgt, receiv, atmos):
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
        if snr_cur > 3:
            range_min = range_mid
        else:
            range_max = range_mid

            

H_bot = 5000
H_top = 5500
Temp = 20
Vis = 20
lmd = 1.06
atmos = Atmosphere(H_bot, H_top, Vis, Temp, lmd)

fi_las = 1.2
P_las = 3.6
las = Laser(fi_las, P_las, lmd)

ro_tgt = 0.5
S_tgt = 0.5
trgt = Target(ro_tgt, S_tgt)

Dapp = 80
tau = 0.8
sens = 0.6
i_nouse = 8
receiv = Receiver(Dapp, sens, i_nouse, tau)


print(round(get_Range(las, trgt, receiv, atmos)/1000, 2))


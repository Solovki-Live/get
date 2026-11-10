def trian(freq, time):
    period = 1/freq
    ans = period - 2 * (time % period)
    ans = abs(ans)
    return ans * freq
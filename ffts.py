import numpy as np

def fftDFSR(x, N):
    "Blake, Witten, Cree (2013), Figure 1"
    assert(N <= 4 or N % 4 == 0) # TODO expensive mod >.<
    y = np.empty(N, dtype=np.complex128) # TODO should be customizable
    if N==1:
        y[0] = x[0]
        return y
    if N==2:
        y[0] = x[0] + x[1]
        y[1] = x[0] - x[1]
        return y

    w = np.exp(-2j * np.pi / N)
    wk = w ** np.arange(N//4)
    wkinv = np.conj(wk)

    Uk2 = fftDFSR(x[::2], N//2)
    Zk4 = fftDFSR(x[1:N-1:4], N//4)
    ZPk4= fftDFSR(np.hstack([x[-1], x[3:N-1:4]]), N//4)

    foo = wk * Zk4[:N//4] + wkinv * ZPk4[:N//4]
    y[:N//4] = Uk2[:N//4] + foo
    y[N//2 : (N//2 + N//4)] = Uk2[:N//4] - foo

    bar = 1j * (wk * Zk4[:N//4] - wkinv * ZPk4[:N//4])
    y[N//4 : N//2] = Uk2[N//4 : N//2] - bar
    y[3*N//4 : ] = Uk2[N//4 : N//2] + bar

    return y




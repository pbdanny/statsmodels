from numpy import array


class Holder(object):
    pass


mlpacf = Holder()
mlpacf.comment = 'mlab.parcorr(x, [], 2, nout=3)'
mlpacf.name = 'mlpacf'
mlpacf.lags1000 = array([
    [  0.],
    [  1.],
    [  2.],
    [  3.],
    [  4.],
    [  5.],
    [  6.],
    [  7.],
    [  8.],
    [  9.],
    [ 10.],
    [ 11.],
    [ 12.],
    [ 13.],
    [ 14.],
    [ 15.],
    [ 16.],
    [ 17.],
    [ 18.],
    [ 19.],
    [ 20.]])
mlpacf.bounds1000 = array([
    [ 0.06334064],
    [-0.06334064]])
mlpacf.lags100 = array([
    [  0.],
    [  1.],
    [  2.],
    [  3.],
    [  4.],
    [  5.],
    [  6.],
    [  7.],
    [  8.],
    [  9.],
    [ 10.],
    [ 11.],
    [ 12.],
    [ 13.],
    [ 14.],
    [ 15.],
    [ 16.],
    [ 17.],
    [ 18.],
    [ 19.],
    [ 20.]])
mlpacf.pacf100 = array([
    [ 1.        ],
    [ 0.47253777],
    [-0.49466966],
    [-0.02689319],
    [-0.00122204],
    [ 0.08419183],
    [ 0.03220774],
    [ 0.10404012],
    [ 0.05304617],
    [-0.04129564],
    [-0.04049451],
    [ 0.11727754],
    [ 0.11804158],
    [-0.05864957],
    [-0.15681802],
    [ 0.11828684],
    [ 0.05156002],
    [ 0.00694629],
    [ 0.01668964],
    [ 0.02236851],
    [-0.0909443 ]])
mlpacf.pacf1000 = array([
    [  1.00000000e+00],
    [  5.29288262e-01],
    [ -5.31849027e-01],
    [  1.17440051e-02],
    [ -5.37941905e-02],
    [ -4.11119348e-02],
    [ -2.40367432e-02],
    [  2.24289891e-02],
    [  3.33007235e-02],
    [  4.59658302e-02],
    [  6.65850553e-03],
    [ -3.76714278e-02],
    [  5.27229738e-02],
    [  2.50796558e-02],
    [ -4.42597301e-02],
    [ -1.95819186e-02],
    [  4.70451394e-02],
    [ -1.70963705e-03],
    [  3.04262524e-04],
    [ -6.22001614e-03],
    [ -1.16694989e-02]])
mlpacf.bounds100 = array([
    [ 0.20306923],
    [-0.20306923]])

mlacf = Holder()
mlacf.comment = 'mlab.autocorr(x, [], 2, nout=3)'
mlacf.name = 'mlacf'
mlacf.acf1000 = array([
    [ 1.        ],
    [ 0.5291635 ],
    [-0.10186759],
    [-0.35798372],
    [-0.25894203],
    [-0.06398397],
    [ 0.0513664 ],
    [ 0.08222289],
    [ 0.08115406],
    [ 0.07674254],
    [ 0.04540619],
    [-0.03024699],
    [-0.05886634],
    [-0.01422948],
    [ 0.01277825],
    [-0.01013384],
    [-0.00765693],
    [ 0.02183677],
    [ 0.03618889],
    [ 0.01622553],
    [-0.02073507]])
mlacf.lags1000 = array([
    [  0.],
    [  1.],
    [  2.],
    [  3.],
    [  4.],
    [  5.],
    [  6.],
    [  7.],
    [  8.],
    [  9.],
    [ 10.],
    [ 11.],
    [ 12.],
    [ 13.],
    [ 14.],
    [ 15.],
    [ 16.],
    [ 17.],
    [ 18.],
    [ 19.],
    [ 20.]])
mlacf.bounds1000 = array([
    [ 0.0795181],
    [-0.0795181]])
mlacf.lags100 = array([
    [  0.],
    [  1.],
    [  2.],
    [  3.],
    [  4.],
    [  5.],
    [  6.],
    [  7.],
    [  8.],
    [  9.],
    [ 10.],
    [ 11.],
    [ 12.],
    [ 13.],
    [ 14.],
    [ 15.],
    [ 16.],
    [ 17.],
    [ 18.],
    [ 19.],
    [ 20.]])
mlacf.bounds100 = array([
    [ 0.24319646],
    [-0.24319646]])
mlacf.acf100 = array([
    [ 1.        ],
    [ 0.47024791],
    [-0.1348087 ],
    [-0.32905777],
    [-0.18632437],
    [ 0.06223404],
    [ 0.16645194],
    [ 0.12589966],
    [ 0.04805397],
    [-0.03785273],
    [-0.0956997 ],
    [ 0.00644021],
    [ 0.17157144],
    [ 0.12370327],
    [-0.07597526],
    [-0.13865131],
    [ 0.02730275],
    [ 0.13624193],
    [ 0.10417949],
    [ 0.01114516],
    [-0.09727938]])

mlccf = Holder()
mlccf.comment = 'mlab.crosscorr(x[4:], x[:-4], [], 2, nout=3)'
mlccf.name = 'mlccf'
mlccf.ccf100 = array([
    [ 0.20745123],
    [ 0.12351939],
    [-0.03436893],
    [-0.14550879],
    [-0.10570855],
    [ 0.0108839 ],
    [ 0.1108941 ],
    [ 0.14562415],
    [ 0.02872607],
    [-0.14976649],
    [-0.08274954],
    [ 0.13158485],
    [ 0.18350343],
    [ 0.00633845],
    [-0.10359988],
    [-0.0416147 ],
    [ 0.05056298],
    [ 0.13438945],
    [ 0.17832125],
    [ 0.06665153],
    [-0.19999538],
    [-0.31700548],
    [-0.09727956],
    [ 0.46547234],
    [ 0.92934645],
    [ 0.44480271],
    [-0.09228691],
    [-0.21627289],
    [-0.05447732],
    [ 0.13786254],
    [ 0.15409039],
    [ 0.07466298],
    [-0.01000896],
    [-0.06744264],
    [-0.0607185 ],
    [ 0.04338471],
    [ 0.12336618],
    [ 0.07712367],
    [-0.08739259],
    [-0.09319212],
    [ 0.04426167]])
mlccf.lags1000 = array([
    [-20.],
    [-19.],
    [-18.],
    [-17.],
    [-16.],
    [-15.],
    [-14.],
    [-13.],
    [-12.],
    [-11.],
    [-10.],
    [ -9.],
    [ -8.],
    [ -7.],
    [ -6.],
    [ -5.],
    [ -4.],
    [ -3.],
    [ -2.],
    [ -1.],
    [  0.],
    [  1.],
    [  2.],
    [  3.],
    [  4.],
    [  5.],
    [  6.],
    [  7.],
    [  8.],
    [  9.],
    [ 10.],
    [ 11.],
    [ 12.],
    [ 13.],
    [ 14.],
    [ 15.],
    [ 16.],
    [ 17.],
    [ 18.],
    [ 19.],
    [ 20.]])
mlccf.bounds1000 = array([
    [ 0.06337243],
    [-0.06337243]])
mlccf.ccf1000 = array([
    [ 0.02733339],
    [ 0.04372407],
    [ 0.01082335],
    [-0.02755073],
    [-0.02076039],
    [ 0.01624263],
    [ 0.03622844],
    [ 0.02186092],
    [-0.00766506],
    [-0.0101448 ],
    [ 0.01279167],
    [-0.01424596],
    [-0.05893064],
    [-0.03028013],
    [ 0.04545462],
    [ 0.076825  ],
    [ 0.08124118],
    [ 0.08231121],
    [ 0.05142144],
    [-0.06405412],
    [-0.25922346],
    [-0.35806674],
    [-0.1017256 ],
    [ 0.5293535 ],
    [ 0.99891094],
    [ 0.52941977],
    [-0.10127572],
    [-0.35691466],
    [-0.25943369],
    [-0.06458511],
    [ 0.05026194],
    [ 0.08196501],
    [ 0.08242852],
    [ 0.07775845],
    [ 0.04590431],
    [-0.03195209],
    [-0.06162966],
    [-0.01395345],
    [ 0.01448736],
    [-0.00952503],
    [-0.00927344]])
mlccf.lags100 = array([
    [-20.],
    [-19.],
    [-18.],
    [-17.],
    [-16.],
    [-15.],
    [-14.],
    [-13.],
    [-12.],
    [-11.],
    [-10.],
    [ -9.],
    [ -8.],
    [ -7.],
    [ -6.],
    [ -5.],
    [ -4.],
    [ -3.],
    [ -2.],
    [ -1.],
    [  0.],
    [  1.],
    [  2.],
    [  3.],
    [  4.],
    [  5.],
    [  6.],
    [  7.],
    [  8.],
    [  9.],
    [ 10.],
    [ 11.],
    [ 12.],
    [ 13.],
    [ 14.],
    [ 15.],
    [ 16.],
    [ 17.],
    [ 18.],
    [ 19.],
    [ 20.]])
mlccf.bounds100 = array([
    [ 0.20412415],
    [-0.20412415]])

mlywar = Holder()
mlywar.comment = "mlab.ar(x100-x100.mean(), 10, 'yw').a.ravel()"
mlywar.arcoef100 = array([
    1.        , -0.66685531,  0.43519425, -0.00399862,  0.05521524,
    -0.09366752,  0.01093454, -0.00688404, -0.04739089,  0.00127931,
    0.03946846])
mlywar.arcoef1000 = array([
    1.        , -0.81230253,  0.55766432, -0.02370962,  0.02688963,
    0.01110911,  0.02239171, -0.01891209, -0.00240527, -0.01752532,
    -0.06348611,  0.0609686 , -0.00717163, -0.0467326 , -0.00122755,
    0.06004768, -0.04893984,  0.00575949,  0.00249315, -0.00560358,
    0.01248498])
mlywar.name = 'mlywar'

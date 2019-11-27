from pylab import *
from scipy import interpolate
rc('text', usetex=True)
rc('text.latex',preamble = \
[
    r'\usepackage[russian]{babel}',
    r'\usepackage{amsmath}',
    r'\usepackage{amssymb}',
])
a4size=21/2.56
rc('font',family='serif',size = 12)
rc('axes',labelsize=14)
rc('figure',figsize=[a4size,a4size*3/4])
rc('legend',fontsize=9)

I=np.array([1.5332,0.7248,0.2018,0.1234])
N=np.array([1,4,32,64])
plot(N,I)
ylabel(r'$I,\text{ доверительный интервал}$')
xlabel(r'$N,\text{ количество отсчетов}$')
grid(which='major', linestyle='-')
grid(which='minor', linestyle=':')
minorticks_on()
legend()
savefig('/home/kannab/documents/random_process/fig/plot2.pdf',bbox_inches='tight')

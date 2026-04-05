import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
from scipy.fft import rfft, rfftfreq
import matplotlib as mpl

    


frenq = 800                                                                  #frenquency in HZ
NFFT = 256                                                                   #for spectrogramm



data = pd.read_csv('1l_1a_1.csv', sep=',', header=None)


value_t   = data[0]                                                         #time
value_x = data[1]                                                           #acceleration on x
value_y = data[2]                                                           #acceleration on y
value_z = data[3]                                                           #acceleration on z
#value_abs = ((value_x**2) +(value_y**2) + (value_z**2))**0.5                #abs acceleration xyz



fig = plt.figure(constrained_layout=True)
spec = gridspec.GridSpec(ncols=2, nrows=4, figure=fig)

f_1_1 = fig.add_subplot(spec[0, :])

f_1_2 = fig.add_subplot(spec[1, 0])
f_2_2 = fig.add_subplot(spec[1, 1])

f_1_3 = fig.add_subplot(spec[2, 0])
f_2_3 = fig.add_subplot(spec[2, 1])

f_1_4 = fig.add_subplot(spec[3, 0])
f_2_4 = fig.add_subplot(spec[3, 1])

#f_1_5 = fig.add_subplot(spec[4, 0])
#f_2_5 = fig.add_subplot(spec[4, 1])


#top plot
f_1_1.set_title("Full Acceleration")
f_1_1.plot(value_t, value_x,"-b" ,label="x")
f_1_1.plot(value_t, value_y,"-r", label="y")
f_1_1.plot(value_t, value_z, "-g", label="z")
f_1_1.grid(True)
f_1_1.legend()

#x_plot
f_1_2.set_title("Isolate Acceleration")
f_1_2.plot(value_t, value_x,"-b" ,label="x")
f_1_2.grid(True)
f_1_2.legend()

#y_plot
f_1_3.plot(value_t, value_y,"-r", label="y")
f_1_3.grid(True)
f_1_3.legend()

#z_plot
f_1_4.plot(value_t, value_z, "-g", label="z" )
f_1_4.grid(True)
f_1_4.legend()

#abs_plot
# f_1_5.plot(value_t, value_abs, "-k" , label="|a|" )
# f_1_5.grid(True)
# f_1_5.legend()


#Furie Transform
N=len(data[0])

fft_x       =np.abs(rfft(value_x,   workers=10)) * (2/N)
fft_y       =np.abs(rfft(value_y,   workers=10)) * (2/N)  
fft_z       =np.abs(rfft(value_z,   workers=10)) * (2/N)   
#fft_abs_a   =np.abs(rfft(value_abs, workers=10)) * (2/N)  
fft_time    =rfftfreq(N, 1/frenq)


f_2_2.set_title("Fourier Transforms")
f_2_2.plot(fft_time, np.abs(fft_x),"-b" ,label="x")
f_2_2.grid(True)
f_2_2.legend()

f_2_3.plot(fft_time, np.abs(fft_y),"-r", label="y")
f_2_3.grid(True)
f_2_3.legend()

f_2_4.plot(fft_time, np.abs(fft_z), "-g", label="z")
f_2_4.grid(True)
f_2_4.legend()

# f_2_5.plot(fft_time, np.abs(fft_abs_a),"-k" , label="|a|")
# f_2_5.grid(True)
# f_2_5.legend()



#Spectrogramm
plt.figure(1)
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Spectrogramm dB')

spectrum, freqs, times, im = ax1.specgram(value_x, Fs = frenq, NFFT = NFFT, scale ='dB', cmap='inferno')
ax1.set_ylabel('X. Frenquency [Hz]')
ax1.grid(True)

spectrum, freqs, times, im = ax2.specgram(value_y, Fs = frenq, NFFT = NFFT, scale ='dB', cmap='inferno')
ax2.set_ylabel('Y. Frenquency [Hz]')
ax2.grid(True)

spectrum, freqs, times, im = ax3.specgram(value_z, Fs = frenq, NFFT = NFFT, scale ='dB', cmap='inferno')
ax3.set_ylabel('Z. Frenquency [Hz]')
ax3.grid(True)



plt.figure(2)
fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Spectrogramm linear')

spectrum, freqs, times, im = ax1.specgram(value_x, Fs = frenq, NFFT = NFFT, scale ='linear', cmap='inferno')
ax1.set_ylabel('X. Frenquency [Hz]')
ax1.grid(True)

spectrum, freqs, times, im = ax2.specgram(value_y, Fs = frenq, NFFT = NFFT, scale ='linear', cmap='inferno')
ax2.set_ylabel('Y. Frenquency [Hz]')
ax2.grid(True)

spectrum, freqs, times, im = ax3.specgram(value_z, Fs = frenq, NFFT = NFFT, scale ='linear', cmap='inferno')
ax3.set_ylabel('Z. Frenquency [Hz]')
ax3.grid(True)

plt.show()

#plt.cm.gist_heat
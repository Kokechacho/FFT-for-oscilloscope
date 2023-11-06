import numpy as np
import matplotlib.pyplot as plt

def graficarDFT(file):

    plt.rcParams['figure.figsize'] = [16, 12]
    plt.rcParams.update({'font.size': 18})


    # Cargas los datos en una matriz
    dataVector = np.loadtxt(file, delimiter = '\t')

    # Traspones la matriz para tener FILA 1 -> x (tiempo) FILA 2 -> y (data)
    dataVector = dataVector.transpose()

    # Filtramos dos vectores | X = time | Y = data
    time = dataVector[0]
    data = dataVector[1]

    # Los datos vienen dados por intervalos de 0.002
    dt = time[1]-time[0]

    # Longitud de la muestra
    n = len(time)

    # Hacemos una transformada rápida de Fourier sobre la muestra
    fft = np.fft.fft(data,n)

    # PSD = fft * fft/n  # Espectro de poder | (Habría que multiplicarlo por el conjugado para normalizar los picos negativos)
    PSD = fft * np.conj(fft) / n

    # PSD = 20 * np.log10(PSD/0.755)  # Por si se necesita pasar de fuerza relativa a decibelios

    # Vector de frecuencias (1/(0.002*100,000)) * [0,1,2...100,000] = [0,0.005,0.01...500] => 100,000 elementos de frecuencias repartidas ecuanimamente (hasta 500Mghz)
    freq = (1/(dt*n)) * np.arange(n)

    # Vector de escala => si solo queremos 1,000 valores => [1,2,3...999] => solo queremos medir los 5 primeros MgHz [0,0.005,0.01...4.99] (primeros 1,000 elementos del vector de frecuencias)
    L = np.arange(1, np.floor(n/100), dtype='int')

    # Filtros para quitar el ruido
    indices = PSD > 1000  # Solo nos quedamos con datos que superen un arbitrario límite [True False True...]
    PSDclean = PSD * indices  # Multiplicamos los datos por los indices para llevar a 0 aquellos datos que no sirvan

    # Hacemos lo mismo con los datos transformados para hacer la inversa de la transformada de Fourier y sacar datos más "limpios"
    fft = indices * fft
    fftfilt = np.fft.ifft(fft)  # Hacemos la inversa

    # Sacamos la frecuencia del pico más alto (Esto nos dice la frecuencia de resonancia)
    freq_max = freq[np.argmax(PSD)]
    print(freq_max)

    # Ploteamos las 4 figuras
    fig,axs = plt.subplots(4,1)

    plt.sca(axs[0])
    plt.plot(time, data, color='c', linewidth=1.5, label='Datos "raw"')
    plt.xlim(time[0], time[-1])
    plt.legend()

    plt.sca(axs[1])
    plt.plot(time, fftfilt, color='c', linewidth=2, label='Datos invertidos exentos de ruido')
    plt.xlim(time[0], time[-1])
    plt.legend()

    plt.sca(axs[2])
    plt.plot(freq[L], PSD[L], color='c', linewidth=2, label='Datos transformados con Fourier')
    plt.xlim(freq[L[0]], freq[L[-1]])
    plt.legend()

    plt.sca(axs[3])
    plt.plot(freq[L], PSD[L], color='c', linewidth=2, label='Datos transformados con Fourier')
    plt.plot(freq[L], PSDclean[L], color='k', linewidth=1.5, label='Datos filtrados')
    plt.xlim(freq[L[0]], freq[L[-1]])
    plt.legend()

    plt.annotate('Frecuencia de resonancia = ' + "{:.4f}".format(freq_max) + ' MgHz', xy=(freq_max, max(PSD)), fontsize=16, xytext=(1, max(PSD)*0.7),
                 arrowprops=dict(facecolor='red'), color='g')

    plt.show()


graficarDFT('ruido_largaCA.txt')
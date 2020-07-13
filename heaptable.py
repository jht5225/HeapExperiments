import math
import matplotlib.pyplot as plt
import sys
""" A program that takes, as a commandline argument, a heapsize (n) and creates the PDF of p_{k,j} for all relevant k,j."""

""" computes n choose k"""
def choose(n,k):
    nfac = math.factorial(n)
    kfac = math.factorial(k)
    diffac = math.factorial(n-k)
    div = nfac/(kfac*diffac)
    return div



"""Given k, returns all j such that p_{k,j} > 0 as well as corresponding values of p_{k,j}"""
def get_heap_pdf(k):
    j = 1
    x = []
    y = []
    while j < k:
        frac = (1)/(2**(k-2))
        ch = choose((k-2), (j-1))
        prob = frac*ch
        x.append(j)
        y.append(prob)
        j = j + 1
    return x,y

"""
Given a heapsize n, plots the pdf for min_k <= k <= max_k.
max_k will be set to (n-1)/2 if max_k < min_k or max_k > (n-k)/2
"""
def get_all_pdfs(n, min_k = 2, max_k = 1):
    #Set up plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    title = "PDF for heap of size " + str(n)
    ax.title.set_text(title)
    ax.set_xlabel("J")
    ax.set_ylabel("Probability")

    #Determine upper_bound
    upper_bound = math.floor(((n-1)/2))
    if((max_k < min_k) or (max_k > upper_bound)):
        max_val = upper_bound
    else:
        max_val = max_k
    k = min_k

    #plot pdfs
    while k <= max_val:

        #get datapoints for each pdf
        domain,range = get_heap_pdf(k)

        ax.plot(domain,range, marker="o", label=str(k))
        k = k + 1
    plt.legend(loc='upper right', title='K')
    plt.show()


def main():
    get_all_pdfs(int(sys.argv[1]))

if __name__ == '__main__':
    main()

import math
import matplotlib.pyplot as plt

def choose(n,k):
    nfac = math.factorial(n)
    kfac = math.factorial(k)
    diffac = math.factorial(n-k)
    div = nfac/(kfac*diffac)
    return div

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

def get_all_pdfs(n, min_k = 2):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    title = "PDF for heap of size " + str(n)
    ax.title.set_text(title)
    ax.set_xlabel("J")
    ax.set_ylabel("Probability")
    upper_bound = math.floor(((n-1)/2))
    k = min_k
    while k <= upper_bound:

        domain,range = get_heap_pdf(k)

        ax.plot(domain,range, marker="o", label=str(k))
        k = k + 1
    plt.legend(loc='upper right', title='K')
    plt.show()


def main():
    get_all_pdfs(30)

if __name__ == '__main__':
    main()

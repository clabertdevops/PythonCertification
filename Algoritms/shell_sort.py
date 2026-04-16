def sedgewick_gaps(n):
    """
    Genera la sequenza di gap di Sedgewick minori di n.
    Restituisce una lista ordinata in ordine decrescente.
    """
    gaps = []
    k = 0

    while True:
        # Calcola il k-esimo gap di Sedgewick
        if k % 2 == 0:
            # formula per k pari
            gap = 9 * (2 ** k) - 9 * (2 ** (k // 2)) + 1
        else:
            gap = 1 + 8 * 2**k - 6 * 2**((k+1)//2)

        # Se il gap è maggiore o uguale a n, interrompi il ciclo
        if gap >= n:
           # formula per k dispari
            gap = 8 * (2 ** k) - 6 * (2 ** ((k + 1) // 2)) + 1

        if gap > n:
            break

        gaps.append(gap)
        k +=1
    
    return gaps[::-1]  # dal più grande al più piccolo

def shell_sort(arr):
    """
    Shell Sort usando la sequenza di Sedgewick.
    Versione didattica con print dettagliati.
    """
    n = len(arr)
    gaps = sedgewick_gaps(n)

    print(f"Array iniziale: {arr}")
    print(f"Sequenza di gap (Sedgewick): {gaps}\n")

    #ciclo sui gap
    for gap in gaps:
        
        print(f"=== GAP = {gap} ===")

        for i in range(gap, n):
            temp = arr[i]
            j = i

            print(f"\nConsidero elemento arr[{i}]")

            # Spostamento degli elementi
            while j >= gap and arr[j - gap] > temp:
                print(
                    f"  arr[{j}] = arr[{j-gap}] ({arr[j-gap]}) "
                    f"> {temp}  → sposto"
                )
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
            print(f"  Inserisco {temp} in posizione {j}")
            print(f"  Stato array: {arr}")

        print(f"\nArray dopo gap {gap}: {arr}\n")
        print(f"Array ordinato: {arr}")
def print_matrix(matrix):
    # Fungsi untuk mencetak matriks
    for row in matrix:
        for val in row:
            print(val, end="\t")
        print()

def gauss_jordan_elimination(matrix):
    # Metode eliminasi Gauss-Jordan
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        # Mencari baris dengan elemen terbesar pada kolom i
        max_row = i
        for j in range(i + 1, rows):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        # Menukar baris dengan elemen terbesar ke baris i
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Mengubah elemen diagonal menjadi 1
        pivot = matrix[i][i]
        print("\nOBE pada langkah {}:".format(i+1))
        print("R{} /= {}".format(i+1, pivot))
        for j in range(i, cols):
            matrix[i][j] /= pivot
        print_matrix(matrix)

        # Mengubah elemen-elemen di bawah elemen diagonal menjadi 0
        for j in range(rows):
            if j != i:
                factor = matrix[j][i]
                print("\nR{} -= {} * R{}".format(j+1, factor, i+1))
                for k in range(i, cols):
                    matrix[j][k] -= factor * matrix[i][k]
                print_matrix(matrix)

def main():
    while True:
        matrix = [[0.0] * 4 for _ in range(3)]

        # Input matriks augmented dari pengguna
        print("Masukkan matriks augmented:")
        for i in range(3):
            for j in range(3):
                matrix[i][j] = float(input("a{}{}: ".format(i+1, j+1)))
            matrix[i][3] = float(input("x{}: ".format(i+1)))

        # Tampilkan matriks sebelum eliminasi
        print("\nMatriks sebelum eliminasi Gauss-Jordan:")
        print_matrix(matrix)

        # Lakukan eliminasi Gauss-Jordan
        gauss_jordan_elimination(matrix)

        # Tampilkan matriks setelah eliminasi
        print("\nMatriks setelah eliminasi Gauss-Jordan:")
        print_matrix(matrix)

        # Tampilkan solusi persamaan linear
        print("\nJadi solusi persamaan linearnya adalah: x, y, z = ({}, {}, {})".format(matrix[0][3], matrix[1][3], matrix[2][3]))

        # Tanya user untuk mengulangi program
        choice = input("-Thanks to ChatGPT-\nApakah ingin mengulangi? (Y/N): ")
        if choice.lower() != "y":
            break

if __name__ == "__main__":
    main()

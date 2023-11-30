import tkinter as tk
from tkinter import Entry, Label, Button

def print_matrix(matrix, output_label):
    # Fungsi untuk mencetak matriks pada label output
    result = ""
    for row in matrix:
        for val in row:
            result += f"{val:.2f}\t"
        result += "\n"
    output_label.config(text=result)

def gauss_jordan_elimination(matrix, output_label):
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
        for j in range(i, cols):
            matrix[i][j] /= pivot

        # Mengubah elemen-elemen di bawah elemen diagonal menjadi 0
        for j in range(rows):
            if j != i:
                factor = matrix[j][i]
                for k in range(i, cols):
                    matrix[j][k] -= factor * matrix[i][k]

        # Update tampilan setiap langkah eliminasi
        output_label.config(text="")
        print_matrix(matrix, output_label)
        output_label.update()

def on_submit(matrix_entries, output_label):
    # Mendapatkan nilai dari input Entry dan menjalankan eliminasi Gauss-Jordan
    matrix = [[0.0] * 4 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            matrix[i][j] = float(matrix_entries[i][j].get())
        matrix[i][3] = float(matrix_entries[i][3].get())

    output_label.config(text="Matriks sebelum eliminasi Gauss-Jordan:\n")
    print_matrix(matrix, output_label)
    output_label.update()

    gauss_jordan_elimination(matrix, output_label)

    output_label.config(text=output_label.cget("text") + "\n\nMatriks setelah eliminasi Gauss-Jordan:\n")
    print_matrix(matrix, output_label)

    output_label.config(text=output_label.cget("text") + f"\n\nJadi solusi persamaan linearnya adalah: x, y, z = ({matrix[0][3]:.2f}, {matrix[1][3]:.2f}, {matrix[2][3]:.2f})")

def create_matrix_input_widgets(root):
    # Membuat widget Entry untuk input matriks
    matrix_entries = []
    for i in range(3):
        row_entries = []
        for j in range(4):
            entry = Entry(root, width=5)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(entry)
        matrix_entries.append(row_entries)
    return matrix_entries

def main():
    root = tk.Tk()
    root.title("Gauss-Jordan Elimination Solver")

    # Membuat widget Entry untuk input matriks
    matrix_entries = create_matrix_input_widgets(root)

    # Membuat label untuk menampilkan output
    output_label = Label(root, text="", justify="left")
    output_label.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

    # Membuat tombol submit
    submit_button = Button(root, text="Submit", command=lambda: on_submit(matrix_entries, output_label))
    submit_button.grid(row=4, column=0, columnspan=4, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

# Classification using PCA-based Method

Pertama-tama, mari kita ``import`` beberapa *libraries* yang akan kita butuhkan dalam metode kali ini.

[1]

Kemudian, kita *load* dataset yang sebelumnya telah diproses menjadi `.pickle` menggunakan ``pickle.load()``. *Return value* berupa data citra serta label kemudian disimpan pada variabel ``ck_data`` dan ``ck_label``. Setelah itu, dilakukan ``split`` untuk membagi data menjadi *training set* dan *test set* dengan perbandingan *training set* sebanyak 75% dan *test set* sebanyak 25%.

[2]

Selanjutnya, kita tampilkan isi data label dengan memanggil ``get_face_label()``.

[3]

## Komputasi EigenFace

Kali ini, kita akan menggunakan metode *Principal Component Analysis* (PCA) untuk *dimensionality reduction*. *Library* `sklearn` yang digunakan merupakan PCA dengan pendekatan *Singular Value Decomposition* (SVD) dari `sklearn.decomposition`. PCA merupakan algoritma *dimensionality reduction* yang umum digunakan dalam EDA dan *Machine Learning*. PCA merupakan metode reduksi dimensi linier klasik yang berupaya menemukan kombinasi linear fitur dalam matriks data berdimensi tinggi.

Beberapa parameter yang digunakan pada proses kali ini yaitu ``n_components``, ``svd_solver``, dan ``whiten``.
- ``n_components`` mengindikasikan jumlah *component* yang akan dipertahankan.
- ``svd_solver`` merupakan *solver* yang dipilih berdasarkan ``X.shape`` dan ``n_components``.
  - Apabila data *input* lebih besar dari 500x500 dan jumlah komponen yang diekstrak lebih rendah dari 80% dari dimensi terkecil data, maka metode yang efisien digunakan yaitu ``randomized``. ``randomized`` menjalankan SVD acak dengan metode Halko et al.
- ``whiten`` akan menghapus beberapa informasi dari *transformed signal* (*relative variance scales* dari komponen-komponen) tetapi terkadang dapat meningkatkan akurasi prediktif dari estimator.
  - Ketika diset ``True`` (*default*: ``False``), ``components_vectors`` akan dikalikan dengan akar dari ``n_samples`` kemudian dibagi dengan *singular values* untuk memastikan *output* yang tidak berkorelasi dengan *variances unit component*.

## Singular Value Decomposition (SVD)

Ada beberapa alasan khusus dalam menggunakan SVD untuk menghitung PCA:
- SVD lebih stabil secara numerik ketika data yang digunakan *collinear*.
- Tradisional PCA memungkinkan mendapatkan *component* dari bilangan imajiner.
- Tradisional PCA tidak bisa diimplementasikan dalam matrix yang besar, tetapi SVD bisa karena kompleksitas SVD lebih rendah.


[4]

Berikut merupakan hasil PCA dari *training set*.

[5]

Berikut merupakan hasil PCA dari *test set*.

[6]

klasifikasi (inan sg njelasno)

[7]


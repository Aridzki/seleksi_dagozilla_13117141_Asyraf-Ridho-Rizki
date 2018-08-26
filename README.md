# Tugas Seleksi Dagozilla

## *Obstacle Avoidance* Menggunakan *Image Processing*

  Seperti yang kita ketahui bahwa *obstacle avoidance* merupakan gerakan untuk menghindari suatu rintangan yang memiliki ciri terntentu. Untuk melakukan *obstacle avoidance*, robot harus mendeteksi objek yang harus dihindari terlebih dahulu. Selanjutnya robot akan melakukan gerakan yang menghindari objek tersebut.
	
  Dalam melakukan deteksi objek, robot haruslah mempunyai kemampuan dalam hal pengelihatan. Oleh karena itu robot harus dipasang kamera. Dari kamera itu robot akan merekam video yang sebenarnya merupakan kumpulan dari gambar-gambar. Dari gambar-gambar tersebut robot dapat melakukan pengolahan gambar yang biasa disebut dengan *image processing*. Salah satu cara melakukan *image processing* adalah dengan menggunakan library OpenCV. Library OpenCV dapat digunakan pada Bahasa pemrogragraman c++ dan juga python. 
	
  Gambar yang ditangkap oleh robot pertama-tama akan disegmentasi seperti yang tertera pada soal. Gambar perlu disegmentasi agar mudah dilakukan Analisa. Karena kamera yang digunakan adalah omnidirectional camera maka gambar perlu diproyeksikan menjadi datar. Dengan proyeksi ini, kita dapat menggunakan pixel pada gambar menjadi koordinat posisi di lapangan. Setelah itu kita akan mengfilter gambar sehingga mengurangi noise yang ada, salah satu jenis filter yang bisa digunakan adalah gaussian filter. Setelah itu, kita dapat melakukan erosi terhadap gambar, bentuk erosi yang kita pilih adalah persegi karena objek yang kita akan deteksi berbentuk kotak. Setelah itu, agar gambar mudah dianalisa, gambar yang tadinya memiliki warna RGB (Red Green Blue) sebaiknya diubah menjadi hitam putih (*Grayscale*). Selanjutnya kita akan melakukan deteksi gambar.
	
  Objek yang ingin kita deteksi berbentuk dua persegi hitam dan dua persegi putih yang saling bersebalahan. Oleh karena itu, kita akan mencari pixel yang bernilai 255 (putih) dan 0 (hitam). Setelah itu kita akan mengecek apakah bentuk kumpulan pixel itu berbentuk persegi, jika iya itu merupakan objek yang kita cari.
	
  Setelah menemukan objek yang harus dihindari, kita harus mecatat posisi pixel tersebut dan mengubah datanya menjadi koordinat di lapangan. Jika robot bergerak secara horizontal, lalu di hadapannya terdapat objek yang harus dihindari, maka robot akan bergeser secara vertical sampai tidak ada objek tersebut di hadapannya. Jika robot bergerak secara vertical, lalu di hadapannya terdapat objek yang harus dihindari, maka robot akan bergeser secara horizontal. Dengan cara seperti ini robot akan di tujuan dengan mengindari objek yang diinginkan.

## Algoritma sudoku.py

1. Pertama program akan mengecek apakah ada paling sedikit ada 3 argumen

Hal ini dapat dilakukan dengan mengimport module sys
2. Program akan membuka file yang tertera pada argument 1 (arg[1])
  - Data yang ada di dalam file input akan dibaca
  - Setiap sel kosong (-) akan diisi 0 sisanya diisi sesuai yang tertera
3. Sudoku yang sudah terbaca akan diprint untuk menunjukan ke user
4. Mulai tahap penyelesaian sudoku
  - Anggap sel (0,0) kosong, array [0,0] akan disimpan di array l
  - Program akan mencari sel kosong (bernilai 0) lalu menyimpan row dan col nya ke array l
  - Jika tidak ada sel yang kosong sudoku selesai
  - Ketika menemukan sel yang kosong, program akan ciba memasukan nilai 1 sampai 9 ke dalam sel
  - Di setiap pengecekan, program akan mengecek setiap row, col, dan block (3x3)
  - Jika di semua percobaan (1 sampai 9) terjadi kegagalan, maka program akan melakukan backtracking
  - Backtracking dilakukan dengan kembali ke sel yang kosong sebelumnya dan mengecek kemungkinan lain untuk mengisi sel kosong tersebut
  - Back tracking akan dilakukan sampai sudoku penuh
5. Ketika sudoku sudah penuh, sudoku yang terbentuk akan diprint dan disimpan pada file yang tertera pada argumrnt kedua

## Algoritma minesweeper.cpp

1. Input data ukuran kotak minesweeper dan jumlah bomb yang diinginkan
   
   Jika bomb yang diberikan melebihi jumlah sel maka akan terjadi looping untuk memasukan data
2. Dari data yang diinput, program akan membuat array 2d yang berisi value dan Boolean (sudah diisi atau belum
    
    Untuk pertama-tama setiap sel diisi 0 dan true
3. Selanjutnya posisi bomb akan dirandom
  - Sel yang berisi bomb akan diberi value -1
  - Program akan menampilkan posisi bob ada di mana saja
4. Program akan melakukan looping sampai selesai
  - Program akan menghitung jumlah sel yang harus dibuka (bukan bomb)
  - User akan mamasukan posisi sel yang ingin dibuka
  - Jika sel berada di luar kotak maka akan terjadi looping (diulang)
  - Program akan mengecek sel yang diminta apakah berisi bomb atau tidak
  - Jumlah sel yang sudah dibuka akan bertambah
  - Jika sel berisi bomb, maka game selesai dan user kalah
Jika sel yang dipilih bernilai 0 maka program akan mengecek dan membuka sel di sekitarnya yang bukan bomb
Jika semua sel yang bukan bomb sudah terbuka maka game selesai dan user menang
Jika masih belum maka looping akan terus berlanjut
5. Jika menang akan ada tulisan menang dan jika kalah akan ada tulisan maaf

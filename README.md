# Tubes-AI 1 Kelompok 25
## Deskripsi Repository
Repository ini berisi algoritma-algoritma local search yang digunakan dalam penyelesaian persoalaan magic cube 5x5x5 yang bertujuan mencari solusi optimal dimana syarat menmenuhi solusi optimal antara lain : 
1. Terdapat satu angka yang disebut sebagai magic number dari kubus tersebut (magic number tidak harus berada 2. dalam rentang angka 1 hingga n3, dan juga bukan merupakan angka yang perlu dimasukkan ke dalam kubus)
3. Jumlah angka-angka pada setiap baris harus sama dengan magic number.
4. Jumlah angka-angka pada setiap kolom juga harus sama dengan magic number.
5. Jumlah angka-angka pada setiap tiang harus sama dengan magic number 
6. Jumlah angka-angka pada setiap diagonal ruang kubus juga sama dengan magic number
7. Jumlah angka-angka pada diagonal-diagonal di setiap potongan bidang dari kubus harus sama dengan magic number.

Dalam repository ini terdapat:
1. Creating.py = berisi objective function
2. RandomRestartHillClimmbing.py
3. SidewayMoveHillClimbing.py
4. SimulatedAnnealing.py
5. SteepestAscentHillClimbing.py
6. StochasticHillClimbing.py
7. genetic.py

## Setup dan Run
Untuk menjalankan salah satu algoritma dapat dilakukan dengan melakukan run code pada tiap file algoritma yang dipilih
Algoritma-algoritma yang dapat dipilih:
1. SteepestAscentHillClimbing :
   Saat di run, user akan diminta untuk menginput duration
   <img src="galeri\Screenshot 2024-11-11 224042.png"></img>
2. SidewayMoveHillClimbing :
   Saat di run, user akan diminta untuk menginput duration dan sidewaymove
   <img src="galeri\Screenshot 2024-11-11 224414.png"></img>
3. SimulatedAnnealing :
   Saat di run, user akan diminta untuk menginput duration dan tenperature
   <img src="galeri\Screenshot 2024-11-11 230356.png"></img>
4. StochasticHillClimbing :
   Saat di run, user akan diminta untuk menginput duration
   <img src="galeri\Screenshot 2024-11-11 230627.png"></img>
5. RandomRestartHillClimmbing
   Saat di run, user akan diminta untuk menginput nilai hillclimbing yang ingio digunakan, durasi, dan     restart
   <img src="galeri\Screenshot 2024-11-11 225536.png"></img>
6. genetic
      Saat di run, user akan diminta untuk menginput jumlah populasi dan jumlah iterasi
   <img src="..\galeri\Screenshot 2024-11-11 225658.png"></img>
   
Setelah di run menghasilkan output state awal, state akhir, total waktu, total iterasi, visualisasi, dan plot nilai objective function
<img src="galeri\image.png"></img>
<img src="galeri\Screenshot 2024-11-11 203142.png"></img>
 <img src="galeri\Screenshot 2024-11-11 211403.png"></img>

 

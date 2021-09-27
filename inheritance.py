class UPI:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

    
    def printname(self):
        print("Nama    : " + self.nama)
        print("Jurusan : " + self.jurusan)
class mahasiswa(UPI):
    def __init__(self, nama, alamat):
        super().__init__(nama, alamat)
        self.nim = "2000675"
        self.semester ="3"
        self.jurusan = "SIK"
    def datamhs(self):
        print("====== Data Mahasiswa ======")
        print("Nama         : ", self.nama)
        print("NIM          : ", self.nim)
        print("Program Studi: ", self.jurusan)
        print("Semester     : ", self.semester)
        print("Alamat       : ", self.alamat)

class dosen(UPI):
    def __init__(self, nama, alamat):
        super().__init__(nama, alamat)

    def datadsn(self):
        print("======== Data Dosen ========")
        print("Nama         : ", self.nama)
        print("Alamat       : ", self.alamat)
        
x =mahasiswa("Putri","Tangerang")
y =dosen("Joko", "Bandung")

x.datamhs()
y.datadsn()
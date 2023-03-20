stockProduct= [
    {
        'Number' : 'A123',
        'Product Name': 'Kayu',
        'Stock' : 100,
        'Type' : 'Jati',
        'Price' : 500000
        
    },
    {
        'Number' : 'A124',
        'Product Name': 'Batako',
        'Stock' : 50,
        'Type' : 'Jumbo',
        'Price' : 150000
        
    },
    {
        'Number' : 'A125',
        'Product Name': 'Pasir',
        'Stock' : 115,
        'Type' : 'Beton',
        'Price' : 250000
        
    },
       {
        'Number' : 'A126',
        'Product Name': 'Semen',
        'Stock' : 125,
        'Type' : 'Prima',
        'Price' : 120500
        
    },
       {
        'Number' : 'A127',
        'Product Name': 'Batu',
        'Stock' : 25,
        'Type' : 'Koral',
        'Price' : 250000
        
    }
]


def bangunan():
    if len(stockProduct) == 0 :
        print('===Tidak ada data===')
    else :
        print('+++Daftar Data Bahan Bangunan di Gudang Suzume+++\n================================================')
        print('Number\t| Product Name\t| Stock\t| Type\t| Price')
        for i in range(len(stockProduct)):
            print('{}\t\t| {}\t| {}\t| {}\t| {}'.format(stockProduct[i]['Number'], stockProduct[i]['Product Name'],stockProduct[i]['Stock'],stockProduct[i]['Type'],stockProduct[i]['Price']))
            print(' ')


def add_bangunan():
    while True:
        ProductNumber = input('Masukkan Product Number : ').capitalize()
        for k in stockProduct:
            if k['Number'] == ProductNumber :
                print('===Data sudah ada===')
                return
        ProductName = input('Masukkan Product Name : ').capitalize()
        ProductStock = input('Masukkan Stock Barang : ')
        ProductType= input('Masukkan Type Barang : ').capitalize()
        ProductPrice = input('Masukkan Price Barang : ')
        
        while True:
            a = input('Apakah data yang anda masukan telah benar (Y/T) :').capitalize()
            if (a == 'Y'):
                stockProduct.append({
                    'Number' : ProductNumber,
                    'Product Name' : ProductName,
                    'Stock' : ProductStock,
                    'Type' : ProductType,
                    'Price' : ProductPrice
                })
                print('===Data tersimpan===')
                return
            elif (a == 'T'):
                break


def update_bangunan():
    while True:
        ProductNumber = (input('Masukkan Product Number yang ingin diganti: ')).capitalize()
        exist = True
        for j in stockProduct:
            if j['Number'] == ProductNumber:
                indexStock = stockProduct.index(j)
                exist = True
                print('Data pada bahan bangunan: \n')
                print('Number\t |Product Name\t |Stock \t|Type \t\t| Price  ')
                print('{}\t | {}  \t | {}\t | {}\t | {}'.format(stockProduct[indexStock]['Number'],stockProduct[indexStock]['Product Name'],stockProduct[indexStock]['Stock'],stockProduct[indexStock]['Type'],stockProduct[indexStock]['Price']))
                print(' ')
                break
            else:
                exist = False
        if exist == False: 
            print('\nData yang anda cari tidak ada!\n')
            menu_3()
            break
        


        update = (input('''
            Data apakah yang ingin Anda update?
            1. Product Name         
            2. Stock
            3. Type
            4. Price
            5. Semua Data
            
            Masukkan angka Menu yang ingin dijalankan: '''))
        if update == '1':
            ProductName = input('Masukkan Name Product : ').capitalize()
            simpan = input('Apakah data mau diperbaharui (Y/T)?').capitalize()
            if simpan == 'Y':
                print(' ')
                print('\nData Terupdate!\n')
                for j in stockProduct:
                    if j['Number'] == ProductNumber:
                        indexStock = stockProduct.index(j)
                        dictProduct = stockProduct[indexStock]
                        dictProduct['Product Name'] = ProductName
                        break
            break
        elif update == '2':
            ProductStock = input('Masukkan Stock: ')
            simpan = input('Apakah data mau diperbaharui (Y/T)?').capitalize()
            if simpan == 'Y':
                print(' ')
                print('\nData Terupdate!\n')
                for j in stockProduct:
                    if j['Number'] == ProductNumber:
                        indexStock = stockProduct.index(j)
                        dictProduct = stockProduct[indexStock]
                        dictProduct['Stock'] = ProductStock
                        break
            break
        elif update == '3':
            ProductType = input('Masukkan Type: ').capitalize()
            simpan = input('Apakah data mau diperbaharui (Y/T)?').capitalize()
            if simpan == 'Y':
                print(' ')
                print('\nData Terupdate!\n')
                for j in stockProduct:
                    if j['Number'] == ProductNumber:
                        indexStock = stockProduct.index(j)
                        dictProduct = stockProduct[indexStock]
                        dictProduct['Type'] = ProductType
                        break
            break
        elif update == '4':
            ProductPrice = input('Masukkan Price: ')
            simpan = input('Apakah data mau diperbaharui (Y/T)?').capitalize()
            if simpan == 'Y':
                print(' ')
                print('\nData Terupdate!\n')
                for j in stockProduct:
                    if j['Number'] == ProductNumber:
                        indexStock = stockProduct.index(j)
                        dictProduct = stockProduct[indexStock]
                        dictProduct['Price'] = ProductPrice
                        break
            break
        elif update == '5':
            ProductName = input('Masukkan Product Name: ')
            ProductStock = input('Masukkan Stock: ')
            ProductType = input('Masukkan Type: ')
            ProductPrice = input('Masukkan Price: ')
            
            simpan = input('Apakah data mau diperbaharui (Y/T)?').capitalize()
            if simpan == 'Y':
                print(' ')
                print('\nData Terupdate!\n')
                for j in stockProduct:
                    if j['Number'] == ProductNumber:
                        indexStock = stockProduct.index(j)
                        dictProduct = stockProduct[indexStock]
                        dictProduct['Product Name'] = ProductName
                        dictProduct['Stock'] = ProductStock
                        dictProduct['Type'] = ProductType
                        dictProduct['Price'] = ProductPrice
                        break
            break   
        else :
            print('===Pilihan yang anda masukan salah===')   


def delete_bangunan():
    ProductNumber = input('Masukan Product Number yang ingin dihapus : ').capitalize()
    PunyaBarang = False
    for i in stockProduct:
        if i['Number'] == ProductNumber :
            while True:
                a = input('Apakah data ingin menghapus data (Y/T) :').capitalize()
                if (a == 'Y'):
                    for k in stockProduct:
                        if k['Number'] == ProductNumber :
                            stockProduct.remove(k)
                            print(' ')
                            print('===Data Deleted===')
                            PunyaBarang = True
                            return
                elif (a == 'T'):
                    break
    if PunyaBarang == False :
        print(' ')
        print ('===Data yang anda cari tidak ada!===')


def show_menu():
    print('========Gudang Bahan Bangunan Suzume=======')
    print(' ')
    print('List Menu:')
    print('1. Menampilkan Daftar Data Bahan Bangunan')
    print('2. Menambahkan Data Bahan Bangunan')
    print('3. Memperbarui Data Bahan Bangunan')
    print('4. Menghapus Data Bahan Bangunan')
    print('5. Keluar dari program')
    print(' ')


def menu_1():
    while True :
        print('Data Bahan Bangunan di Gudang')
        print(' ')
        print('1. Tampilkan Seluruh Daftar Data Bahan Bangunan')
        print('2. Tampilkan Data Bahan Bangunan Tertentu')
        print('3. Kembali ke Menu Utama')
        print(' ')
        MenuSatu = input('Silahkan pilih sub menu (1-3) : ')
        if(MenuSatu == '1') :
            bangunan()
        elif(MenuSatu == '2') :
            bangunan_tertentu()
        elif(MenuSatu == '3') :
            break
        else :
            print('===Pilihan yang anda masukan salah===')


def bangunan_tertentu():
    ProductNumber = input('Masukkan Product Number : ').capitalize()
    PunyaBarang = False
    for i in stockProduct:
        if i['Number'] == ProductNumber :
            print(' Number\t| Product Name\t| Stock\t| Type\t| Price ')
            print(' {}\t\t| {}\t| {}\t| {}\t| {}'.format(i['Number'],i['Product Name'],i['Stock'],i['Type'],i['Price']))
            print(' ')
            PunyaBarang = True
    if PunyaBarang == False :
        print ('===Tidak Ada Data===')


def menu_2():
     while True :
        print('Tambah Data Bahan Bangunan di Gudang')
        print(' ')
        print('1. Tambah Data Bahan Bangunan di Gudang')
        print('2. Kembali ke Menu Utama')
        MenuDua = input('Silahkan pilih sub menu (1-2) : ')
        if(MenuDua == '1') :
            add_bangunan()
            bangunan()
        elif(MenuDua == '2') :
            break
        else :
            print('===Pilihan yang anda masukan salah===')


def menu_3():
     while True :
        print('Update Data Bahan Bangunan di Gudang')
        print(' ')
        print('1. Update Data Bahan Bangunan di Gudang')
        print('2. Kembali ke Menu Utama')
        MenuTiga = input('Silahkan pilih sub menu (1-2) :  ')
        if MenuTiga == '1':
            update_bangunan()
            bangunan()
        elif MenuTiga == '2':
            break
        else :
            print('===Pilihan yang anda masukan salah===')

           
def menu_4 ():
    while True :
        print('Hapus Data Bahan Bangunan di Gudang')
        print(' ')
        print('1. Hapus Data Bahan Bangunan di Gudang')
        print('2. Kembali ke Menu Utama')
        MenuEmpat = input('Silahkan pilih sub menu (1-2) : ')
        if(MenuEmpat == '1') :
            delete_bangunan()
            bangunan()
        elif(MenuEmpat == '2') :
            break
        else :
            print('===Pilihan yang anda masukan salah===')


while True :
    show_menu()
    PilihanMenu = input ('Masukkan angka Menu yang ingin dijalankan : ')
    if(PilihanMenu == '1') :
        menu_1()
    elif(PilihanMenu == '2') :
        menu_2()
    elif(PilihanMenu == '3') :
        menu_3()
    elif(PilihanMenu == '4') :
        menu_4()
    elif(PilihanMenu == '5') :
        break
    else :
        print('===Pilihan yang Anda Masukan Salah===')

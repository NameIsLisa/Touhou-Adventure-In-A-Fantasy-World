define Y = Character("You", color="#ffffff") #Ini ada di line 16. 
define r = Character("Reimu", color="#ff0000") #Ini ada di line 19
# ^ yang di atas dimulai dari line 16

label start:
    #di bawah ini adalah dialog-dialog!
    "Halo, ini dialog ku!"
    "mana dialog mu?"

    #kamu juga bisa menambahkan nama karakter, tanpa itu kita tidak tau siapa yang berbicara kan?
    "Dev""Ini aku!"
    ## Sebelum dialog, tambahkan "" dan masukan nama didalamnya(namanya terserah kamu) 
    ## "Dev" < nama karakter | "Ini aku!" < dialog.

    # Kamu juga bisa mempersingkatnya!
    Y "Aku kamu!" # lihat line 1
    # define 'serah kamu' = Character("Name", color="")  mendefinisikan abjad(JANGAN ANGKA!) untuk uh... bisa dibilang mempersingkat nama yang panjang...
    # dibagian color="" kamu bisa mengubah warna namanya, seperti #ffffff untuk putih, #ff0000 untuk merah, dll
    r "Testing testing..." # Y(huruf besar) r(huruf kecil) itu tidak masalah! selagi bukan angka ya~

    return

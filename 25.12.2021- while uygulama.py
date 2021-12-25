# kullanıcı adı: admin, şifre: 123456 yazınca sisteme giriş başarılı bunları dışında bir şey yazınca kullanıcı adı veya
# şifre hatalı diyerek tekrar kullanıcı adı ve şifre isteyen program geliştiriniz
while True:
   kullanıcıadı=input("kullanıcı adı giriniz").lower()
   sifre=input("şifre giriniz")
   if kullanıcıadı=="admin" and sifre=="123456":
        print("sisteme giriş başarılı")
        break
   else:
        print("kullanıcı adı veya şifre hatalı")

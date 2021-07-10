import instaloader

ini = instaloader.Instaloader()
UserName = input('Informe o nome do Usuário: ')

ini.download_profile(UserName, profile_pic_only=True)

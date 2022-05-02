import ctypes
import string
import os
import time
LICNECE = """
"""

USE_WEBHOOK = True

print(LICNECE)

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:  
    from discord_webhook import DiscordWebhook  
except ImportError:  
    
    input(
        f"Le module discord_webhook n'est pas installé, pour l'installer veuillez faire '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nVous pouvez ignorez cette erreur si vous n'utilisez pas de webhook.\nPressez entrer pour continuer.")
    USE_WEBHOOK = True
try:  
    import requests  
except ImportError:  
    
    input(
        f"Le module requests n'est pas installé, pour l'installer veuillez faire '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\nAppuyez sur Entrée pour quitter.")
    exit()  
try:  
    import numpy  
except ImportError:  
   
    input(
        f"Le module numpy n'est pas installé, pour l'installer veuillez faire '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\nAppuyez sur Entrée pour quitter.")
    exit()  


url = "https://github.com"
try:
    response = requests.get(url)  
    print("Internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:
    
    input("Vous n'êtes pas connecté à Internet, vérifiez votre connexion et réessayez.\nAppuyez sur Entrée pour quitter.")
    exit()  


class NitroGen:  
    def __init__(self):  
        self.fileName = "Nitro Codes.txt"  

    def main(self):  
        os.system('cls' if os.name == 'nt' else 'clear')  
        if os.name == "nt":  
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "Nitro Generateur et Checker - By keizu#4369") 
        else:  
            print(f'\33]0;Nitro Generateur et Checker - By keizu#4369\a',
                  end='', flush=True)  

        print(""" █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗██╗  ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║╚██╗██╔╝
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██║ ██╔██╗
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
                                                        """)  
        time.sleep(2)  
        
        self.slowType("By: keizu#4369", .02)
        time.sleep(1)  
        
        self.slowType(
            "\nEntrez le nombre de codes à générer et à checker: ", .02, newLine=False)

        try:
            num = int(input(''))  
        except ValueError:
            input("Ce que vous avez entrée n'est pas un nombre.\nAppuyez sur Entrée pour quitter.")
            exit()  

        if USE_WEBHOOK:
            
            self.slowType(
                "Si vous souhaitez utiliser un webhook Discord, saisissez-le ici ou appuyez sur Entrée pour ignorer : ", .02, newLine=False)
            url = input('')  
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(  
                        url=url,
                        content=f"```Vérification des URL en cours, tout les codes valides apparaitront ici.```"
                    ).execute()

        

        valid = []  
        invalid = 0  
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        
        c = numpy.random.choice(chars, size=[num, 16])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}"  # Generate the url

                result = self.quickChecker(url, webhook)  # Check the codes

                if result:  
                    
                    valid.append(url)
                else: 
                    invalid += 1  
            except KeyboardInterrupt:
                
                print("\nInterrompu par l'utilisateur")
                break  

            except Exception as e:  
                print(f" Erreur | {url} ")  

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generateur et Checker - {len(valid)} Valide | {invalid} Invalide - By keizu#4369")  
                print("")
            else:  
                
                print(
                    f'\33]0;Nitro Generateur et Checker - {len(valid)} Valid | {invalid} Invalid - By keizu#4369\a', end='', flush=True)

        print(f"""
Résultats:
 Valide : {len(valid)}
 Invalide: {invalid}
 Valide Codes: {', '.join(valid)}""")  

        
        input("\nC'est fini ! Appuyez 5 fois sur Entrée pour fermer le programme.")
        [input(i) for i in range(4, 0, -1)]  

    
    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:  
            
            print(i, end="", flush=True)
            time.sleep(speed)  
        if newLine:  
            print()  

    def quickChecker(self, nitro:str, notify=None):  
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)  

        if response.status_code == 200:  
            
            print(f" Valide | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("Nitro Codes.txt", "w") as file:  
                
                file.write(nitro)

            if notify is not None:  
                DiscordWebhook(  
                    url=url,
                    content=f"Un code nitro valide a été détecté ! @everyone \n{nitro}"
                ).execute()

            return True  

        
        else:
           
            print(f" Invalid | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False  


if __name__ == '__main__':
    Gen = NitroGen()  
    Gen.main()  

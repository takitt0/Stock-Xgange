from conn import Database
from mysql.connector import Error
from datetime import datetime
from utils import ginp
import getpass
import config
import os
import socket
import sys
import logging
import admin

class Main:
    def __init__(self):
        self._logged = False
        self._username = None

    def login(self):
        try:
            while self._logged == False:
                usn = ginp(str, "Ingresa un nombre")
                psw = getpass.getpass("Ingresa tu contraseña para hacer login (secreta): ")
                
                if (usn == "quit") or (psw == 'quit'):
                    os.system('cls')
                    break

                if self.check_log(usn, psw):
                    os.system('cls')
                    print("Logged in")

                    self._username = usn
                    self._logged = True
                else:
                    os.system('cls')
                    print("Incorrect")
            
            return self
        
        except Error as e:
            logging.error(e)
            print(f"Ocurrio un error en el registro, reinicia el programa: {e}")
            conn.close_conn()
            sys.exit()

        except Exception as e:
            print(f"Ocurrio un error interno, reinicia el programa: {e}")
            conn.close_conn()
            sys.exit()
            
    def register(self):
        try:
            while self._logged == False:
                usn = ginp(str, "Ingresa un nombre para registrar")
                psw = getpass.getpass("Ingresa una contraseña para registrar (secreta): ")
                dtn = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if (usn == "quit") or (psw == 'quit'):
                    os.system('cls')
                    break

                ip_ad = socket.gethostname()
                
                if len(usn) >= config.max_user_len or len(psw) >= config.max_pwd_len:
                    os.system('cls')
                    print("Inserta un valor valido")
                    continue
                
                if self.check_user(usn):
                    os.system('cls')
                    print("Ingresa otro nombre, este ya esta ocupado")
                    continue

                if len(psw) <= 4:
                    os.system('cls')
                    print("Usa una contraseña más larga de 4 caracteres")
                    continue
                
                if usn.lower() == psw.lower():
                    os.system('cls')
                    print("No puedes tener el mismo usuario y la misma contraseña")
                    continue
                
                if ' ' in usn:
                    os.system('cls')
                    print("No puedes tener espacios en tu usuario")
                    continue
                
                if False in [letter in config.available_chars for letter in usn]:
                    os.system('cls')
                    print("Tienes caracteres no validos.")
                    continue

                conn.callpr("insert_acc", (usn, psw, ip_ad, 1, dtn))
                os.system('cls')

                return self
            
        except Error as e:
            logging.error(e)
            print(f"Ocurrio un error en el registro, reinicia el programa: {e}")
            conn.close_conn()
            sys.exit()

        except Exception as e:
            logging.error(e)
            print(f"Ocurrio un error interno, reinicia el programa: {e}")
            conn.close_conn()
            sys.exit()

    def check_user(self, username):
        return bool(conn.callfc("check_usn", (username,))[0][0])
    
    def check_log(self, username, password):
        return bool(conn.callfc("check_log", (username, password))[0][0])
    
if __name__ == '__main__':
    logging.basicConfig(filename=config.log_normal, encoding="utf-8", level=logging.DEBUG)
    
    mainf = Main()

    conn = Database(**config.config)
    
    while (mainf._logged == False):
        ans = ginp(str, config.log_question)

        match ans:
            case config.login_case:
                os.system('cls')
                mainf.login()

            case config.register_case:
                os.system('cls')
                mainf.register() 

            case config.manual_case:
                os.system('cls')
                print("Lee README.md")

            case config.exit_case:
                sys.exit()
                
            case _:
                print("Opción Desconocida")
    # print(conn.callfc("check_usn", ("Juanifdto",))[0])
    # print(conn.callpr("insert_val", ("Pera 2", 3000, 12)))
    #print("test")
    admin.main(conn, mainf._username)
    print("Mostrar panel de admin")
    conn.close_conn()
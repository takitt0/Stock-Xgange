from utils import ginp, abreviation
from mysql.connector import Error
from datetime import datetime
import logging
import config
import os
import sys

class Main:
    def __init__(self):
        pass

    def insert_item(self, conn, perms, user_request):
        try:
            while perms >= 2:
                self.name = ginp(str, "Ingresa el nombre")
                self.abreviacion = ginp(str, "Ingresa una abreviación (máximo 4 caracteres, dejar en blanco para automatico)")
                self.unit = ginp(str, "Ingresa la unidad de medida (p.e 200 gr.)")
                self.stock = ginp(None, "Ingresa el numero de stock actual")
                self.price = ginp(None, "Ingresa el precio por unidad")
                self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                if self.abreviacion == " " or self.abreviacion == "":
                    self.abreviacion = abreviation(self.name)

                self.data = (self.name, self.price, self.stock, self.unit, self.abreviacion, user_request, self.date)
                
                if any([choice == "quit" or choice == 0 for choice in self.data]):
                    os.system('cls')
                    break

                if len(self.name) < 2:
                    os.system('cls')
                    print("Ingresa un nombre mas largo de 2 caracteres")
                    continue

                if any([not(letter in config.available_item_chars) for letter in self.name]):
                    os.system('cls')
                    print("No puedes poner caracteres invalidos (en el manual están)")
                    continue
                

                conn.callpr("insert_item", self.data)
                os.system('cls')
                print(self.data)

                return self
            else:
                os.system('cls')
                print("No tienes permisos")
        
        except Error as e:
            logging.error(e)
            print(f"Ocurrio un error en el registro, reinicia el programa: {e}")
            conn.close_conn()
            sys.exit()

        except Exception as e:
            print(f"Ocurrio un error interno, reinicia el programa: {e}")
            conn.close_conn()
            sys.exit()

def main(conn, name):
    logging.basicConfig(filename=config.log_normal, encoding="utf-8", level=logging.DEBUG)
    mainf = Main()
    perms = int(conn.callfc("get_perms", (name, ))[0][0])

    logging.error(f"{perms}, {name}")
    while True:
        ans = ginp(str, config.admin_question)

        match ans:
            case config.insert_case:
                os.system('cls')
                mainf.insert_item(conn, perms, name)
            
            case config.delete_case:
                os.system('cls')
                print("WIP")

            case config.info_case:
                os.system('cls')
                print("WIP")

            case config.exit_case:
                os.system('cls')
                sys.exit()
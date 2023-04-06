import string

# Database config
config = dict(
        host="localhost",
        database="stock_xgange",
        user="root",
        passw="edsitopro"
)
max_user_len = 100
max_pwd_len = 250
max_abrev_len = 5

#Perms
insert_and_delete_perm = 2
# Dirs
log_normal = r"C:\Users\Acer\PycharmProjects\stock_xgange\logs\reg.log"
log_sql = r"C:\Users\Acer\PycharmProjects\stock_xgange\logs\regsql.log"

# Login & register cases
login_case = "1"
register_case = "2"
manual_case = "3"
exit_case = "4"

# Query case
insert_q_case = "1"
delete_q_case = "2"
sum_q_case = "3"
rest_q_case = "4"
exit_q_case = "5"

# Admin cases
insert_case = "1"
delete_case = "2"
info_case = "3"
ad_exit_case = "4"
# Other
available_chars = string.digits + string.ascii_letters + "_-"
available_item_chars = available_chars + " "

# ASCII Art
log_question = rf"""
        
                    S T O C K - X G A N G E

        1. Login
        2. Registrar
        3. Manual
        4. Salir
    """

admin_question = rf"""
        
                 S T O C K - X G A N G E // A D M I N

        1. Insertar Item
        2. Eliminar Item
        3. Info. cuenta
        4. Salir
    """
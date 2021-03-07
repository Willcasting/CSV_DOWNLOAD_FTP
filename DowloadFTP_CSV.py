#Versão 1.0
#Criado por William Freitas dos Santos 
#Data 04/03/2021


from ftplib import FTP
from datetime import datetime
import time, shutil, os

date = datetime.now()
dateModified = date.strftime("%Y%m%d")

ftpServer = "server"
ftpPassword = "senha"
ftpUser = "usuario"

pathCSV = "caminho para salvar os arquivos"

pathOutCSV = "caminho final dos arquivos"

print("#######################"+date.strftime("%d/%m/%Y %H:%M")+"################################")
print("Data de pesquisa do arquivo: "+ date.strftime("%d/%m/%Y %H:%M"))
print("Data de modificada para pesquisa do arquivo: " + dateModified)
print("Entrando no servidor FTP:" + ftpServer)
time.sleep(1)
ftp = FTP(ftpServer)
ftp.login(ftpUser, ftpPassword)

print("Entrando na PASTA do servidor FTP")
ftp.cwd("PASTA")

for name in ftp.nlst():
        if dateModified in name:
                print("Download do arquivo ... " + name);
                time.sleep(1.5)
                ftp.retrbinary("RETR " + name, open(pathCSV + name, 'wb').write)

print("Saindo do servidor FTP...")
ftp.close()

for root, dirs, files in os.walk(pathCSV):
        for file in files:
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(pathOutCSV, file)
                shutil.move(old_file_path,new_file_path)
                print(file + " Arquivo movido com sucesso !")

endDate = datetime.now()

print("Data final da rotina CSV: ", endDate.strftime("%d/%m/%Y %H:%M"))
print("#######################################################")

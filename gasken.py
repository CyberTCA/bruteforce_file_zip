#coding: utf-8

# module yang di butuhkan
import zipfile,os,sys,time

# untuk membersihkan text
clear = lambda : os.system("clear")


# brute force zip
def brute():
  banner = """
\033[1;90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;96mஜ۩۞۩ஜ\033[1;90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
 \033[1;90m{\033[1;96m•\033[1;90m} \033[1;93mAuthor      \033[1;91m:  \033[1;95mDimas Aryo
 \033[1;90m{\033[1;96m•\033[1;90m} \033[1;93mFacebook    \033[1;91m:  \033[1;95mDimas Aryo
 \033[1;90m{\033[1;96m•\033[1;90m} \033[1;93mYouTube     \033[1;93m: \033[1;95m Mr Tcg Cyber
 \033[1;90m{\033[1;96m•\033[1;90m} \033[1;93mInstagram   \033[1;91m:  \033[1;95m@dimasaryo_17
 \033[1;90m{\033[1;96m•\033[1;90m} \033[1;93mJenis Tools \033[1;91m:  \033[1;95mBrute/Brute Force Zip
\033[1;90m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"""
  clear()
  print banner
  filezip = raw_input(" \033[1;90m{\033[1;95m+\033[1;90m} \033[1;96mMasukan lokasi file zip \033[1;91m>\033[1;92m  ")
  wordlist = raw_input(" \033[1;90m{\033[1;95m+\033[1;90m} \033[1;96mMasukan Lokasi File Wordlist \033[1;91m>\033[1;92m  ")
  x = zipfile.ZipFile(filezip)
  p = open(wordlist, "r")
  a = 0
  for o in p.readlines():
    password = o.strip()
    try:
      x.extractall(pwd=password)
      print "\033[1;96m+\033[1:90m======================\033[1;95m",a,"\033[1;90m====================="
      print " \033[1;90m{\033[1;92m•\033[1;90m} \033[1;92mpassword di temukan"
      print " \033[1;90m{\033[1;92m•\033[1;90m} \033[1;92mpassword \033[1;90m~\033[1;96m•\033[1;93m>\033[1;95m",password
      break
    except:
      print " \033[1;90m{\033[1;91m",a,"\033[1;90m} \033[1;91mFailed \033[1;90m~\033[1;96m•\033[1;93m>\033[1;96m",password
      a += 1


# memanggil function brute
brute()

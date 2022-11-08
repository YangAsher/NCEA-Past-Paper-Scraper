import requests, os, colorama

os.system("title NCEA Past Paper Scraper - Made by Asher Yang")
os.system("cls")

def scrape():
  # Parameters
  current_year = 2022
  subj = input("Subject Name (eg calc, chem, bio)\n> ")
  ass = input("Achievement Standard (eg 91577)\n> ")

  try:
    if len(ass) == 5:
      ass = int(ass)
    else:
      print("AS number (eg 91577) should be 5 characters")
  except:
    print("Please input the AS number (eg 91577)")

  # Make the folders
  try: os.mkdir(subj)
  except: pass

  try: os.mkdir(f"{subj}/{ass}")
  except: pass
  try: os.mkdir(f"{subj}/{ass}/exm")
  except: pass
  try: os.mkdir(f"{subj}/{ass}/ass")
  except: pass

  r = requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/2013/{ass}-ass-2013.pdf").status_code # take mark scheme, it is smaller than question book most of the time
  if r == 200:
    NCEA = True
    print(f"{colorama.Fore.GREEN}[Paper Detected]{colorama.Fore.WHITE} NCEA paper detected")
  elif r == 404:
    NCEA = False
    r2 = requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/2013/{ass}-qbk-2013.pdf").status_code #some scholarship papers use qbk (math, english), others exm (sciences). we must account for this. waste of bandwidth tbh
    if r2 == 200:
      print(f"{colorama.Fore.GREEN}[Paper Detected]{colorama.Fore.WHITE} Scholarship paper type qbk (likely math or essay) detected")
      papertype = "qbk"
    else:
      r3 = requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/2013/{ass}-exm-2013.pdf").status_code
      if r3 == 200:
        print(f"{colorama.Fore.GREEN}[Paper Detected]{colorama.Fore.WHITE} Scholarship paper type exm (likely science) detected")
        papertype = "exm"
      if r == r2 == r3 == 404:
        print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.WHITE} Paper not found. Did you input the correct AS number?")
        scrape()


  # Steal the files hehe
  for n in range(current_year, 2013, -1):
    n -= 1 #computer numbers momento

    if NCEA == True: # NCEA Papers
        open(f"{subj}/{ass}/exm/{ass}-exm-{n}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/{n}/{ass}-exm-{n}.pdf").content)
        print(f"{colorama.Fore.WHITE}Downloaded exam paper {colorama.Fore.CYAN}{ass}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{n}{colorama.Fore.WHITE}.")
        open(f"{subj}/{ass}/ass/{ass}-ass-{n}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/schedules/{n}/{ass}-ass-{n}.pdf").content)
        print(f"{colorama.Fore.WHITE}Downloaded marking scheme {colorama.Fore.CYAN}{ass}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{n}{colorama.Fore.WHITE}.")
    if NCEA == False: # Scholarship Papers
        open(f"{subj}/{ass}/exm/{ass}-{papertype}-{n}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/{n}/{ass}-{papertype}-{n}.pdf").content) #papertype as math/essay exams have a qbk and abk
        print(f"{colorama.Fore.CYAN}[SCHOLARSHIP] {colorama.Fore.WHITE}Downloaded exam paper {colorama.Fore.CYAN}{ass}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{n}{colorama.Fore.WHITE}.")
        open(f"{subj}/{ass}/ass/{ass}-ass-{n}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/{n}/{ass}-ass-{n}.pdf").content)
        print(f"{colorama.Fore.CYAN}[SCHOLARSHIP] {colorama.Fore.WHITE}Downloaded marking scheme {colorama.Fore.CYAN}{ass}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{n}{colorama.Fore.WHITE}.")


scrape()
input("All papers downloaded. Press [ENTER] to exit.")

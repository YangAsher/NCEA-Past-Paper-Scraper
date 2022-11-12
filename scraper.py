import requests
import os
import colorama

os.system("title NCEA Past Paper Scraper - Made by Asher Yang")
os.system("cls")

def scrape(first_year=2013, last_year=2021):
	"""
	Find all NCEA past papers for an achievement standard between specified years.

	Keyword arguments:
	first_year -- The earliest year from which we want to download papers (default 2013)
	last_year -- The latest year from which we want to download papers (default 2021)
	"""

	subject = input("Subject Name (e.g. calc, chem, bio)\n> ")

	# Loop until user enters a standard in the correct format
	while True:
		standard = input("Achievement Standard (e.g. 91577)\n> ")

		# Check if the entered standard is a 5 digit number
		if len(standard) == 5 and standard.isdigit():
			break

		print("Achievement Standard should consist of 5 numbers (e.g. 91577)")

	# Check if directory already exists
	if not os.path.exists(subject):
		# Make required directories
		os.mkdir(subject)
	if not os.path.exists(f"{subject}/{standard}"):
		os.mkdir(f"{subject}/{standard}")
	if not os.path.exists(f"{subject}/{standard}/exm"):
		os.mkdir(f"{subject}/{standard}/exm")
	if not os.path.exists(f"{subject}/{standard}/ass"):
		os.mkdir(f"{subject}/{standard}/ass")

	# If an assessment standard is a scholarship paper or not 
	scholarship_paper = False

	# Attempt to find marking scheme for given assessment standard
	r = requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/schedules/2013/{standard}-ass-2013.pdf", stream=True).status_code 

	# Check if paper is NCEA or Scholarship paper
	if r == 200:
		print(f"{colorama.Fore.GREEN}[Paper Detected]{colorama.Fore.WHITE} NCEA paper detected")
	elif r == 404:
		# Some scholarship papers use qbk (math, english), others exm (sciences)
		# To account for this, we make a request to both urls and check if either returns a 200 status
		r2 = requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/2013/{standard}-qbk-2013.pdf", stream=True).status_code 
		r3 = requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/2013/{standard}-exm-2013.pdf", stream=True).status_code
		scholarship_paper = True # if it isn't, r2/3 will 404 and else will make the func recur
		if r2 == 200:
			print(f"{colorama.Fore.GREEN}[Paper Detected]{colorama.Fore.WHITE} Scholarship paper type qbk (likely math or essay) detected")
			papertype = "qbk"
		elif r3 == 200:
			print(f"{colorama.Fore.GREEN}[Paper Detected]{colorama.Fore.WHITE} Scholarship paper type exm (likely science) detected")
			papertype = "exm"
		else:
			print(f"{colorama.Fore.RED}[ERROR]{colorama.Fore.WHITE} Paper not found. Did you input the correct AS number?")
			scrape()

	# Download files between first_year and last_year
	for year in range(first_year, last_year + 1):
		if scholarship_paper:
			open(f"{subject}/{standard}/exm/{standard}-{papertype}-{year}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/{year}/{standard}-{papertype}-{year}.pdf").content) 
			print(f"{colorama.Fore.CYAN}[SCHOLARSHIP] {colorama.Fore.WHITE}Downloaded exam paper {colorama.Fore.CYAN}{standard}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{year}{colorama.Fore.WHITE}.")
			open(f"{subject}/{standard}/ass/{standard}-ass-{year}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/assets/scholarship/{year}/{standard}-ass-{year}.pdf").content)
			print(f"{colorama.Fore.CYAN}[SCHOLARSHIP] {colorama.Fore.WHITE}Downloaded marking scheme {colorama.Fore.CYAN}{standard}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{year}{colorama.Fore.WHITE}.")
		else: 
			open(f"{subject}/{standard}/exm/{standard}-exm-{year}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/exams/{year}/{standard}-exm-{year}.pdf").content)
			print(f"{colorama.Fore.WHITE}Downloaded exam paper {colorama.Fore.CYAN}{standard}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{year}{colorama.Fore.WHITE}.")
			open(f"{subject}/{standard}/ass/{standard}-ass-{year}.pdf", 'wb').write(requests.get(f"https://www.nzqa.govt.nz/nqfdocs/ncea-resource/schedules/{year}/{standard}-ass-{year}.pdf").content)
			print(f"{colorama.Fore.WHITE}Downloaded marking scheme {colorama.Fore.CYAN}{standard}{colorama.Fore.WHITE} from {colorama.Fore.CYAN}{year}{colorama.Fore.WHITE}.")
	
	input("All papers downloaded. Press [ENTER] to exit.")

if __name__ == "__main__":
	scrape()

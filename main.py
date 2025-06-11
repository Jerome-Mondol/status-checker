import requests
from colorama import Fore, Style



def pre_run():
    with open("working_links.txt", "w") as file:
        file.write("")
    with open("broken_links.txt", "w") as file:
        file.write("")

pre_run()


URLS = "list.txt" 


def check_site(file_path):
    total = good = bad = 0
    with open(file_path, "r") as file:
        for link in file:
            total += 1
            url = link.strip()
            if not url:
                continue
        
            if not url.startswith("https"):
                url = "https://" + url
                
            try:
                response = requests.get(url, timeout=5)

                if response.status_code == 200:
                    print(f"{Fore.GREEN}[+] {url} is good {Style.RESET_ALL}")
                    with open("working_links.txt", "a") as working_file:
                        working_file.write(f"{url} \n")

                    good += 1
                else:
                    print(f"{Fore.RED}[-] {url} isn't working {Style.RESET_ALL}")
                    with open("broken_links.txt", "a") as broken_links:
                        broken_links.write(f"{url} \n")

                    bad += 1

            except requests.exceptions.RequestException as e:
                print(f"{Fore.RED}[-] {url} failed {Style.RESET_ALL}")
                with open("broken_links.txt", "a") as broken_links:
                        broken_links.write(f"{url} \n")
                
                bad += 1

    print(f"Total Sites: {total}")
    print(f"Good Sites: {good}")
    print(f"Bad sites: {bad}")

check_site(URLS)


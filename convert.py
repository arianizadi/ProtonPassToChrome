import json

PROTON_PASS_FILE = "passwords.json"
OUTPUT_FILE = "passwords.csv"


def main():
    with open(PROTON_PASS_FILE, "r") as f:
        data = json.load(f)

    if data["encrypted"]:
        print("Cannot convert encrypted file.")
        exit(1)

    vaults = list(data["vaults"].keys())

    with open(OUTPUT_FILE, "w") as f:
        f.write("username,password,website\n")
        for vault in vaults:
            for item in data["vaults"][vault]["items"]:
                if item["data"]["type"] != "login":
                    continue
                try:
                    username = item["data"]["content"]["username"]
                    password = item["data"]["content"]["password"]
                    url = (
                        len(item["data"]["content"]["urls"]) > 0
                        and item["data"]["content"]["urls"][0]
                        or ""
                    )
                    f.write(f"{username},{password},{url}\n")
                except:
                    print(f"Error parsing {vault} {item['data']['itemId']}")
                    pass

    print("Conversion complete!")


if __name__ == "__main__":
    main()

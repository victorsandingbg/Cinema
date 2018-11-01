class get_bussdriv:
    with open("busschaffis.txt", "r") as f:
        obs = f.readlines()
        obs = [x.strip() for x in obs]
        print(obs[])
def main():
    get_bussdriv()

if __name__ == '__main__':
    main()
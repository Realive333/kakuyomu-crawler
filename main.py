import package.traveler as traveler
import os

def main():
    
    try:
        os.mkdir('works')
    except OSError as error:
        print(error)
    
    t1 = traveler.Traveler(query = "1177354054880238351")
    t1.travasal()
    
    
if __name__ == '__main__':
    main()
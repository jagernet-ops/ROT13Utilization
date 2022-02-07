print('###############################')
print('    ROT13 Cipher Utilization   ')
print('###############################')
input_string = input("Input the encoded string here: ")
alphabet_lowercase = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m','A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}

output_string = None
def decode():
    print('###############################')
    print('Output: ',end='')
    for i in input_string:
        if i in alphabet_lowercase:
            print(alphabet_lowercase[i], end='')
        else:
            print(i ,end='')

decode()


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* Encryption(char* text, char* key) {
    int textLen = strlen(text);
    int keyLen = strlen(key);
    char* cipherText = (char*)malloc((textLen + 1) * sizeof(char));
    int* cipher = (int*)malloc(keyLen * sizeof(int));

    for (int i = 0; i < keyLen; i++) {
        cipher[i] = (int)(text[i]) - (int)('A') + (int)(key[i]) - (int)('A');
    }

    for (int i = 0; i < keyLen; i++) {
        if (cipher[i] > 25) {
            cipher[i] -= 26;
        }
    }

    for (int i = 0; i < keyLen; i++) {
        cipherText[i] = (char)(cipher[i] + (int)('A'));
    }
    cipherText[keyLen] = '\0';

    free(cipher);
    return cipherText;
}

int main() {
    char plainText[100];
    char key[100];

    printf("text to encrypt :");
    scanf("%s", plainText);

    printf("tell me the key :");
    scanf("%s", key);

    char* encryptedText = Encryption(plainText, key);
    printf("Cipher Text - %s\n", encryptedText);

    free(encryptedText);
    return 0;
}


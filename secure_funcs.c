#include <string.h>

// 문자열 뒤집기
__declspec(dllexport)
void reverse_string(const char *str, char *out) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        out[i] = str[len - i - 1];
    }
    out[len] = '\0';
}

// 토큰 검증 (token == reversed(secret) 비교)
__declspec(dllexport)
int verify_token(const char *token, const char *secret) {
    char reversed[256];
    reverse_string(secret, reversed);
    return strcmp(token, reversed) == 0;
}

// 할인 계산
__declspec(dllexport)
double calculate_discount(double price, double percentage) {
    return price * (1 - percentage / 100.0);
}

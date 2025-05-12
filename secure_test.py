import ctypes

# DLL 로드
lib = ctypes.CDLL('./secure_funcs.dll')

# 함수 시그니처 등록
lib.verify_token.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.verify_token.restype = ctypes.c_int

lib.calculate_discount.argtypes = [ctypes.c_double, ctypes.c_double]
lib.calculate_discount.restype = ctypes.c_double

# 테스트
token = b"321terces" #secret을 뒤집은 값
secret = b"secret123"

result = lib.verify_token(token, secret)
print("✅ Token verified!" if result else "❌ Invalid token.")

price = 100.0
discounted = lib.calculate_discount(price, 15.0)
print(f"💸 Discounted price: {discounted:.2f}")
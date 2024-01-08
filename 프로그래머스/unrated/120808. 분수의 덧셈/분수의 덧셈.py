from math import gcd

def solution(numer1, denom1, numer2, denom2):
    # 두 분수의 분모를 통일하여 분자를 더합니다.
    new_denom = denom1 * denom2
    new_numer = numer1 * denom2 + numer2 * denom1

    # 결과 분자와 분모의 최대공약수를 구합니다.
    greatest_common_divisor = gcd(new_numer, new_denom)

    # 기약 분수로 만듭니다.
    simplified_numer = new_numer // greatest_common_divisor
    simplified_denom = new_denom // greatest_common_divisor

    return [simplified_numer, simplified_denom]



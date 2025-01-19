# Imports
import re

# Define Tokens
TOKEN_TYPES = [
  ('NUMBER', r'\d+'),                                          # 정수
  ('IDENTIFIER', r'[가-힣\w]+'),                        	     # 식별자 (한글 및 영문자)
  ('KEYWORD', r'\b(거짓|없음|참|그리고|라고|참인가|비동기|기다림|종료|모음|건너뛰기|함수|삭제|혹은|아니고만약|아니면|모두아니면|예외|무조건|동안|에서|전역|만약|불러오기|안에|같은가|람다|비지역|부정|또는|넘어가기|예외발생|반환|시도|까지|함께|생성값)\b'),  					# 한국어 키워드
  ('OPERATOR', r'[=+\-*/<>!]+'),                               # 연산자
  ('PARENTHESIS', r'[(){}[\]]'),                               # 괄호
  ('COMMA', r','),                                          	 # 쉼표
  ('COLON', r':'),
  ('SEMICOLON', r';'),                                     	 	 # 세미콜론
  ('STRING', r'"(.*?)"'),                                  		 # 문자열 리터럴
  ('COMMENT', r'#.*'),                                      	 # 주석
  ('WHITESPACE', r'\s+'),                                   	 # 공백
]

# Functions
def tokenize(code):
  tokens = []
  while code:
    match = None
    for token_type, pattern in TOKEN_TYPES:
      regex = re.compile(pattern)
      match = regex.match(code)
      if match:
        tokens.append((token_type, match.group(0)))
        code = code[match.end():]
        break
    if not match:
      print(f"Unhandled part of the code: {code[:10]}")  # 디버깅 출력
      raise SyntaxError(f"Unexpected token: {code[0]}")
  return tokens

source_code = """
함수 더하기(첫번째, 두번째):
    반환 첫번째 + 두번째  # 두 수를 더합니다

# 주석 예제
반지름_값 = 5  # 반지름
결과 = 더하기(반지름_값, 반지름_값 * 2)  # 함수 호출
출력("결과:", 결과)  # 결과 출력

만약 결과 > 10:
    출력("결과가 10보다 큽니다.")
그렇지않으면:
    출력("결과가 10 이하입니다.")
"""

# Run
tokens = tokenize(source_code)
for token in tokens:
    print(token)